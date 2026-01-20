"""
PDF parser for extracting text and structure from arXiv papers.

Uses pypdf for robust PDF text extraction.
"""

import io
import re
from typing import Any, BinaryIO, Optional

import pypdf


class PDFParser:
    """Extract text and structure from PDF files."""

    def __init__(self, verbose: bool = False):
        """
        Initialize PDF parser.

        Args:
            verbose: Enable verbose logging
        """
        self.verbose = verbose

    def extract_text(self, pdf_path: str) -> str:
        """
        Extract all text from a PDF file.

        Args:
            pdf_path: Path to PDF file

        Returns:
            Extracted text content
        """
        with open(pdf_path, "rb") as f:
            return self._extract_pypdf(f)

    def extract_text_from_bytes(self, pdf_bytes: bytes) -> str:
        """
        Extract text from PDF bytes.

        Args:
            pdf_bytes: Raw PDF bytes

        Returns:
            Extracted text content
        """
        return self._extract_pypdf(io.BytesIO(pdf_bytes))

    def _extract_pypdf(self, source: BinaryIO | io.BytesIO) -> str:
        """Extract text using pypdf."""
        reader = pypdf.PdfReader(source)
        text_parts = []

        for page in reader.pages:
            text = page.extract_text()
            if text:
                text_parts.append(text)

        return "\n\n".join(text_parts)

    def extract_structured(self, pdf_path: str) -> dict:
        """
        Extract structured information from PDF.

        Args:
            pdf_path: Path to PDF file

        Returns:
            Structured extraction dictionary
        """
        text = self.extract_text(pdf_path)

        return {
            "text": text,
            "sections": self._extract_sections(text),
            "figures": self._extract_figures(text),
            "tables": self._extract_tables(text),
            "equations": self._extract_equations(text),
            "references": self._extract_references(text),
            "metadata": self._extract_metadata(text),
        }

    def _extract_sections(self, text: str) -> dict:
        """Extract paper sections."""
        sections = {}

        section_patterns = [
            ("abstract", r"(?i)(?:^|\n)(abstract)\s*[:\n](.+?)(?=\n\s*(?:1\.?|introduction|background))"),
            ("introduction", r"(?i)(?:^|\n)(1\.?\s*(?:introduction)?)\s*[:\n](.+?)(?=\n\s*(?:2\.?|related work|background))"),
            ("related_work", r"(?i)(?:^|\n)(2\.?\s*(?:related work|background)?)\s*[:\n](.+?)(?=\n\s*(?:3\.?|method|approach|methodology))"),
            ("methodology", r"(?i)(?:^|\n)(3\.?\s*(?:method|approach|methodology)?)\s*[:\n](.+?)(?=\n\s*(?:4\.?|experiment|evaluation|results|discussion))"),
            ("experiments", r"(?i)(?:^|\n)(4\.?\s*(?:experiment|evaluation|experiments)?)\s*[:\n](.+?)(?=\n\s*(?:5\.?|result|discussion|conclusion))"),
            ("results", r"(?i)(?:^|\n)(5\.?\s*(?:result|results|discussion)?)\s*[:\n](.+?)(?=\n\s*(?:6\.?|conclusion|future|limitation))"),
            ("conclusion", r"(?i)(?:^|\n)(6\.?\s*(?:conclusion|conclusions|discussion)?)\s*[:\n](.+?)(?=\n\s*(?:references|bibliography|$))"),
            ("acknowledgments", r"(?i)(?:^|\n)(acknowledgments?)\s*[:\n](.+?)(?=\n\s*(?:references|bibliography|$))"),
        ]

        for section_name, pattern in section_patterns:
            match = re.search(pattern, text, re.DOTALL)
            if match:
                content = match.group(2).strip()
                if len(content) > 10000:
                    content = content[:10000] + "..."
                sections[section_name] = content

        return sections

    def _extract_figures(self, text: str) -> list[dict]:
        """Extract figure references and captions."""
        figures = []
        pattern = r"(?:Figure|Fig\.?)\s*(\d+)[:\.\s]+([^\n]+?)(?=\n\s*(?:Figure|Fig\.?|Table|$))"

        for i, match in enumerate(re.finditer(pattern, text, re.IGNORECASE)):
            caption = match.group(2).strip()[:200]
            figures.append({
                "id": i + 1,
                "number": match.group(1),
                "caption": caption,
            })

        return figures

    def _extract_tables(self, text: str) -> list[dict]:
        """Extract table references and captions."""
        tables = []
        pattern = r"(?:Table|Tab\.?)\s*(\d+)[:\.\s]+([^\n]+?)(?=\n\s*(?:Table|Tab\.?|Figure|$))"

        for i, match in enumerate(re.finditer(pattern, text, re.IGNORECASE)):
            caption = match.group(2).strip()[:200]
            tables.append({
                "id": i + 1,
                "number": match.group(1),
                "caption": caption,
            })

        return tables

    def _extract_equations(self, text: str) -> list[dict]:
        """Extract numbered equations."""
        equations = []
        patterns = [
            r"\((?:eq\.?\s*)?(\d+)\)\s*[:=]\s*(.+?)(?=\n|$)",
            r"(?:Eq\.?|Equation)\s*(\d+)\s*[:=]\s*(.+?)(?=\n|$)",
        ]

        for pattern in patterns:
            for i, match in enumerate(re.finditer(pattern, text)):
                eq_num = match.group(1)
                content = match.group(2).strip()[:100]
                equations.append({
                    "id": i + 1,
                    "number": eq_num,
                    "content": content,
                })

        return equations

    def _extract_references(self, text: str) -> list[dict]:
        """Extract bibliography entries."""
        references = []
        ref_match = re.search(r"(?i)(?:references|bibliography)\s*[:\n](.+)", text, re.DOTALL)
        if not ref_match:
            return references

        ref_text = ref_match.group(1)
        bracket_pattern = r"(\d+)\.\s+(.+?)(?=\n\s*\d+\.|\Z)"

        for match in re.finditer(bracket_pattern, ref_text, re.DOTALL):
            ref_id = match.group(1)
            ref_content = match.group(2).strip()[:500]
            references.append({
                "id": ref_id,
                "text": ref_content,
                "arxiv_id": self._extract_arxiv_id(ref_content),
            })

        return references

    def _extract_arxiv_id(self, text: str) -> Optional[str]:
        """Extract arXiv ID from text."""
        match = re.search(r"arXiv[:\.]?\s*(\d+\.\d+)", text, re.IGNORECASE)
        return match.group(1) if match else None

    def _extract_metadata(self, text: str) -> dict:
        """Extract paper metadata from text."""
        metadata = {}
        lines = text.split("\n")

        for line in lines[:10]:
            if line.strip() and len(line.strip()) > 10:
                if not line.strip().startswith("http"):
                    metadata["first_line"] = line.strip()[:200]
                break

        metadata["approximate_pages"] = len(text) // 3000
        metadata["word_count"] = len(text.split())

        return metadata
