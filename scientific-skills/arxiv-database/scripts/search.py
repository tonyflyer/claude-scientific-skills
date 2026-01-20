#!/usr/bin/env python3
"""
ArXiv search command-line tool.

Usage:
    python scripts/search.py --query "transformer" --max-results 50
    python scripts/search.py --author "Hinton" --output results.json
    python scripts/search.py --category cs.AI --days-back 30
"""

import argparse
import json
import sys

from arxiv_client import ArxivSearcher


def main():
    parser = argparse.ArgumentParser(
        description="Search arXiv for scientific papers"
    )

    # Search parameters
    parser.add_argument("--query", "-q", type=str, default="", help="Search query")
    parser.add_argument("--author", "-a", type=str, default="", help="Author name")
    parser.add_argument("--category", "-c", type=str, action="append",
                        help="arXiv category (can be used multiple times)")
    parser.add_argument("--categories", nargs="+", default=None,
                        help="List of arXiv categories")

    # ID lookup
    parser.add_argument("--id", type=str, default="", help="arXiv paper ID")

    # Result parameters
    parser.add_argument("--max-results", "-m", type=int, default=50,
                        help="Maximum number of results")
    parser.add_argument("--sort-by", type=str, default="relevance",
                        choices=["relevance", "lastUpdatedDate", "submittedDate"],
                        help="Sort criterion")
    parser.add_argument("--sort-order", type=str, default="descending",
                        choices=["ascending", "descending"],
                        help="Sort order")

    # Date parameters
    parser.add_argument("--start-date", type=str, default="",
                        help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", type=str, default="",
                        help="End date (YYYY-MM-DD)")
    parser.add_argument("--days-back", type=int, default=None,
                        help="Number of days to search back")

    # Output parameters
    parser.add_argument("--output", "-o", type=str, default="",
                        help="Output file (JSON)")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Enable verbose output")

    args = parser.parse_args()

    # Initialize searcher
    searcher = ArxivSearcher(max_results=args.max_results, verbose=args.verbose)

    # Handle categories
    categories = args.categories or args.category or None

    # Handle date range
    from datetime import datetime, timedelta

    start_date = args.start_date
    end_date = args.end_date

    if args.days_back:
        end_date = datetime.now().strftime("%Y-%m-%d")
        start_date = (datetime.now() - timedelta(days=args.days_back)).strftime("%Y-%m-%d")

    # Execute search
    if args.id:
        result = searcher.get_paper(args.id)
        results = {"result_count": 1 if result else 0, "results": [result] if result else []}
    elif args.author:
        results = searcher.search_author(
            author_name=args.author,
            max_results=args.max_results,
            date_from=start_date,
            date_to=end_date,
            categories=categories,
        )
    elif categories:
        results = searcher.search_category(
            categories=categories,
            max_results=args.max_results,
            date_from=start_date,
            date_to=end_date,
        )
    elif args.query:
        results = searcher.search(
            query=args.query,
            max_results=args.max_results,
            sort_by=args.sort_by,
            sort_order=args.sort_order,
            date_from=start_date,
            date_to=end_date,
            categories=categories,
        )
    else:
        # Default: search recent papers
        results = searcher.search(
            max_results=args.max_results,
            sort_by="submittedDate",
            sort_order="descending",
        )

    # Output results
    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"Results saved to {args.output}")
    else:
        print(json.dumps(results, indent=2, ensure_ascii=False))

    # Summary
    print(f"\nFound {results['result_count']} papers", file=sys.stderr)


if __name__ == "__main__":
    main()
