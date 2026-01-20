"""
Tests for arxiv-database skill.
"""

import json
import pytest
from unittest.mock import Mock, patch

# Test fixtures
@pytest.fixture
def mock_paper_data():
    """Sample paper data for testing."""
    return {
        "id": "2401.12345",
        "title": "Test Paper on Transformers",
        "authors": ["Author A", "Author B", "Author C"],
        "abstract": "This is a test abstract for the paper.",
        "published": "2024-01-15",
        "updated": "2024-01-20",
        "categories": ["cs.LG", "cs.AI"],
        "pdf_url": "https://arxiv.org/pdf/2401.12345v1.pdf",
        "comment": "12 pages, 3 figures",
        "doi": "10.48550/arXiv.2401.12345",
    }


class TestPaperExtractor:
    """Tests for PaperExtractor class."""

    def test_extract_metadata(self, mock_paper_data):
        """Test metadata extraction."""
        from scripts.analysis.extractor import PaperExtractor

        extractor = PaperExtractor()
        result = extractor.extract(mock_paper_data)

        assert "metadata" in result
        assert result["metadata"]["title"] == "Test Paper on Transformers"
        assert result["metadata"]["arxiv_id"] == "2401.12345"
        assert len(result["metadata"]["authors"]) == 3

    def test_extract_sections(self):
        """Test section extraction from text."""
        from scripts.analysis.extractor import PaperExtractor

        extractor = PaperExtractor()
        text = """
        1. Introduction
        This is the introduction section.

        2. Related Work
        This is related work.

        3. Methodology
        This is the methodology.
        """

        result = extractor.extract_from_text(text)
        assert "sections" in result


class TestPaperEvaluator:
    """Tests for PaperEvaluator class."""

    def test_evaluate_novelty(self, mock_paper_data):
        """Test novelty assessment."""
        from scripts.analysis.evaluator import PaperEvaluator

        evaluator = PaperEvaluator()
        result = evaluator.evaluate(mock_paper_data)

        assert "innovation_score" in result
        assert "novelty_level" in result
        assert 0 <= result["innovation_score"] <= 1

    def test_evaluate_methodology(self, mock_paper_data):
        """Test methodology assessment."""
        from scripts.analysis.evaluator import PaperEvaluator

        evaluator = PaperEvaluator()
        result = evaluator.evaluate(mock_paper_data)

        assert "methodology_score" in result
        assert "methodology_strengths" in result
        assert "methodology_weaknesses" in result

    def test_compare_papers(self, mock_paper_data):
        """Test paper comparison."""
        from scripts.analysis.evaluator import PaperEvaluator

        evaluator = PaperEvaluator()
        papers = [mock_paper_data, {**mock_paper_data, "id": "2401.12346"}]

        # Evaluate all papers
        evaluations = []
        for paper in papers:
            eval_result = evaluator.evaluate(paper)
            eval_result["arxiv_id"] = paper["id"]
            evaluations.append(eval_result)

        comparison = evaluator.compare_papers(evaluations)
        assert "ranking" in comparison
        assert "summary" in comparison


class TestPaperReviewer:
    """Tests for PaperReviewer class."""

    def test_generate_review(self, mock_paper_data):
        """Test review generation."""
        from scripts.analysis.reviewer import PaperReviewer

        reviewer = PaperReviewer()
        review = reviewer.generate_review(
            paper_id="2401.12345",
            paper_data=mock_paper_data,
        )

        assert review["paper_id"] == "2401.12345"
        assert "overall_assessment" in review
        assert "peer_review" in review
        assert "revision_suggestions" in review

    def test_review_score_range(self, mock_paper_data):
        """Test that review scores are in valid range."""
        from scripts.analysis.reviewer import PaperReviewer

        reviewer = PaperReviewer()
        review = reviewer.generate_review(
            paper_id="2401.12345",
            paper_data=mock_paper_data,
        )

        score = review["overall_assessment"]["score"]
        assert 1 <= score <= 5


class TestSearchFunctionality:
    """Tests for search functionality (mocked)."""

    @patch("scripts.arxiv_client.arxiv")
    def test_search_query_construction(self, mock_arxiv):
        """Test query building logic."""
        from scripts.arxiv_client import ArxivSearcher

        # Mock arxiv client
        mock_result = Mock()
        mock_result.get_short_id.return_value = "2401.12345"
        mock_result.title = "Test Paper"
        mock_result.authors = [Mock(name="Author A")]
        mock_result.summary = "Abstract"
        mock_result.published = Mock()
        mock_result.published.isoformat.return_value = "2024-01-15"
        mock_result.updated = Mock()
        mock_result.updated.isoformat.return_value = "2024-01-20"
        mock_result.categories = ["cs.LG"]
        mock_result.primary_category = "cs.LG"
        mock_result.pdf_url = "https://arxiv.org/pdf/2401.12345.pdf"
        mock_result.comment = None
        mock_result.journal_ref = None
        mock_result.doi = None

        mock_search = Mock()
        mock_search.results = [mock_result]

        with patch.object(
            Mock(), "results", return_value=iter([mock_result])
        ):
            searcher = ArxivSearcher()
            # Basic test that searcher initializes
            assert searcher.max_results == 100
            assert searcher.delay_seconds == 3.0


class TestCitationGeneration:
    """Tests for citation generation."""

    def test_bibtex_format(self, mock_paper_data):
        """Test BibTeX citation generation."""
        from scripts.arxiv_client import ArxivSearcher

        searcher = ArxivSearcher()
        citation = searcher.generate_citation(mock_paper_data, format="bibtex")

        assert "@article{" in citation
        assert "Test Paper on Transformers" in citation
        assert "2401.12345" in citation

    def test_apa_format(self, mock_paper_data):
        """Test APA citation generation."""
        from scripts.arxiv_client import ArxivSearcher

        searcher = ArxivSearcher()
        citation = searcher.generate_citation(mock_paper_data, format="apa")

        assert "Author A" in citation
        assert "2024" in citation


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
