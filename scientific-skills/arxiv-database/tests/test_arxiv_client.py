"""
Tests for arxiv_client module.

Tests core arXiv search and retrieval functionality.
"""

import json
import pytest
import sys
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Add scripts to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from arxiv_client import ArxivSearcher


class TestArxivSearcherInitialization:
    """Tests for ArxivSearcher initialization."""

    def test_create_with_defaults(self):
        """Test creating searcher with default parameters."""
        searcher = ArxivSearcher()
        assert searcher.max_results == 100
        assert searcher.delay_seconds == 3.0
        assert searcher.verbose is False

    def test_create_with_custom_params(self):
        """Test creating searcher with custom parameters."""
        searcher = ArxivSearcher(
            max_results=50,
            delay_seconds=5.0,
            verbose=True
        )
        assert searcher.max_results == 50
        assert searcher.delay_seconds == 5.0
        assert searcher.verbose is True

    def test_client_initialization(self):
        """Test that arxiv client is initialized."""
        searcher = ArxivSearcher(max_results=200)
        assert searcher.client is not None


class TestQueryBuilding:
    """Tests for query construction."""

    def test_build_query_basic(self):
        """Test building basic query."""
        searcher = ArxivSearcher()
        query = searcher._build_query("machine learning")
        assert "machine learning" in query

    def test_build_query_with_categories(self):
        """Test building query with categories."""
        searcher = ArxivSearcher()
        query = searcher._build_query(
            "transformers",
            categories=["cs.AI", "cs.LG"]
        )
        assert "transformers" in query
        assert "cat:cs.AI" in query or "cs.AI" in query
        assert "cat:cs.LG" in query or "cs.LG" in query

    def test_build_query_with_dates(self):
        """Test building query with date range."""
        searcher = ArxivSearcher()
        query = searcher._build_query(
            "neural networks",
            date_from="2024-01-01",
            date_to="2024-12-31"
        )
        assert "neural networks" in query
        assert "submittedDate" in query or "2024" in query

    def test_build_query_empty(self):
        """Test building query with no parameters."""
        searcher = ArxivSearcher()
        query = searcher._build_query("")
        assert query == "all:"

    def test_escape_query_special_chars(self):
        """Test escaping special characters in query."""
        searcher = ArxivSearcher()
        escaped = searcher._escape_query("test+query-with&special|chars")
        assert "\\" in escaped or escaped == "test+query-with&special|chars"


class TestSearchFunctionality:
    """Tests for search methods."""

    @pytest.mark.integration
    def test_search_basic_real(self):
        """Test basic search with real arXiv API (integration test)."""
        searcher = ArxivSearcher(max_results=2, verbose=False)
        results = searcher.search(query="ti:attention mechanism")

        assert "results" in results
        assert "result_count" in results
        assert isinstance(results["results"], list)

    def test_search_returns_correct_structure(self):
        """Test that search returns expected structure."""
        searcher = ArxivSearcher(max_results=1)
        with patch.object(searcher.client, 'results') as mock_results:
            # Mock a result
            mock_result = MagicMock()
            mock_result.get_short_id.return_value = "2401.12345"
            mock_result.title = "Test Paper"
            mock_result.authors = [MagicMock(name="Author One")]
            mock_result.summary = "Test abstract"
            mock_result.published = None
            mock_result.updated = None
            mock_result.categories = ["cs.AI"]
            mock_result.primary_category = "cs.AI"
            mock_result.pdf_url = "https://arxiv.org/pdf/2401.12345.pdf"
            mock_result.comment = "Test comment"
            mock_result.journal_ref = None
            mock_result.doi = None

            mock_results.return_value = [mock_result]

            results = searcher.search(query="test")

            assert "query" in results
            assert "result_count" in results
            assert "results" in results
            assert results["result_count"] == 1
            assert results["results"][0]["id"] == "2401.12345"
            assert results["results"][0]["title"] == "Test Paper"

    def test_search_author(self):
        """Test author search method."""
        searcher = ArxivSearcher(max_results=1)
        with patch.object(searcher, 'search') as mock_search:
            mock_search.return_value = {"results": [], "result_count": 0}

            searcher.search_author("Hinton")

            # Verify search was called with author query
            mock_search.assert_called_once()
            call_args = mock_search.call_args
            assert "au:" in call_args[1]["query"]

    def test_search_category(self):
        """Test category search method."""
        searcher = ArxivSearcher(max_results=1)
        with patch.object(searcher, 'search') as mock_search:
            mock_search.return_value = {"results": [], "result_count": 0}

            searcher.search_category(["cs.AI", "cs.LG"])

            # Verify search was called with categories
            mock_search.assert_called_once()
            call_args = mock_search.call_args
            assert call_args[1]["categories"] == ["cs.AI", "cs.LG"]


class TestPaperRetrieval:
    """Tests for retrieving specific papers."""

    def test_get_paper_by_id(self):
        """Test getting a specific paper by ID."""
        searcher = ArxivSearcher()
        with patch.object(searcher, 'search') as mock_search:
            mock_search.return_value = {
                "results": [{"id": "2401.12345", "title": "Test"}],
                "result_count": 1
            }

            paper = searcher.get_paper("2401.12345")

            assert paper is not None
            assert paper["id"] == "2401.12345"

    def test_get_paper_not_found(self):
        """Test getting a paper that doesn't exist."""
        searcher = ArxivSearcher()
        with patch.object(searcher, 'search') as mock_search:
            mock_search.return_value = {"results": [], "result_count": 0}

            paper = searcher.get_paper("9999.99999")

            assert paper is None

    def test_get_paper_cleans_id(self):
        """Test that paper ID is cleaned (removes arxiv: prefix)."""
        searcher = ArxivSearcher()
        with patch.object(searcher, 'search') as mock_search:
            mock_search.return_value = {"results": [], "result_count": 0}

            searcher.get_paper("arxiv:2401.12345")

            # Verify ID was cleaned
            mock_search.assert_called_once()
            call_args = mock_search.call_args
            assert "arxiv:" not in str(call_args)


class TestCitationGeneration:
    """Tests for citation generation."""

    def test_generate_bibtex_citation(self):
        """Test generating BibTeX citation."""
        searcher = ArxivSearcher()
        paper = {
            "id": "2401.12345",
            "title": "Test Paper Title",
            "authors": ["John Smith", "Jane Doe"],
            "published": "2024-01-15"
        }

        citation = searcher.generate_citation(paper, format="bibtex")

        assert "@article" in citation
        assert "Test Paper Title" in citation
        assert "John Smith" in citation
        assert "2024" in citation
        assert "2401.12345" in citation

    def test_generate_apa_citation(self):
        """Test generating APA citation."""
        searcher = ArxivSearcher()
        paper = {
            "id": "2401.12345",
            "title": "Test Paper",
            "authors": ["Smith"],
            "published": "2024-01-01"
        }

        citation = searcher.generate_citation(paper, format="apa")

        assert "Smith" in citation
        assert "2024" in citation
        assert "Test Paper" in citation

    def test_generate_mla_citation(self):
        """Test generating MLA citation."""
        searcher = ArxivSearcher()
        paper = {
            "id": "2401.12345",
            "title": "Test Paper",
            "authors": ["Smith"],
            "published": "2024-01-01"
        }

        citation = searcher.generate_citation(paper, format="mla")

        assert "Smith" in citation
        assert "Test Paper" in citation
        assert "2024" in citation

    def test_generate_citation_handles_missing_data(self):
        """Test citation generation handles missing data gracefully."""
        searcher = ArxivSearcher()
        paper = {
            "id": "2401.12345",
            "title": "Test",
            "authors": [],
            "published": ""
        }

        citation = searcher.generate_citation(paper, format="bibtex")

        # Should not crash, should use defaults
        assert citation is not None
        assert len(citation) > 0


class TestResultFormatting:
    """Tests for result formatting."""

    def test_format_result(self):
        """Test formatting arXiv result to dictionary."""
        searcher = ArxivSearcher()

        # Create mock result
        mock_author = MagicMock()
        mock_author.name = "Author"

        mock_result = MagicMock()
        mock_result.get_short_id.return_value = "2401.12345"
        mock_result.title = "Test Title"
        mock_result.authors = [mock_author]
        mock_result.summary = "Abstract"
        mock_result.published = None
        mock_result.updated = None
        mock_result.categories = ["cs.AI"]
        mock_result.primary_category = "cs.AI"
        mock_result.pdf_url = "https://arxiv.org/pdf/2401.12345.pdf"
        mock_result.comment = None
        mock_result.journal_ref = None
        mock_result.doi = None

        formatted = searcher._format_result(mock_result)

        assert formatted["id"] == "2401.12345"
        assert formatted["title"] == "Test Title"
        assert formatted["authors"] == ["Author"]
        assert formatted["abstract"] == "Abstract"
        assert formatted["categories"] == ["cs.AI"]


class TestErrorHandling:
    """Tests for error handling."""

    def test_search_handles_exception_gracefully(self):
        """Test that search handles exceptions without crashing."""
        searcher = ArxivSearcher(verbose=False)
        with patch.object(searcher.client, 'results') as mock_results:
            mock_results.side_effect = Exception("API Error")

            results = searcher.search(query="test")

            # Should return empty results, not crash
            assert "results" in results
            assert results["result_count"] == 0

    def test_download_pdf_handles_failure(self):
        """Test that PDF download handles failures gracefully."""
        searcher = ArxivSearcher(verbose=False)

        success = searcher.download_pdf("invalid_id", "/tmp/test.pdf")

        # Should return False, not crash
        assert success is False


class TestBatchOperations:
    """Tests for batch operations."""

    def test_batch_download_structure(self):
        """Test batch download returns proper structure."""
        searcher = ArxivSearcher()

        # Create mock input file
        mock_data = {
            "results": [
                {"id": "2401.12345"},
                {"id": "2401.67890"}
            ]
        }

        with patch('builtins.open', create=True) as mock_open:
            with patch('json.load', return_value=mock_data):
                with patch.object(searcher, 'download_pdf', return_value=True):
                    with patch('os.makedirs'):
                        summary = searcher.batch_download(
                            "test.json",
                            "/tmp/output",
                            max_papers=2
                        )

        assert "successful" in summary
        assert "failed" in summary
        assert "papers" in summary


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
