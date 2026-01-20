#!/usr/bin/env python3
"""
Quick Literature Review Template.

Generates a quick overview of papers in a research area.

Usage:
    python scripts/templates/literature_review.py \
        --query "transformer attention" \
        --years 2023-2025 \
        --max-papers 20 \
        --output literature_review.json
"""

import argparse
import json
from collections import defaultdict
from datetime import datetime

from arxiv_client import ArxivSearcher


def main():
    parser = argparse.ArgumentParser(
        description="Generate quick literature review"
    )

    # Search parameters
    parser.add_argument("--query", "-q", type=str, required=True,
                        help="Research query")
    parser.add_argument("--years", type=str, default="2020-2025",
                        help="Year range (e.g., 2023-2025)")
    parser.add_argument("--max-papers", "-m", type=int, default=50,
                        help="Maximum papers to analyze")
    parser.add_argument("--category", "-c", type=str, action="append",
                        help="Filter by category")

    # Output parameters
    parser.add_argument("--output", "-o", type=str, required=True,
                        help="Output file path")

    args = parser.parse_args()

    # Parse year range
    start_year, end_year = args.years.split("-")
    date_from = f"{start_year}-01-01"
    date_to = f"{end_year}-12-31"

    # Initialize searcher
    searcher = ArxivSearcher(max_results=args.max_papers)

    print(f"Searching for: {args.query}")
    print(f"Year range: {start_year}-{end_year}")

    # Execute search
    results = searcher.search(
        query=args.query,
        max_results=args.max_papers,
        date_from=date_from,
        date_to=date_to,
        categories=args.category,
    )

    papers = results.get("results", [])

    # Analyze papers
    analysis = {
        "query": args.query,
        "year_range": args.years,
        "total_papers": len(papers),
        "generated_at": datetime.now().isoformat(),
        "summary": _generate_summary(papers),
        "papers": _format_papers(papers),
        "bibliography": _generate_bibliography(papers),
    }

    # Save output
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)

    print(f"\nLiterature review saved to {args.output}")
    print(f"Analyzed {len(papers)} papers")


def _generate_summary(papers: list) -> dict:
    """Generate summary statistics."""
    if not papers:
        return {"message": "No papers found"}

    # Count by category
    category_counts = defaultdict(int)
    for paper in papers:
        for cat in paper.get("categories", []):
            category_counts[cat] += 1

    # Count by year
    year_counts = defaultdict(int)
    for paper in papers:
        date = paper.get("published", "")
        if date:
            year = date[:4]
            year_counts[year] += 1

    return {
        "category_distribution": dict(sorted(category_counts.items(), key=lambda x: -x[1])[:10]),
        "year_distribution": dict(sorted(year_counts.items())),
        "top_authors": _extract_top_authors(papers),
    }


def _format_papers(papers: list) -> list:
    """Format papers for output."""
    return [
        {
            "id": p.get("id"),
            "title": p.get("title"),
            "authors": p.get("authors")[:3],  # Top 3 authors
            "year": p.get("published", "")[:4] if p.get("published") else "",
            "categories": p.get("categories", [])[:2],
            "abstract_summary": p.get("abstract", "")[:300] + "...",
        }
        for p in papers
    ]


def _extract_top_authors(papers: list, top_n: int = 10) -> list:
    """Extract most frequent authors."""
    from collections import Counter

    authors = []
    for paper in papers:
        authors.extend(paper.get("authors", []))

    author_counts = Counter(authors)
    return [
        {"name": name, "count": count}
        for name, count in author_counts.most_common(top_n)
    ]


def _generate_bibliography(papers: list) -> str:
    """Generate bibliography in text format."""
    lines = ["# Bibliography\n"]

    for i, paper in enumerate(papers, 1):
        authors = ", ".join(paper.get("authors", ["Unknown"])[:3])
        if len(paper.get("authors", [])) > 3:
            authors += " et al."

        title = paper.get("title", "Unknown")
        year = paper.get("published", "")[:4] if paper.get("published") else "n.d."
        paper_id = paper.get("id", "")

        lines.append(f"[{i}] {authors} ({year}). {title}. arXiv:{paper_id}")

    return "\n".join(lines)


if __name__ == "__main__":
    main()
