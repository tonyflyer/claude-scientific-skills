# arXiv API Reference

## Overview

This document provides detailed API specifications for the arxiv-database skill.

## ArxivSearcher Class

### Constructor

```python
from arxiv_client import ArxivSearcher

searcher = ArxivSearcher(
    max_results: int = 100,
    delay_seconds: float = 3.0,
    verbose: bool = False
)
```

**Parameters:**
- `max_results` (int): Default maximum results per query
- `delay_seconds` (float): Delay between API requests (respects arXiv rate limits)
- `verbose` (bool): Enable verbose logging

### Methods

#### search()

Search arXiv for papers.

```python
results = searcher.search(
    query: str = "",
    max_results: Optional[int] = None,
    sort_by: str = "relevance",
    sort_order: str = "descending",
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    categories: Optional[list[str]] = None,
    id_list: Optional[list[str]] = None
) -> dict
```

**Parameters:**
- `query` (str): Search query string
- `max_results` (int, optional): Override default max results
- `sort_by` (str): Sort criterion - "relevance", "lastUpdatedDate", or "submittedDate"
- `sort_order` (str): Sort order - "ascending" or "descending"
- `date_from` (str, optional): Start date in YYYY-MM-DD format
- `date_to` (str, optional): End date in YYYY-MM-DD format
- `categories` (list, optional): List of arXiv categories to filter
- `id_list` (list, optional): List of specific arXiv IDs to retrieve

**Returns:**
```json
{
  "query": {
    "query_string": "transformer",
    "categories": ["cs.AI"],
    "date_from": "2024-01-01",
    "date_to": "2024-12-31"
  },
  "result_count": 42,
  "results": [
    {
      "id": "2401.12345",
      "title": "Paper Title",
      "authors": ["Author A", "Author B"],
      "abstract": "...",
      "published": "2024-01-15",
      "updated": "2024-01-20",
      "categories": ["cs.AI", "cs.LG"],
      "pdf_url": "https://arxiv.org/pdf/2401.12345v1.pdf",
      "comment": "12 pages",
      "doi": "10.48550/arXiv.2401.12345"
    }
  ]
}
```

#### search_author()

Search papers by author.

```python
results = searcher.search_author(
    author_name: str,
    max_results: Optional[int] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    categories: Optional[list[str]] = None
) -> dict
```

#### search_category()

Search papers by category.

```python
results = searcher.search_category(
    categories: list[str],
    max_results: Optional[int] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None
) -> dict
```

#### get_paper()

Get details for a specific paper.

```python
paper = searcher.get_paper(paper_id: str) -> Optional[dict]
```

**Parameters:**
- `paper_id` (str): arXiv ID (with or without version)

**Returns:** Paper data dictionary or None

#### download_pdf()

Download PDF for a paper.

```python
success = searcher.download_pdf(
    paper_id: str,
    output_path: str,
    version: Optional[int] = None
) -> bool
```

**Parameters:**
- `paper_id` (str): arXiv ID
- `output_path` (str): Output file path
- `version` (int, optional): Specific version number

**Returns:** True if successful, False otherwise

#### batch_download()

Batch download papers from search results.

```python
summary = searcher.batch_download(
    input_file: str,
    output_dir: str,
    max_papers: int = 50
) -> dict
```

**Returns:**
```json
{
  "successful": 10,
  "failed": 2,
  "papers": [
    {"id": "2401.12345", "status": "success"},
    {"id": "2401.12346", "status": "failed"}
  ]
}
```

#### generate_citation()

Generate citation for a paper.

```python
citation = searcher.generate_citation(
    paper: dict,
    format: str = "bibtex"
) -> str
```

**Parameters:**
- `paper` (dict): Paper data dictionary
- `format` (str): Format - "bibtex", "apa", or "mla"

**Returns:** Formatted citation string

## Rate Limits

arXiv API rate limits:
- Maximum 1 request per 3 seconds
- Maximum 30000 results per query
- Maximum 2000 results per page

The client automatically handles rate limiting with configurable delays.

## Error Handling

The client raises exceptions for:
- Network errors
- Invalid paper IDs
- API errors (non-200 responses)

All errors are logged if `verbose=True`.
