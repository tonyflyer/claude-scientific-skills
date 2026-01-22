"""
Data models for paper review workflow.

Contains dataclasses for representing paper structure, metadata,
sections, figures, tables, and references.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class PaperSection:
    """Represents a section of a paper."""
    title: str
    content: str
    level: int = 1


@dataclass
class PaperReference:
    """Represents a reference from a paper."""
    id: str
    text: str
    arxiv_id: Optional[str] = None
    doi: Optional[str] = None


@dataclass
class PaperFigure:
    """Represents a figure in a paper."""
    number: str
    caption: str
    page_estimate: Optional[int] = None


@dataclass
class PaperTable:
    """Represents a table in a paper."""
    number: str
    caption: str
    page_estimate: Optional[int] = None


@dataclass
class PaperMetadata:
    """Complete metadata for a paper."""
    title: str
    authors: list[str] = field(default_factory=list)
    abstract: str = ""
    categories: list[str] = field(default_factory=list)
    arxiv_id: Optional[str] = None
    doi: Optional[str] = None
    pdf_url: Optional[str] = None
    published: Optional[str] = None
    updated: Optional[str] = None
    comment: Optional[str] = None
    journal_ref: Optional[str] = None
    source_type: str = "unknown"


@dataclass
class StructuredPaperData:
    """Complete structured paper data."""
    metadata: PaperMetadata
    sections: dict[str, PaperSection] = field(default_factory=dict)
    figures: list[PaperFigure] = field(default_factory=list)
    tables: list[PaperTable] = field(default_factory=list)
    references: list[PaperReference] = field(default_factory=list)
