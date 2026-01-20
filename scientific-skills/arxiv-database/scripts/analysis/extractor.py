"""
Paper information extractor for structured analysis.

Extracts metadata, sections, figures, tables, and other
structured information from papers.
"""

import json
import re
from typing import Any


class PaperExtractor:
    """Extract structured information from papers."""

    # Section patterns (common in CS/AI papers)
    SECTION_PATTERNS = {
        "abstract": r"(?i)(?:^|\n)(abstract)\s*[:\n](.+?)(?=\n\s*(?:1\.|introduction|background|related work))",
        "introduction": r"(?i)(?:^|\n)(1\s*\.|introduction)\s*[:\n](.+?)(?=\n\s*(?:2\s*\.|related work|background))",
        "related_work": r"(?i)(?:^|\n)(2\s*\.?|related work|background)\s*[:\n](.+?)(?=\n\s*(?:3\s*\.|method|approach|methodology))",
        "methodology": r"(?i)(?:^|\n)(3\s*\.?|method|approach|methodology|methodology?)\s*[:\n](.+?)(?=\n\s*(?:4\s*\.|experiment|evaluation|results|discussion))",
        "experiments": r"(?i)(?:^|\n)(4\s*\.?|experiment|evaluation|experiments)\s*[:\n](.+?)(?=\n\s*(?:5\s*\.|result|discussion|conclusion))",
        "results": r"(?i)(?:^|\n)(5\s*\.?|result|results|discussion)\s*[:\n](.+?)(?=\n\s*(?:6\s*\.|conclusion|future|limitation))",
        "conclusion": r"(?i)(?:^|\n)(6\s*\.?|conclusion|conclusions|discussion)\s*[:\n](.+?)(?=\n\s*(?:references|bibliography|$))",
    }

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def extract(self, paper_data: dict) -> dict:
        """
        Extract structured information from paper data.

        Args:
            paper_data: Paper metadata dictionary

        Returns:
            Structured paper analysis
        """
        result = {
            "metadata": self._extract_metadata(paper_data),
            "abstract": paper_data.get("abstract", ""),
            "sections": {},
            "figures": [],
            "tables": [],
            "equations": [],
            "references": [],
        }

        # Extract sections from abstract if available
        abstract = paper_data.get("abstract", "")
        result["sections"]["abstract"] = abstract

        return result

    def _extract_metadata(self, paper_data: dict) -> dict:
        """Extract and normalize metadata."""
        return {
            "title": paper_data.get("title", ""),
            "authors": paper_data.get("authors", []),
            "published": paper_data.get("published", ""),
            "updated": paper_data.get("updated", ""),
            "categories": paper_data.get("categories", []),
            "arxiv_id": paper_data.get("id", ""),
            "doi": paper_data.get("doi", ""),
            "pdf_url": paper_data.get("pdf_url", ""),
            "comment": paper_data.get("comment", ""),
            "journal_ref": paper_data.get("journal_ref", ""),
        }

    def extract_from_text(self, text: str) -> dict:
        """
        Extract structured information from paper text.

        Args:
            text: Full paper text

        Returns:
            Structured extraction
        """
        result = {
            "sections": self._extract_sections(text),
            "figures": self._extract_figures(text),
            "tables": self._extract_tables(text),
            "equations": self._extract_equations(text),
            "references": self._extract_references(text),
        }

        return result

    def _extract_sections(self, text: str) -> dict:
        """Extract paper sections."""
        sections = {}

        for section_name, pattern in self.SECTION_PATTERNS.items():
            match = re.search(pattern, text, re.DOTALL)
            if match:
                sections[section_name] = match.group(2).strip()

        return sections

    def _extract_figures(self, text: str) -> list[dict]:
        """Extract figure captions and references."""
        figures = []

        # Pattern: "Figure N:" or "Fig. N:" followed by caption
        pattern = r"(?:Figure|Fig\.?)\s*(\d+)[:\.\s]+(.+?)(?=\n\s*(?:Figure|Fig\.?|Table|$))"

        for i, match in enumerate(re.finditer(pattern, text, re.IGNORECASE)):
            figures.append({
                "id": i + 1,
                "number": match.group(1),
                "caption": match.group(2).strip()[:200],
            })

        return figures

    def _extract_tables(self, text: str) -> list[dict]:
        """Extract table captions and references."""
        tables = []

        # Pattern: "Table N:" followed by caption
        pattern = r"(?:Table|Tab\.?)\s*(\d+)[:\.\s]+(.+?)(?=\n\s*(?:Table|Tab\.?|Figure|$))"

        for i, match in enumerate(re.finditer(pattern, text, re.IGNORECASE)):
            tables.append({
                "id": i + 1,
                "number": match.group(1),
                "caption": match.group(2).strip()[:200],
            })

        return tables

    def _extract_equations(self, text: str) -> list[dict]:
        """Extract equations (numbered)."""
        equations = []

        # Pattern: "(N)" or "Eq. N" followed by equation
        pattern = r"(?:\((?:eq\.?\s*)?(\d+)\)|Eq\.?\s*(\d+))\s*[:=]\s*(.+?)(?=\n|$)"

        for i, match in enumerate(re.finditer(pattern, text)):
            eq_num = match.group(1) or match.group(2)
            equations.append({
                "id": i + 1,
                "number": eq_num,
                "content": match.group(3).strip()[:100],
            })

        return equations

    def _extract_references(self, text: str) -> list[dict]:
        """Extract bibliography entries."""
        references = []

        # Find references section
        ref_match = re.search(r"(?i)(?:references|bibliography)\s*[:\n](.+)", text, re.DOTALL)
        if not ref_match:
            return references

        ref_text = ref_match.group(1)

        # Pattern: "[N] Title. Authors. Venue. Year"
        pattern = r"\[(\d+)\]\s*(.+?)(?=\n\s*\[|\n\s*\d+\.|\Z)"

        for match in re.finditer(pattern, ref_text, re.DOTALL):
            ref_text = match.group(2).strip()
            references.append({
                "id": match.group(1),
                "text": ref_text[:500],
                "arxiv_id": self._extract_arxiv_id(ref_text),
            })

        return references

    def _extract_arxiv_id(self, text: str) -> str | None:
        """Extract arXiv ID from reference text."""
        match = re.search(r"arXiv[:\.]?\s*(\d+\.\d+)", text, re.IGNORECASE)
        return match.group(1) if match else None
