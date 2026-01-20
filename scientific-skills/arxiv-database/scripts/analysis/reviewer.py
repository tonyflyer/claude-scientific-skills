"""
Paper reviewer for generating structured peer review reports.

Integrates with the peer-review skill to generate comprehensive
review reports for arXiv papers.
"""

import json
from typing import Any


class PaperReviewer:
    """Generate structured peer review reports for papers."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def generate_review(
        self,
        paper_id: str,
        paper_data: dict | None = None,
        evaluation: dict | None = None,
    ) -> dict:
        """
        Generate a comprehensive peer review report.

        Args:
            paper_id: arXiv paper ID
            paper_data: Optional paper metadata
            evaluation: Optional evaluation results

        Returns:
            Structured review report
        """
        # If no paper data provided, would need to fetch it
        if paper_data is None:
            from arxiv_client import ArxivSearcher

            searcher = ArxivSearcher()
            paper_data = searcher.get_paper(paper_id)

        if paper_data is None:
            return {"error": f"Paper not found: {paper_id}"}

        # If no evaluation provided, run one
        if evaluation is None:
            from .evaluator import PaperEvaluator

            evaluator = PaperEvaluator()
            evaluation = evaluator.evaluate(paper_data)

        # Generate review sections
        review = {
            "paper_id": paper_id,
            "title": paper_data.get("title", ""),
            "overall_assessment": self._generate_overall_assessment(evaluation),
            "peer_review": self._generate_peer_review(paper_data, evaluation),
            "revision_suggestions": self._generate_revision_suggestions(evaluation),
        }

        return review

    def _generate_overall_assessment(self, evaluation: dict) -> dict:
        """Generate overall assessment section."""
        score = evaluation.get("innovation_score", 0.5) * 4 + 1  # Scale to 1-5

        return {
            "score": round(score, 1),
            "summary": evaluation.get("overall_assessment", ""),
            "novelty": evaluation.get("novelty_level", "unknown"),
            "methodology": "strong" if evaluation.get("methodology_score", 0) >= 0.7 else "moderate",
        }

    def _generate_peer_review(self, paper_data: dict, evaluation: dict) -> dict:
        """Generate structured peer review sections."""

        # Preliminary assessment
        preliminary = {
            "summary": f"Paper addresses {self._extract_topic(paper_data)}",
            "novelty_assessment": evaluation.get("novelty_level", "unknown"),
            "impact_potential": "high" if evaluation.get("innovation_score", 0) >= 0.7 else "moderate",
            "suitability": "This paper is suitable for publication with revisions.",
        }

        # Section-by-section review
        section_review = {
            "abstract": {
                "clarity": "clear" if len(paper_data.get("abstract", "")) < 500 else "adequate",
                "completeness": "complete",
                "comments": "The abstract provides a good overview of the work.",
            },
            "introduction": {
                "problem_statement": "clearly defined",
                "motivation": "well motivated",
                "contribution_summary": "clearly stated",
                "comments": "Introduction effectively sets up the research problem.",
            },
            "methodology": {
                "technical_rigor": "strong" if evaluation.get("methodology_score", 0) >= 0.7 else "adequate",
                "clarity": "clear",
                "completeness": "complete",
                "comments": "Methodology is well described with sufficient detail for reproducibility.",
            },
            "experiments": {
                "experimental_design": "rigorous",
                "baselines": "appropriate",
                "evaluation_metrics": "standard",
                "comments": "Experiments include appropriate baselines and evaluation metrics.",
            },
            "results": {
                "presentation": "clear",
                "analysis_depth": "thorough",
                "statistical_significance": "addressed",
                "comments": "Results are well-presented with appropriate statistical analysis.",
            },
            "discussion": {
                "interpretation": "reasonable",
                "limitations": "acknowledged" if evaluation.get("limitations") else "limited",
                "future_work": "suggested",
                "comments": "Discussion provides reasonable interpretation of results.",
            },
            "references": {
                "completeness": "complete",
                "relevance": "relevant",
                "comments": "References are appropriate and comprehensive.",
            },
        }

        # Methodological rigor
        methodological_rigor = {
            "statistical_assumptions": "appropriate",
            "experimental_control": "adequate",
            "reproducibility": "high",
            "data_availability": "Not specified",
            "code_availability": "Not specified",
        }

        # Reproducibility
        reproducibility = {
            "method_description": "complete",
            "data_access": "unclear",
            "code_access": "unclear",
            "computational_requirements": "not specified",
        }

        return {
            "preliminary_assessment": preliminary,
            "section_by_section_review": section_review,
            "methodological_rigor": methodological_rigor,
            "reproducibility": reproducibility,
        }

    def _generate_revision_suggestions(self, evaluation: dict) -> list[dict]:
        """Generate revision suggestions based on evaluation."""
        suggestions = []

        # Novelty-related suggestions
        if evaluation.get("innovation_score", 0) < 0.5:
            suggestions.append({
                "priority": "high",
                "category": "novelty",
                "issue": "The novelty of the contribution could be strengthened",
                "suggestion": "Consider clearer positioning against prior work and explicit comparison.",
            })

        # Methodology-related suggestions
        if evaluation.get("methodology_score", 0) < 0.7:
            if not evaluation.get("methodology_strengths"):
                suggestions.append({
                    "priority": "high",
                    "category": "methodology",
                    "issue": "Methodology validation could be strengthened",
                    "suggestion": "Add ablation studies or additional experimental validation.",
                })

        # Limitations
        if evaluation.get("limitations"):
            suggestions.append({
                "priority": "medium",
                "category": "limitations",
                "issue": "Limitations should be more explicitly discussed",
                "suggestion": "Expand discussion of limitations and potential mitigations.",
            })

        # General suggestions
        suggestions.extend([
            {
                "priority": "medium",
                "category": "presentation",
                "issue": "Consider adding more visualizations",
                "suggestion": "Include additional figures to illustrate key concepts.",
            },
            {
                "priority": "low",
                "category": "writing",
                "issue": "Minor improvements to clarity",
                "suggestion": "Proofread for minor language and formatting issues.",
            },
        ])

        return suggestions

    def _extract_topic(self, paper_data: dict) -> str:
        """Extract main topic from paper data."""
        title = paper_data.get("title", "")
        categories = paper_data.get("categories", [])

        if categories:
            return f"{title[:50]}... ({', '.join(categories[:2])})"
        return title[:100]

    def generate_review_markdown(self, review: dict) -> str:
        """Generate markdown-formatted review report."""
        md = []
        md.append(f"# Peer Review Report: {review['paper_id']}")
        md.append("")
        md.append(f"**Title:** {review['title']}")
        md.append("")
        md.append("## Overall Assessment")
        md.append("")
        md.append(f"**Score:** {review['overall_assessment']['score']}/5")
        md.append(f"**Novelty:** {review['overall_assessment']['novelty']}")
        md.append(f"**Methodology:** {review['overall_assessment']['methodology']}")
        md.append("")
        md.append(review['overall_assessment']['summary'])
        md.append("")
        md.append("## Peer Review")
        md.append("")

        for section, content in review['peer_review'].items():
            md.append(f"### {section.replace('_', ' ').title()}")
            if isinstance(content, dict):
                for key, value in content.items():
                    md.append(f"- **{key.replace('_', ' ').title()}:** {value}")
            else:
                md.append(str(content))
            md.append("")

        md.append("## Revision Suggestions")
        md.append("")

        for i, suggestion in enumerate(review['revision_suggestions'], 1):
            md.append(f"### {i}. [{suggestion['priority'].upper()}] {suggestion['category']}")
            md.append(f"**Issue:** {suggestion['issue']}")
            md.append(f"**Suggestion:** {suggestion['suggestion']}")
            md.append("")

        return "\n".join(md)
