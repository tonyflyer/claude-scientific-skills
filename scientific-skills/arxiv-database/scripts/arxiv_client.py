"""
ArXiv API Client for Claude Scientific Skills.

Provides efficient search and retrieval of arXiv preprints
with structured JSON output.
"""

import json
import re
import time
from datetime import datetime
from typing import Any, Generator, Optional

import arxiv
from pydantic import BaseModel, Field


class ArxivSearcher:
    """Client for searching and retrieving arXiv papers."""

    def __init__(
        self,
        max_results: int = 100,
        delay_seconds: float = 3.0,
        verbose: bool = False,
    ):
        """
        Initialize the arXiv search client.

        Args:
            max_results: Default maximum results per query
            delay_seconds: Delay between API requests
            verbose: Enable verbose logging
        """
        self.max_results = max_results
        self.delay_seconds = delay_seconds
        self.verbose = verbose

        # Create arXiv client with appropriate settings
        self.client = arxiv.Client(
            page_size=min(max_results, 200),
            delay_seconds=delay_seconds,
            num_retries=3,
        )

    def search(
        self,
        query: str = "",
        max_results: Optional[int] = None,
        sort_by: str = "relevance",
        sort_order: str = "descending",
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        categories: Optional[list[str]] = None,
        id_list: Optional[list[str]] = None,
    ) -> dict:
        """
        Search arXiv for papers.

        Args:
            query: Search query string (supports arXiv query syntax)
            max_results: Maximum number of results
            sort_by: Sort criterion (relevance, lastUpdatedDate, submittedDate)
            sort_order: Sort order (ascending, descending)
            date_from: Start date (YYYY-MM-DD)
            date_to: End date (YYYY-MM-DD)
            categories: List of arXiv categories
            id_list: List of arXiv IDs to retrieve

        Returns:
            Dictionary with search results
        """
        max_results = max_results or self.max_results

        # Build search query
        search_query = self._build_query(query, categories, date_from, date_to)

        # Map sort parameters
        sort_map = {
            "relevance": arxiv.SortCriterion.Relevance,
            "lastUpdatedDate": arxiv.SortCriterion.LastUpdatedDate,
            "submittedDate": arxiv.SortCriterion.SubmittedDate,
        }
        order_map = {
            "ascending": arxiv.SortOrder.Ascending,
            "descending": arxiv.SortOrder.Descending,
        }

        # Create search object
        if id_list:
            search = arxiv.Search(
                id_list=id_list,
                max_results=max_results,
            )
        else:
            search = arxiv.Search(
                query=search_query,
                max_results=max_results,
                sort_by=sort_map.get(sort_by, arxiv.SortCriterion.Relevance),
                sort_order=order_map.get(sort_order, arxiv.SortOrder.Descending),
            )

        # Execute search
        results = []
        try:
            for result in self.client.results(search):
                paper_data = self._format_result(result)
                results.append(paper_data)
                if len(results) >= max_results:
                    break
        except Exception as e:
            if self.verbose:
                print(f"Search error: {e}")

        return {
            "query": {
                "query_string": query,
                "categories": categories,
                "date_from": date_from,
                "date_to": date_to,
            },
            "result_count": len(results),
            "results": results,
        }

    def search_author(
        self,
        author_name: str,
        max_results: Optional[int] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        categories: Optional[list[str]] = None,
    ) -> dict:
        """
        Search papers by author.

        Args:
            author_name: Name of the author
            max_results: Maximum number of results
            date_from: Start date
            date_to: End date
            categories: Filter by categories

        Returns:
            Dictionary with search results
        """
        query = f"au:{self._escape_query(author_name)}"
        return self.search(
            query=query,
            max_results=max_results,
            date_from=date_from,
            date_to=date_to,
            categories=categories,
        )

    def search_category(
        self,
        categories: list[str],
        max_results: Optional[int] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
    ) -> dict:
        """
        Search papers by category.

        Args:
            categories: List of arXiv categories (e.g., ['cs.AI', 'cs.LG'])
            max_results: Maximum number of results
            date_from: Start date
            date_to: End date

        Returns:
            Dictionary with search results
        """
        return self.search(
            query="",
            categories=categories,
            max_results=max_results,
            date_from=date_from,
            date_to=date_to,
        )

    def get_paper(self, paper_id: str) -> Optional[dict]:
        """
        Get details for a specific paper.

        Args:
            paper_id: arXiv ID (with or without version)

        Returns:
            Paper data dictionary or None
        """
        # Clean the paper ID
        clean_id = paper_id.replace("arxiv:", "").strip()

        results = self.search(id_list=[clean_id], max_results=1)
        if results["results"]:
            return results["results"][0]
        return None

    def download_pdf(
        self,
        paper_id: str,
        output_path: str,
        version: Optional[int] = None,
    ) -> bool:
        """
        Download PDF for a paper.

        Args:
            paper_id: arXiv ID
            output_path: Output file path
            version: Specific version number (defaults to latest)

        Returns:
            True if successful, False otherwise
        """
        try:
            search = arxiv.Search(id_list=[paper_id.replace("arxiv:", "")])
            result = next(self.client.results(search))

            # Determine version
            if version:
                pdf_url = f"https://arxiv.org/pdf/{paper_id}v{version}.pdf"
            else:
                pdf_url = result.pdf_url

            # Download using requests
            import requests

            response = requests.get(pdf_url, stream=True)
            response.raise_for_status()

            with open(output_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            return True

        except Exception as e:
            if self.verbose:
                print(f"Download error: {e}")
            return False

    def batch_download(
        self,
        input_file: str,
        output_dir: str,
        max_papers: int = 50,
    ) -> dict:
        """
        Batch download papers from a search results file.

        Args:
            input_file: JSON file with search results
            output_dir: Output directory for PDFs
            max_papers: Maximum papers to download

        Returns:
            Download summary
        """
        with open(input_file, "r") as f:
            data = json.load(f)

        results = data.get("results", [])
        summary = {"successful": 0, "failed": 0, "papers": []}

        import os

        os.makedirs(output_dir, exist_ok=True)

        for i, paper in enumerate(results[:max_papers]):
            paper_id = paper["id"]
            output_path = os.path.join(output_dir, f"{paper_id}.pdf")

            if self.download_pdf(paper_id, output_path):
                summary["successful"] += 1
                summary["papers"].append({"id": paper_id, "status": "success"})
            else:
                summary["failed"] += 1
                summary["papers"].append({"id": paper_id, "status": "failed"})

            # Respect rate limits
            time.sleep(self.delay_seconds)

        return summary

    def generate_citation(
        self,
        paper: dict,
        format: str = "bibtex",
    ) -> str:
        """
        Generate citation for a paper.

        Args:
            paper: Paper data dictionary
            format: Citation format (bibtex, apa, mla)

        Returns:
            Formatted citation string
        """
        authors = paper.get("authors", [])
        first_author = authors[0] if authors else "Unknown"

        # Extract year from date
        date_str = paper.get("published", "")
        year = date_str[:4] if date_str else "2024"

        if format == "bibtex":
            citation = f"""@article{{{first_author.split()[-1]}{year},
  title = {{{paper.get("title", "")}}},
  author = {{{", ".join(authors)}}},
  journal = {{arXiv preprint}},
  year = {{{year}}},
  eprint = {{{paper.get("id", "")}}},
  url = {{https://arxiv.org/abs/{paper.get("id", "")}}}
}}"""
        elif format == "apa":
            citation = f"""{first_author} ({year}). {paper.get("title", "")}. arXiv. https://arxiv.org/abs/{paper.get("id", "")}"""
        elif format == "mla":
            citation = f"""{first_author}. "{paper.get("title", "")}." arXiv, {year}."""
        else:
            citation = str(paper)

        return citation

    def _build_query(
        self,
        query: str,
        categories: Optional[list[str]] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
    ) -> str:
        """Build arXiv query string."""
        parts = []

        if query:
            parts.append(query)

        if categories:
            cat_parts = [f"cat:{cat}" for cat in categories]
            parts.append(" OR ".join(cat_parts))

        if date_from:
            parts.append(f"submittedDate:[{date_from} TO {date_to or '3000-12-31'}]")

        return " AND ".join(parts) if parts else "all:"

    def _escape_query(self, query: str) -> str:
        """Escape special characters in query."""
        return re.sub(r'([+\-&|(){}[\]^"~*?:\\])', r'\\\1', query)

    def _format_result(self, result: arxiv.Result) -> dict:
        """Format arXiv result to dictionary."""
        return {
            "id": result.get_short_id(),
            "title": result.title,
            "authors": [a.name for a in result.authors],
            "abstract": result.summary,
            "published": result.published.isoformat() if result.published else None,
            "updated": result.updated.isoformat() if result.updated else None,
            "categories": result.categories,
            "primary_category": result.primary_category,
            "pdf_url": result.pdf_url,
            "comment": result.comment,
            "journal_ref": result.journal_ref,
            "doi": result.doi,
        }
