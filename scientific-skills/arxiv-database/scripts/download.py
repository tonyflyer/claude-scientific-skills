#!/usr/bin/env python3
"""
ArXiv download command-line tool.

Usage:
    python scripts/download.py --id 2401.12345 --output paper.pdf
    python scripts/download.py --input results.json --output ./papers
"""

import argparse
import json
import os
import sys

from arxiv_client import ArxivSearcher


def main():
    parser = argparse.ArgumentParser(
        description="Download papers from arXiv"
    )

    # Single paper mode
    parser.add_argument("--id", "-i", type=str, default="",
                        help="arXiv paper ID")

    # Batch mode
    parser.add_argument("--input", "-f", type=str, default="",
                        help="JSON file with search results")

    # Output parameters
    parser.add_argument("--output", "-o", type=str, default="./papers",
                        help="Output file or directory")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Enable verbose output")

    # Limits
    parser.add_argument("--max-papers", type=int, default=50,
                        help="Maximum papers to download (batch mode)")

    args = parser.parse_args()

    if not args.id and not args.input:
        parser.error("Either --id or --input must be provided")

    # Initialize searcher
    searcher = ArxivSearcher(verbose=args.verbose)

    # Single paper mode
    if args.id:
        output_path = args.output
        if os.path.isdir(args.output):
            output_path = os.path.join(args.output, f"{args.id}.pdf")

        if searcher.download_pdf(args.id, output_path):
            print(f"Downloaded: {output_path}")
        else:
            print(f"Failed to download: {args.id}", file=sys.stderr)
            sys.exit(1)

    # Batch mode
    else:
        if not os.path.isdir(args.output):
            os.makedirs(args.output, exist_ok=True)

        with open(args.input, "r") as f:
            data = json.load(f)

        results = data.get("results", [])
        total = min(len(results), args.max_papers)

        print(f"Downloading {total} papers to {args.output}")

        for i, paper in enumerate(results[:args.max_papers], 1):
            paper_id = paper.get("id")
            output_path = os.path.join(args.output, f"{paper_id}.pdf")

            if searcher.download_pdf(paper_id, output_path):
                print(f"[{i}/{total}] Downloaded: {paper_id}")
            else:
                print(f"[{i}/{total}] Failed: {paper_id}", file=sys.stderr)

            # Respect rate limits
            import time
            time.sleep(searcher.delay_seconds)

        print(f"\nCompleted: {total} papers")


if __name__ == "__main__":
    main()
