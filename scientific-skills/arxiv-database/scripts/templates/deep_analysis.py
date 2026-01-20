#!/usr/bin/env python3
"""
Deep Paper Analysis Template.

Generates comprehensive analysis of a single paper.

Usage:
    python scripts/templates/deep_analysis.py \
        --paper-id 2401.12345 \
        --output analysis_report.json
"""

import argparse
import json
from datetime import datetime

from arxiv_client import ArxivSearcher
from analysis.extractor import PaperExtractor
from analysis.evaluator import PaperEvaluator
from analysis.reviewer import PaperReviewer


def main():
    parser = argparse.ArgumentParser(
        description="Generate deep analysis of an arXiv paper"
    )

    parser.add_argument("--paper-id", "-p", type=str, required=True,
                        help="arXiv paper ID")
    parser.add_argument("--output", "-o", type=str, required=True,
                        help="Output file path")
    parser.add_argument("--include-pdf", action="store_true",
                        help="Include PDF text analysis (requires local PDF)")
    parser.add_argument("--download", action="store_true",
                        help="Download paper PDF first")

    args = parser.parse_args()

    print(f"Analyzing paper: {args.paper_id}")

    # Initialize components
    searcher = ArxivSearcher()
    extractor = PaperExtractor()
    evaluator = PaperEvaluator()
    reviewer = PaperReviewer()

    # Get paper data
    paper_data = searcher.get_paper(args.paper_id)
    if not paper_data:
        print(f"Error: Paper not found: {args.paper_id}")
        return

    print(f"Title: {paper_data.get('title', '')[:60]}...")

    # Extract structured information
    extraction = extractor.extract(paper_data)

    # Evaluate paper
    evaluation = evaluator.evaluate(paper_data, extraction)

    # Generate peer review
    review = reviewer.generate_review(args.paper_id, paper_data, evaluation)

    # Compile analysis report
    analysis = {
        "paper_id": args.paper_id,
        "generated_at": datetime.now().isoformat(),
        "metadata": paper_data,
        "extraction": extraction,
        "evaluation": evaluation,
        "peer_review": review,
        "recommendations": _generate_recommendations(evaluation, review),
    }

    # Save output
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)

    print(f"\nAnalysis saved to {args.output}")

    # Print summary
    _print_summary(evaluation, review)


def _generate_recommendations(evaluation: dict, review: dict) -> dict:
    """Generate recommendations based on analysis."""
    recommendations = {
        "for_authors": [],
        "for_reviewers": [],
        "for_readers": [],
    }

    # Author recommendations
    if review.get("revision_suggestions"):
        for suggestion in review["revision_suggestions"][:3]:
            recommendations["for_authors"].append(
                f"[{suggestion['priority'].upper()}] {suggestion['suggestion']}"
            )

    # Reviewer recommendations
    recommendations["for_reviewers"] = [
        "Focus on the novelty and contribution of the work",
        "Evaluate the methodology and experimental design",
        "Check reproducibility and availability of code/data",
    ]

    # Reader recommendations
    if evaluation.get("innovation_score", 0) >= 0.7:
        recommendations["for_readers"].append(
            "This paper presents significant novel contributions - highly recommended"
        )
    else:
        recommendations["for_readers"].append(
            "This paper provides incremental improvements - useful for specific applications"
        )

    return recommendations


def _print_summary(evaluation: dict, review: dict):
    """Print analysis summary to console."""
    print("\n" + "=" * 60)
    print("ANALYSIS SUMMARY")
    print("=" * 60)

    print(f"\n📊 Innovation Score: {evaluation.get('innovation_score', 'N/A')}/1.0")
    print(f"📊 Methodology Score: {evaluation.get('methodology_score', 'N/A')}/1.0")
    print(f"⭐ Overall Rating: {review['overall_assessment']['score']}/5")

    print("\n🔑 Novelty Points:")
    for point in evaluation.get("novelty_points", [])[:3]:
        print(f"  • {point[:80]}...")

    print("\n💡 Key Findings:")
    for finding in evaluation.get("key_findings", [])[:3]:
        print(f"  • {finding[:80]}...")

    print("\n📝 Revision Suggestions:")
    for suggestion in review.get("revision_suggestions", [])[:3]:
        print(f"  [{suggestion['priority'].upper()}] {suggestion['issue']}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
