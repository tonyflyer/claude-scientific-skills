"""
Review module for paper analysis and evaluation.

This module provides components for parsing papers, searching literature,
and generating review templates.
"""

from .data_models import (
    PaperFigure,
    PaperMetadata,
    PaperReference,
    PaperSection,
    PaperTable,
    StructuredPaperData,
)
from .parsers import DocxParser, LatexParser, PaperParser, PdfParser

__all__ = [
    # Data models
    "PaperSection",
    "PaperReference",
    "PaperFigure",
    "PaperTable",
    "PaperMetadata",
    "StructuredPaperData",
    # Parsers
    "PaperParser",
    "DocxParser",
    "PdfParser",
    "LatexParser",
]
