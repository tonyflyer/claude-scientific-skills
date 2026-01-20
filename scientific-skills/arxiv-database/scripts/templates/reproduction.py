#!/usr/bin/env python3
"""
Paper Reproduction Template.

Generates a plan for reproducing paper experiments.

Usage:
    python scripts/templates/reproduction.py \
        --paper-id 2401.12345 \
        --output reproduction_plan.json
"""

import argparse
import json
from datetime import datetime

from arxiv_client import ArxivSearcher
from analysis.extractor import PaperExtractor


def main():
    parser = argparse.ArgumentParser(
        description="Generate reproduction plan for an arXiv paper"
    )

    parser.add_argument("--paper-id", "-p", type=str, required=True,
                        help="arXiv paper ID")
    parser.add_argument("--output", "-o", type=str, required=True,
                        help="Output file path")
    parser.add_argument("--download-pdf", action="store_true",
                        help="Download paper PDF")

    args = parser.parse_args()

    print(f"Creating reproduction plan for: {args.paper_id}")

    # Get paper data
    searcher = ArxivSearcher()
    paper_data = searcher.get_paper(args.paper_id)

    if not paper_data:
        print(f"Error: Paper not found: {args.paper_id}")
        return

    # Extract methodology section
    extractor = PaperExtractor()
    extraction = extractor.extract(paper_data)
    methodology = extraction.get("sections", {}).get("methodology", "")

    # Generate reproduction plan
    plan = {
        "paper_id": args.paper_id,
        "title": paper_data.get("title"),
        "generated_at": datetime.now().isoformat(),
        "reproduction_plan": _generate_plan(paper_data, methodology),
        "implementation_guide": _generate_implementation_guide(methodology),
        "data_requirements": _identify_data_requirements(paper_data, methodology),
        "code_structure": _suggest_code_structure(paper_data),
        "evaluation_checklist": _generate_evaluation_checklist(paper_data),
    }

    # Save output
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)

    print(f"Reproduction plan saved to {args.output}")
    _print_summary(plan)


def _generate_plan(paper_data: dict, methodology: str) -> dict:
    """Generate step-by-step reproduction plan."""
    return {
        "phase1_preparation": {
            "steps": [
                "Download and read the paper carefully",
                "Identify key claims and results to reproduce",
                "Gather required datasets",
                "Set up development environment",
                "Clone or implement the model code",
            ],
            "estimated_time": "2-4 hours",
        },
        "phase2_implementation": {
            "steps": [
                "Implement data preprocessing pipeline",
                "Implement model architecture",
                "Implement training procedure",
                "Implement evaluation metrics",
            ],
            "estimated_time": "4-8 hours",
        },
        "phase3_training": {
            "steps": [
                "Train model on original dataset",
                "Monitor training progress",
                "Save checkpoints",
            ],
            "estimated_time": "Depends on model size",
        },
        "phase4_evaluation": {
            "steps": [
                "Run evaluation on test set",
                "Compare with reported results",
                "Run additional analysis if needed",
            ],
            "estimated_time": "1-2 hours",
        },
        "phase5_reporting": {
            "steps": [
                "Document reproduction results",
                "Note any deviations from paper",
                "Summarize findings",
            ],
            "estimated_time": "1 hour",
        },
    }


def _generate_implementation_guide(methodology: str) -> dict:
    """Generate implementation guidance based on methodology."""
    return {
        "key_components": [
            "Data loader for the specific dataset",
            "Model architecture implementation",
            "Training loop with appropriate hyperparameters",
            "Evaluation scripts",
        ],
        "hyperparameters": {
            "note": "Extract specific values from paper methodology section",
            "common_params": [
                "learning_rate",
                "batch_size",
                "number_of_epochs",
                "optimizer",
                "weight_decay",
            ],
        },
        "dependencies": [
            "torch / tensorflow / jax",
            "numpy",
            "pandas",
            "scikit-learn",
            "Dataset-specific packages",
        ],
    }


def _identify_data_requirements(paper_data: dict, methodology: str) -> dict:
    """Identify data requirements for reproduction."""
    return {
        "primary_dataset": "See paper for dataset name and source",
        "preprocessing_steps": "Extract from methodology section",
        "data_format": "Typically: train/val/test split",
        "expected_size": "See paper experimental setup",
        "download_links": "See paper or supplementary materials",
    }


def _suggest_code_structure(paper_data: dict) -> dict:
    """Suggest code directory structure."""
    title = paper_data.get("title", "").lower()

    return {
        "recommended_structure": {
            "data/": "Dataset and preprocessing scripts",
            "models/": "Model architecture implementations",
            "training/": "Training scripts",
            "evaluation/": "Evaluation and metrics scripts",
            "configs/": "Configuration files",
            "notebooks/": "Analysis notebooks",
        },
        "main_scripts": [
            "train.py - Main training script",
            "evaluate.py - Evaluation script",
            "inference.py - Inference script",
        ],
    }


def _generate_evaluation_checklist(paper_data: dict) -> list:
    """Generate evaluation checklist for reproduction."""
    return [
        {
            "item": "Primary metric match",
            "description": "Does the reproduction achieve similar primary metric?",
            "tolerance": "Typically within 1-5% of paper value",
        },
        {
            "item": "Training stability",
            "description": "Does training converge as expected?",
            "tolerance": "N/A - qualitative check",
        },
        {
            "item": "Ablation studies",
            "description": "Can you reproduce key ablation results?",
            "tolerance": "Consistent trends",
        },
        {
            "item": "Qualitative results",
            "description": "Do qualitative results match paper?",
            "tolerance": "N/A - visual comparison",
        },
        {
            "item": "Runtime/memory",
            "description": "Do resource requirements match paper?",
            "tolerance": "Within 20%",
        },
    ]


def _print_summary(plan: dict):
    """Print summary to console."""
    print("\n" + "=" * 60)
    print("REPRODUCTION PLAN SUMMARY")
    print("=" * 60)

    print(f"\n📄 Paper: {plan['title'][:60]}...")

    reproduction = plan.get("reproduction_plan", {})
    for phase, details in reproduction.items():
        print(f"\n📋 {phase.replace('_', ' ').title()}")
        print(f"   Time: {details.get('estimated_time', 'TBD')}")
        for step in details.get("steps", [])[:2]:
            print(f"   • {step}")

    print("\n✅ Evaluation Checklist:")
    for item in plan.get("evaluation_checklist", [])[:3]:
        print(f"   • {item['item']}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
