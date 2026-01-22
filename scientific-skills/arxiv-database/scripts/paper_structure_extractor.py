#!/usr/bin/env python3
"""
Paper Structure Extractor - Extract structured data from academic papers.

This tool parses papers in various formats (DOCX, PDF, LaTeX) and extracts:
- Metadata (title, authors, abstract)
- Sections and their content
- Figures and tables
- References

This is a focused tool for structure extraction only. For paper evaluation,
use the peer-review or paper-validator skills.

Usage:
    python paper_structure_extractor.py input.pdf
    python paper_structure_extractor.py input.docx --output structure.json
    python paper_structure_extractor.py arxiv:2401.12345 --download
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Optional

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from review import (
    DocxParser,
    LatexParser,
    PaperMetadata,
    PdfParser,
    StructuredPaperData,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PaperStructureExtractor:
    """
    Extract structured data from academic papers.

    Supports:
    - DOCX files
    - PDF files
    - LaTeX files (when LatexParser is available)
    - arXiv papers (downloads PDF first)
    """

    def __init__(self, verbose: bool = False):
        """
        Initialize extractor.

        Args:
            verbose: Enable verbose logging
        """
        self.verbose = verbose
        if verbose:
            logger.setLevel(logging.DEBUG)

        # Initialize parsers
        self.docx_parser = DocxParser(verbose=verbose)
        self.pdf_parser = PdfParser(verbose=verbose)

        # LaTeX parser - optional
        try:
            self.latex_parser = LatexParser(verbose=verbose)
        except ImportError:
            self.latex_parser = None
            if verbose:
                logger.debug("LaTeX parser not available (pylatexenc not installed)")

    def extract_from_file(self, file_path: str) -> StructuredPaperData:
        """
        Extract structure from a file.

        Args:
            file_path: Path to paper file

        Returns:
            StructuredPaperData containing parsed information

        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format not supported
        """
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if not path.is_file():
            raise ValueError(f"Path is not a file: {file_path}")

        # Determine parser based on extension
        suffix = path.suffix.lower()

        if suffix == '.docx':
            logger.info(f"Parsing DOCX file: {path.name}")
            return self.docx_parser.parse(str(path))
        elif suffix == '.pdf':
            logger.info(f"Parsing PDF file: {path.name}")
            return self.pdf_parser.parse(str(path))
        elif suffix in ['.tex', '.latex']:
            if self.latex_parser is None:
                raise ValueError(
                    f"LaTeX parsing not available. Install pylatexenc: "
                    f"pip install pylatexenc>=2.10"
                )
            logger.info(f"Parsing LaTeX file: {path.name}")
            return self.latex_parser.parse(str(path))
        else:
            raise ValueError(
                f"Unsupported file format: {suffix}. "
                f"Supported formats: .docx, .pdf, .tex"
            )

    def extract_from_arxiv(
        self,
        arxiv_id: str,
        download_dir: Optional[str] = None
    ) -> StructuredPaperData:
        """
        Extract structure from arXiv paper.

        Downloads PDF from arXiv first, then parses it.

        Args:
            arxiv_id: arXiv ID (e.g., "2401.12345" or "arxiv:2401.12345")
            download_dir: Directory to download PDF (default: temp directory)

        Returns:
            StructuredPaperData containing parsed information

        Raises:
            ImportError: If arxiv package not available
            ValueError: If paper not found
        """
        try:
            from arxiv_client import ArxivSearcher
        except ImportError:
            raise ImportError(
                "arxiv_client not available. Ensure arxiv_client.py is in the same directory."
            )

        # Clean arXiv ID
        arxiv_id = arxiv_id.replace("arxiv:", "").strip()

        logger.info(f"Fetching paper from arXiv: {arxiv_id}")

        # Get paper metadata
        searcher = ArxivSearcher(verbose=self.verbose)
        paper = searcher.get_paper(arxiv_id)

        if not paper:
            raise ValueError(f"Paper not found on arXiv: {arxiv_id}")

        # Download PDF
        download_dir = download_dir or "/tmp/arxiv_papers"
        Path(download_dir).mkdir(parents=True, exist_ok=True)

        pdf_path = Path(download_dir) / f"{arxiv_id}.pdf"

        if not pdf_path.exists():
            logger.info(f"Downloading PDF to: {pdf_path}")
            success = searcher.download_pdf(arxiv_id, str(pdf_path))
            if not success:
                raise ValueError(f"Failed to download PDF for: {arxiv_id}")
        else:
            logger.info(f"Using cached PDF: {pdf_path}")

        # Parse PDF
        structure = self.extract_from_file(str(pdf_path))

        # Enhance metadata with arXiv information
        structure.metadata.arxiv_id = arxiv_id
        structure.metadata.source_type = "arxiv"
        if not structure.metadata.title and paper.get("title"):
            structure.metadata.title = paper["title"]
        if not structure.metadata.authors and paper.get("authors"):
            structure.metadata.authors = paper["authors"]
        if not structure.metadata.abstract and paper.get("abstract"):
            structure.metadata.abstract = paper["abstract"]

        return structure

    def to_json(self, structure: StructuredPaperData) -> dict:
        """
        Convert structure to JSON-serializable dictionary.

        Args:
            structure: Parsed paper structure

        Returns:
            Dictionary ready for JSON serialization
        """
        return {
            "metadata": {
                "title": structure.metadata.title,
                "authors": structure.metadata.authors,
                "abstract": structure.metadata.abstract,
                "categories": structure.metadata.categories,
                "arxiv_id": structure.metadata.arxiv_id,
                "doi": structure.metadata.doi,
                "pdf_url": structure.metadata.pdf_url,
                "published": structure.metadata.published,
                "updated": structure.metadata.updated,
                "comment": structure.metadata.comment,
                "journal_ref": structure.metadata.journal_ref,
                "source_type": structure.metadata.source_type,
            },
            "sections": {
                title: {
                    "title": section.title,
                    "content": section.content,
                    "level": section.level,
                }
                for title, section in structure.sections.items()
            },
            "figures": [
                {
                    "number": fig.number,
                    "caption": fig.caption,
                    "page_estimate": fig.page_estimate,
                }
                for fig in structure.figures
            ],
            "tables": [
                {
                    "number": table.number,
                    "caption": table.caption,
                    "page_estimate": table.page_estimate,
                }
                for table in structure.tables
            ],
            "references": [
                {
                    "id": ref.id,
                    "text": ref.text,
                    "arxiv_id": ref.arxiv_id,
                    "doi": ref.doi,
                }
                for ref in structure.references
            ],
        }

    def save_to_file(
        self,
        structure: StructuredPaperData,
        output_path: str,
        format: str = "json"
    ):
        """
        Save structure to file.

        Args:
            structure: Parsed paper structure
            output_path: Output file path
            format: Output format ("json" or "markdown")
        """
        output_path = Path(output_path)

        if format == "json":
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(self.to_json(structure), f, indent=2, ensure_ascii=False)
            logger.info(f"Saved structure to: {output_path}")

        elif format == "markdown":
            # Generate markdown report
            lines = []

            # Metadata
            lines.append(f"# {structure.metadata.title}")
            lines.append("")
            if structure.metadata.authors:
                lines.append(f"**Authors:** {', '.join(structure.metadata.authors)}")
            if structure.metadata.arxiv_id:
                lines.append(f"**arXiv ID:** {structure.metadata.arxiv_id}")
            if structure.metadata.doi:
                lines.append(f"**DOI:** {structure.metadata.doi}")
            lines.append("")

            # Abstract
            if structure.metadata.abstract:
                lines.append("## Abstract")
                lines.append("")
                lines.append(structure.metadata.abstract)
                lines.append("")

            # Sections
            lines.append("## Structure")
            lines.append("")
            lines.append(f"- **Sections:** {len(structure.sections)}")
            lines.append(f"- **Figures:** {len(structure.figures)}")
            lines.append(f"- **Tables:** {len(structure.tables)}")
            lines.append(f"- **References:** {len(structure.references)}")
            lines.append("")

            # Section list
            if structure.sections:
                lines.append("### Sections")
                lines.append("")
                for title, section in structure.sections.items():
                    indent = "  " * (section.level - 1)
                    lines.append(f"{indent}- {title}")
                lines.append("")

            # Figures
            if structure.figures:
                lines.append("### Figures")
                lines.append("")
                for fig in structure.figures:
                    lines.append(f"- **Figure {fig.number}:** {fig.caption}")
                lines.append("")

            # Tables
            if structure.tables:
                lines.append("### Tables")
                lines.append("")
                for table in structure.tables:
                    lines.append(f"- **Table {table.number}:** {table.caption}")
                lines.append("")

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            logger.info(f"Saved markdown report to: {output_path}")

        else:
            raise ValueError(f"Unsupported format: {format}")


def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description="Extract structured data from academic papers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Extract from local file
  python paper_structure_extractor.py paper.pdf

  # Save as JSON
  python paper_structure_extractor.py paper.docx -o structure.json

  # Save as markdown
  python paper_structure_extractor.py paper.pdf -o report.md -f markdown

  # Extract from arXiv
  python paper_structure_extractor.py arxiv:2401.12345

  # Extract from arXiv and save
  python paper_structure_extractor.py 2401.12345 -o structure.json

For paper evaluation and review, use the peer-review or paper-validator skills.
        """
    )

    parser.add_argument(
        "input",
        help="Input file path or arXiv ID (e.g., 'paper.pdf' or 'arxiv:2401.12345')"
    )

    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: print to stdout)"
    )

    parser.add_argument(
        "-f", "--format",
        choices=["json", "markdown"],
        default="json",
        help="Output format (default: json)"
    )

    parser.add_argument(
        "-d", "--download-dir",
        help="Directory for downloading arXiv PDFs (default: /tmp/arxiv_papers)"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    # Create extractor
    extractor = PaperStructureExtractor(verbose=args.verbose)

    try:
        # Determine if input is arXiv ID or file path
        input_str = args.input.strip()

        if input_str.startswith("arxiv:") or (
            len(input_str.replace(".", "")) <= 10 and "." in input_str
        ):
            # Looks like arXiv ID
            structure = extractor.extract_from_arxiv(
                input_str,
                download_dir=args.download_dir
            )
        else:
            # File path
            structure = extractor.extract_from_file(input_str)

        # Output
        if args.output:
            extractor.save_to_file(structure, args.output, format=args.format)
        else:
            # Print to stdout
            if args.format == "json":
                print(json.dumps(extractor.to_json(structure), indent=2, ensure_ascii=False))
            else:
                # For markdown, save to temp file and print
                import tempfile
                with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
                    temp_path = f.name
                extractor.save_to_file(structure, temp_path, format="markdown")
                with open(temp_path, 'r') as f:
                    print(f.read())
                Path(temp_path).unlink()

        logger.info("Structure extraction completed successfully")
        return 0

    except Exception as e:
        logger.error(f"Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
