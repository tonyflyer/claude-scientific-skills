"""
Tests for review.data_models module.

Tests all data models used in paper parsing and review workflow.
"""

import pytest
import sys
from pathlib import Path

# Add scripts to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from review.data_models import (
    PaperFigure,
    PaperMetadata,
    PaperReference,
    PaperSection,
    PaperTable,
    StructuredPaperData,
)


class TestPaperSection:
    """Tests for PaperSection dataclass."""

    def test_create_basic_section(self):
        """Test creating a basic paper section."""
        section = PaperSection(
            title="Introduction",
            content="This is the introduction."
        )
        assert section.title == "Introduction"
        assert section.content == "This is the introduction."
        assert section.level == 1  # Default value

    def test_create_section_with_level(self):
        """Test creating a section with specific level."""
        section = PaperSection(
            title="Methods",
            content="Description of methods.",
            level=2
        )
        assert section.level == 2

    def test_section_content_can_be_long(self):
        """Test that sections can hold long content."""
        long_content = "A" * 10000
        section = PaperSection(
            title="Results",
            content=long_content
        )
        assert len(section.content) == 10000


class TestPaperReference:
    """Tests for PaperReference dataclass."""

    def test_create_basic_reference(self):
        """Test creating a basic reference."""
        ref = PaperReference(
            id="1",
            text="Author et al. Title. Journal, 2024."
        )
        assert ref.id == "1"
        assert ref.text == "Author et al. Title. Journal, 2024."
        assert ref.arxiv_id is None
        assert ref.doi is None

    def test_create_reference_with_arxiv(self):
        """Test creating reference with arXiv ID."""
        ref = PaperReference(
            id="2",
            text="Paper with arXiv",
            arxiv_id="2401.12345"
        )
        assert ref.arxiv_id == "2401.12345"

    def test_create_reference_with_doi(self):
        """Test creating reference with DOI."""
        ref = PaperReference(
            id="3",
            text="Paper with DOI",
            doi="10.1234/example"
        )
        assert ref.doi == "10.1234/example"


class TestPaperFigure:
    """Tests for PaperFigure dataclass."""

    def test_create_basic_figure(self):
        """Test creating a basic figure."""
        fig = PaperFigure(
            number="1",
            caption="Example figure showing results."
        )
        assert fig.number == "1"
        assert fig.caption == "Example figure showing results."
        assert fig.page_estimate is None

    def test_create_figure_with_page(self):
        """Test creating figure with page estimate."""
        fig = PaperFigure(
            number="2",
            caption="Another figure",
            page_estimate=5
        )
        assert fig.page_estimate == 5


class TestPaperTable:
    """Tests for PaperTable dataclass."""

    def test_create_basic_table(self):
        """Test creating a basic table."""
        table = PaperTable(
            number="1",
            caption="Results summary table."
        )
        assert table.number == "1"
        assert table.caption == "Results summary table."

    def test_table_caption_can_be_long(self):
        """Test that table captions can be detailed."""
        long_caption = "Detailed description " * 20
        table = PaperTable(
            number="2",
            caption=long_caption
        )
        assert len(table.caption) > 100


class TestPaperMetadata:
    """Tests for PaperMetadata dataclass."""

    def test_create_minimal_metadata(self):
        """Test creating metadata with only title."""
        metadata = PaperMetadata(title="Test Paper")
        assert metadata.title == "Test Paper"
        assert metadata.authors == []
        assert metadata.abstract == ""
        assert metadata.categories == []
        assert metadata.source_type == "unknown"

    def test_create_full_metadata(self):
        """Test creating metadata with all fields."""
        metadata = PaperMetadata(
            title="Complete Paper",
            authors=["Author One", "Author Two"],
            abstract="This is the abstract.",
            categories=["cs.AI", "cs.LG"],
            arxiv_id="2401.12345",
            doi="10.1234/example",
            pdf_url="https://arxiv.org/pdf/2401.12345.pdf",
            published="2024-01-15",
            updated="2024-01-20",
            comment="12 pages, 3 figures",
            journal_ref="Journal Name, 2024",
            source_type="arxiv"
        )

        assert metadata.title == "Complete Paper"
        assert len(metadata.authors) == 2
        assert metadata.abstract == "This is the abstract."
        assert len(metadata.categories) == 2
        assert metadata.arxiv_id == "2401.12345"
        assert metadata.doi == "10.1234/example"
        assert metadata.source_type == "arxiv"

    def test_metadata_default_factory(self):
        """Test that default factories work correctly."""
        meta1 = PaperMetadata(title="Paper 1")
        meta2 = PaperMetadata(title="Paper 2")

        meta1.authors.append("Author 1")

        # Ensure default factories create separate lists
        assert len(meta1.authors) == 1
        assert len(meta2.authors) == 0


class TestStructuredPaperData:
    """Tests for StructuredPaperData dataclass."""

    def test_create_minimal_paper_data(self):
        """Test creating minimal structured paper data."""
        metadata = PaperMetadata(title="Test")
        paper_data = StructuredPaperData(metadata=metadata)

        assert paper_data.metadata.title == "Test"
        assert paper_data.sections == {}
        assert paper_data.figures == []
        assert paper_data.tables == []
        assert paper_data.references == []

    def test_create_full_paper_data(self):
        """Test creating complete structured paper data."""
        metadata = PaperMetadata(
            title="Complete Paper",
            authors=["Author"],
            abstract="Abstract text"
        )

        sections = {
            "Introduction": PaperSection("Introduction", "Intro text"),
            "Methods": PaperSection("Methods", "Methods text")
        }

        figures = [
            PaperFigure("1", "Figure 1 caption"),
            PaperFigure("2", "Figure 2 caption")
        ]

        tables = [
            PaperTable("1", "Table 1 caption")
        ]

        references = [
            PaperReference("1", "Reference 1 text"),
            PaperReference("2", "Reference 2 text", arxiv_id="2401.12345")
        ]

        paper_data = StructuredPaperData(
            metadata=metadata,
            sections=sections,
            figures=figures,
            tables=tables,
            references=references
        )

        assert len(paper_data.sections) == 2
        assert len(paper_data.figures) == 2
        assert len(paper_data.tables) == 1
        assert len(paper_data.references) == 2
        assert paper_data.references[1].arxiv_id == "2401.12345"

    def test_paper_data_default_factory(self):
        """Test that default factories create independent instances."""
        metadata1 = PaperMetadata(title="Paper 1")
        metadata2 = PaperMetadata(title="Paper 2")

        paper1 = StructuredPaperData(metadata=metadata1)
        paper2 = StructuredPaperData(metadata=metadata2)

        paper1.sections["Test"] = PaperSection("Test", "Content")

        # Ensure default factories create separate dicts/lists
        assert len(paper1.sections) == 1
        assert len(paper2.sections) == 0


class TestDataModelIntegration:
    """Integration tests for data models working together."""

    def test_build_complete_paper_structure(self):
        """Test building a complete paper structure."""
        # Create metadata
        metadata = PaperMetadata(
            title="Example Scientific Paper",
            authors=["Alice Smith", "Bob Jones"],
            abstract="This paper presents novel findings.",
            categories=["cs.AI"],
            arxiv_id="2401.12345",
            source_type="arxiv"
        )

        # Create sections
        sections = {
            "Abstract": PaperSection(
                title="Abstract",
                content=metadata.abstract
            ),
            "Introduction": PaperSection(
                title="Introduction",
                content="Background and motivation for the work.",
                level=1
            ),
            "Methods": PaperSection(
                title="Methods",
                content="Description of experimental methodology.",
                level=1
            ),
            "Results": PaperSection(
                title="Results",
                content="Presentation of findings.",
                level=1
            ),
            "Conclusion": PaperSection(
                title="Conclusion",
                content="Summary and future work.",
                level=1
            )
        }

        # Create figures
        figures = [
            PaperFigure("1", "Overview of the proposed system"),
            PaperFigure("2", "Experimental results comparison"),
            PaperFigure("3", "Qualitative examples")
        ]

        # Create tables
        tables = [
            PaperTable("1", "Quantitative results on benchmark datasets"),
            PaperTable("2", "Ablation study results")
        ]

        # Create references
        references = [
            PaperReference(
                "1",
                "Smith et al. Previous work. Conference, 2023.",
                arxiv_id="2301.00001"
            ),
            PaperReference(
                "2",
                "Jones et al. Related research. Journal, 2024.",
                doi="10.1234/example"
            )
        ]

        # Build complete paper
        paper = StructuredPaperData(
            metadata=metadata,
            sections=sections,
            figures=figures,
            tables=tables,
            references=references
        )

        # Verify structure
        assert paper.metadata.title == "Example Scientific Paper"
        assert len(paper.metadata.authors) == 2
        assert len(paper.sections) == 5
        assert "Introduction" in paper.sections
        assert len(paper.figures) == 3
        assert len(paper.tables) == 2
        assert len(paper.references) == 2

        # Verify content
        assert paper.sections["Introduction"].level == 1
        assert paper.figures[0].number == "1"
        assert paper.references[0].arxiv_id == "2301.00001"
        assert paper.references[1].doi == "10.1234/example"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
