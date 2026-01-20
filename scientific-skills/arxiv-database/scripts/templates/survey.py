#!/usr/bin/env python3
"""
Survey Generation Template.

Generates a survey draft for a research topic.

Usage:
    python scripts/templates/survey.py \
        --query "transformer architectures" \
        --years 2020-2025 \
        --max-papers 100 \
        --output survey_draft.md
"""

import argparse
import json
import os
from collections import defaultdict
from datetime import datetime

from arxiv_client import ArxivSearcher
from analysis.evaluator import PaperEvaluator


def main():
    parser = argparse.ArgumentParser(
        description="Generate survey draft for a research topic"
    )

    parser.add_argument("--query", "-q", type=str, required=True,
                        help="Research topic query")
    parser.add_argument("--years", type=str, default="2020-2025",
                        help="Year range (e.g., 2020-2025)")
    parser.add_argument("--max-papers", "-m", type=int, default=100,
                        help="Maximum papers to analyze")
    parser.add_argument("--category", "-c", type=str, action="append",
                        help="Filter by category")
    parser.add_argument("--output", "-o", type=str, required=True,
                        help="Output file path")

    args = parser.parse_args()

    # Parse year range
    start_year, end_year = args.years.split("-")
    date_from = f"{start_year}-01-01"
    date_to = f"{end_year}-12-31"

    print(f"Generating survey on: {args.query}")
    print(f"Year range: {start_year}-{end_year}")
    print(f"Max papers: {args.max_papers}")

    # Initialize searcher and evaluator
    searcher = ArxivSearcher(max_results=args.max_papers)
    evaluator = PaperEvaluator()

    # Execute search
    results = searcher.search(
        query=args.query,
        max_results=args.max_papers,
        date_from=date_from,
        date_to=date_to,
        categories=args.category,
    )

    papers = results.get("results", [])
    print(f"Found {len(papers)} papers")

    # Analyze papers
    analysis = {
        "papers": [],
        "category_distribution": defaultdict(int),
        "year_distribution": defaultdict(int),
        "top_papers": [],
        "trend_analysis": {},
    }

    for paper in papers:
        # Evaluate paper
        evaluation = evaluator.evaluate(paper)

        paper_entry = {
            "id": paper.get("id"),
            "title": paper.get("title"),
            "authors": paper.get("authors"),
            "year": paper.get("published", "")[:4] if paper.get("published") else "",
            "categories": paper.get("categories"),
            "innovation_score": evaluation.get("innovation_score"),
            "key_findings": evaluation.get("key_findings"),
        }

        analysis["papers"].append(paper_entry)

        # Update distributions
        for cat in paper.get("categories", []):
            analysis["category_distribution"][cat] += 1

        year = paper.get("published", "")[:4] if paper.get("published") else ""
        if year:
            analysis["year_distribution"][year] += 1

    # Sort by innovation score for top papers
    analysis["top_papers"] = sorted(
        analysis["papers"],
        key=lambda x: x.get("innovation_score", 0),
        reverse=True
    )[:20]

    # Generate survey draft
    survey_content = _generate_survey_markdown(
        args.query,
        start_year,
        end_year,
        analysis,
    )

    # Save output
    if args.output.endswith(".md"):
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(survey_content)
    else:
        # Save as JSON if not markdown
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(analysis, f, indent=2, ensure_ascii=False)

    print(f"\nSurvey saved to {args.output}")
    _print_summary(analysis)


def _generate_survey_markdown(query: str, start_year: str, end_year: str, analysis: dict) -> str:
    """Generate markdown survey draft."""
    md = []

    # Title
    md.append(f"# A Survey on {query.title()}")
    md.append(f"**{start_year}-{end_year}**")
    md.append("")
    md.append(f"*Generated on: {datetime.now().strftime('%Y-%m-%d')}*")
    md.append("")

    # Abstract placeholder
    md.append("## Abstract")
    md.append("")
    md.append("This survey provides a comprehensive overview of recent advances in the field of "
              f"{query.lower()} during the period {start_year}-{end_year}. We analyze {len(analysis['papers'])} "
              "papers from major venues and preprints, identifying key trends, methodological innovations, "
              "and future research directions.")
    md.append("")

    # Introduction
    md.append("## 1. Introduction")
    md.append("")
    md.append(f"The field of {query.lower()} has seen significant growth in recent years. "
              f"This survey covers {len(analysis['papers'])} papers published between "
              f"{start_year} and {end_year}, providing a systematic review of the state-of-the-art.")
    md.append("")

    # Categorization
    md.append("## 2. Taxonomies and Categorization")
    md.append("")

    # Category distribution
    md.append("### 2.1 Distribution by Research Area")
    md.append("")
    md.append("| Category | Number of Papers |")
    md.append("|----------|-----------------|")
    for cat, count in sorted(analysis["category_distribution"].items(), key=lambda x: -x[1])[:10]:
        md.append(f"| {cat} | {count} |")
    md.append("")

    # Year distribution
    md.append("### 2.2 Publication Trends by Year")
    md.append("")
    for year in sorted(analysis["year_distribution"].keys()):
        count = analysis["year_distribution"][year]
        bar = "█" * (count // 5)
        md.append(f"- **{year}**: {bar} ({count})")
    md.append("")

    # Key papers section
    md.append("## 3. Key Papers and Contributions")
    md.append("")

    for i, paper in enumerate(analysis["top_papers"][:10], 1):
        md.append(f"### 3.{i} {paper['title'][:60]}...")
        md.append("")
        md.append(f"**Authors:** {', '.join(paper.get('authors', [])[:3])}")
        md.append(f"**Year:** {paper.get('year', 'N/A')}")
        md.append(f"**arXiv ID:** {paper.get('id', 'N/A')}")
        md.append(f"**Innovation Score:** {paper.get('innovation_score', 'N/A')}")
        md.append("")
        md.append("**Key Contributions:**")
        for finding in paper.get("key_findings", [])[:3]:
            md.append(f"- {finding}")
        md.append("")

    # Methods section
    md.append("## 4. Methodology Analysis")
    md.append("")

    # Group papers by methodology type
    md.append("### 4.1 Common Approaches")
    md.append("")
    md.append("Based on our analysis, we identify the following dominant methodologies:")
    md.append("")
    md.append("- **Method A**: Description...")
    md.append("- **Method B**: Description...")
    md.append("- **Method C**: Description...")
    md.append("")

    md.append("### 4.2 Emerging Techniques")
    md.append("")
    md.append("Several emerging techniques have gained attention:")
    md.append("")
    md.append("- **Technique A**: Description...")
    md.append("- **Technique B**: Description...")
    md.append("")

    # Trends section
    md.append("## 5. Trends and Future Directions")
    md.append("")

    md.append("### 5.1 Observed Trends")
    md.append("")
    md.append("Based on the literature review, we observe the following trends:")
    md.append("")
    md.append("1. **Trend 1**: Description...")
    md.append("2. **Trend 2**: Description...")
    md.append("3. **Trend 3**: Description...")
    md.append("")

    md.append("### 5.2 Open Challenges")
    md.append("")
    md.append("Several challenges remain open:")
    md.append("")
    md.append("- **Challenge 1**: Description...")
    md.append("- **Challenge 2**: Description...")
    md.append("- **Challenge 3**: Description...")
    md.append("")

    # Conclusion
    md.append("## 6. Conclusion")
    md.append("")
    md.append(f"This survey has presented a comprehensive overview of {query.lower()} "
              f"research from {start_year} to {end_year}. The field continues to evolve rapidly, "
              "with new methodologies and applications emerging regularly.")
    md.append("")

    # Bibliography
    md.append("## References")
    md.append("")
    for i, paper in enumerate(analysis["top_papers"], 1):
        authors = ", ".join(paper.get("authors", ["Unknown"])[:3])
        if len(paper.get("authors", [])) > 3:
            authors += " et al."
        year = paper.get("year", "n.d.")
        title = paper.get("title", "Unknown")
        paper_id = paper.get("id", "")

        md.append(f"[{i}] {authors} ({year}). {title}. arXiv:{paper_id}")
    md.append("")

    return "\n".join(md)


def _print_summary(analysis: dict):
    """Print summary to console."""
    print("\n" + "=" * 60)
    print("SURVEY GENERATION SUMMARY")
    print("=" * 60)

    print(f"\n📊 Total Papers Analyzed: {len(analysis['papers'])}")

    print("\n📁 Category Distribution (Top 5):")
    for cat, count in list(analysis["category_distribution"].items())[:5]:
        print(f"   {cat}: {count}")

    print("\n📅 Year Distribution:")
    for year in sorted(analysis["year_distribution"].keys()):
        print(f"   {year}: {analysis['year_distribution'][year]} papers")

    print("\n⭐ Top 5 Most Innovative Papers:")
    for i, paper in enumerate(analysis["top_papers"][:5], 1):
        print(f"   {i}. {paper['title'][:50]}...")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
