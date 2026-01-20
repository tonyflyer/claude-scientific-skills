"""
Paper evaluator for innovation and methodology assessment.

Analyzes papers to assess novelty, methodology quality,
and provides structured evaluation scores.
"""

import re
from typing import Any


class PaperEvaluator:
    """Evaluate paper novelty, methodology, and quality."""

    # Innovation indicators
    NOVELTY_KEYWORDS = {
        "high": [
            "first", "novel", "new", "introduce", "propose", "proposed",
            "breakthrough", "revolutionary", "paradigm shift", "state-of-the-art",
            "significantly outperforms", "substantially improves", "new perspective",
        ],
        "medium": [
            "improve", "enhance", "extend", "build upon", "based on",
            "combine", "integrate", "unify", "generalize",
        ],
        "low": [
            "compare", "analyze", "study", "investigate", "evaluate",
            "benchmark", "survey", "review",
        ],
    }

    # Methodology quality indicators
    METHOD_STRENGTHS = [
        r"comprehensive experiments",
        r"extensive evaluation",
        r"rigorous analysis",
        r"theoretical guarantees",
        r"proof of",
        r"消融实验",  # ablation study
        r"ablation study",
        r"statistically significant",
        r"baseline", r"benchmarks",
        r"compare.*state-of-the-art",
        r"compare.*SOTA",
    ]

    METHOD_WEAKNESSES = [
        r"limited experiments?",
        r"small dataset",
        r"no ablation",
        r"no baseline",
        r"qualitative only",
        r"subjective evaluation",
        r"potential bias",
    ]

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def evaluate(self, paper_data: dict, extraction: dict | None = None) -> dict:
        """
        Evaluate a paper across multiple dimensions.

        Args:
            paper_data: Paper metadata
            extraction: Optional extracted sections

        Returns:
            Evaluation results dictionary
        """
        abstract = paper_data.get("abstract", "").lower()
        title = paper_data.get("title", "").lower()

        # Assess novelty
        novelty = self._assess_novelty(title, abstract)

        # Assess methodology
        methodology = self._assess_methodology(abstract)

        # Extract key findings
        key_findings = self._extract_key_findings(abstract)

        # Identify limitations
        limitations = self._identify_limitations(abstract)

        return {
            "innovation_score": novelty["score"],
            "novelty_level": novelty["level"],
            "novelty_points": novelty["points"],
            "methodology_score": methodology["score"],
            "methodology_strengths": methodology["strengths"],
            "methodology_weaknesses": methodology["weaknesses"],
            "key_findings": key_findings,
            "limitations": limitations,
            "overall_assessment": self._generate_assessment(novelty, methodology),
        }

    def _assess_novelty(self, title: str, abstract: str) -> dict:
        """Assess paper novelty from title and abstract."""
        text = f"{title} {abstract}"
        text_lower = text.lower()

        # Count novelty indicators
        high_count = sum(1 for kw in self.NOVELTY_KEYWORDS["high"] if kw in text_lower)
        medium_count = sum(1 for kw in self.NOVELTY_KEYWORDS["medium"] if kw in text_lower)
        low_count = sum(1 for kw in self.NOVELTY_KEYWORDS["low"] if kw in text_lower)

        # Calculate score (0-1)
        score = min(1.0, (high_count * 0.3 + medium_count * 0.15 + low_count * 0.05))

        # Determine level
        if score >= 0.7:
            level = "high"
        elif score >= 0.4:
            level = "medium"
        else:
            level = "incremental"

        # Extract novelty points
        points = []
        for kw in self.NOVELTY_KEYWORDS["high"]:
            if kw in text_lower:
                context = self._extract_context(text, kw)
                if context:
                    points.append(context)

        return {
            "score": round(score, 2),
            "level": level,
            "points": points[:5],  # Top 5 points
        }

    def _assess_methodology(self, abstract: str) -> dict:
        """Assess methodology quality from abstract."""
        text_lower = abstract.lower()

        # Find strengths
        strengths = []
        for pattern in self.METHOD_STRENGTHS:
            if re.search(pattern, text_lower):
                strengths.append(pattern.replace(r"\?", ""))

        # Find weaknesses
        weaknesses = []
        for pattern in self.METHOD_WEAKNESSES:
            if re.search(pattern, text_lower):
                weaknesses.append(pattern.replace(r"\?", ""))

        # Calculate score
        base_score = 0.5
        base_score += min(0.3, len(strengths) * 0.1)
        base_score -= min(0.3, len(weaknesses) * 0.15)
        score = min(1.0, max(0.0, base_score))

        return {
            "score": round(score, 2),
            "strengths": strengths[:5],
            "weaknesses": weaknesses[:5],
        }

    def _extract_key_findings(self, abstract: str) -> list[str]:
        """Extract key findings from abstract."""
        findings = []

        # Pattern for results
        result_patterns = [
            r"achieves? (?:state-of-the-art|SOTA) results?",
            r"outperforms? .* by .*%",
            r"improves? .* by .*%",
            r"reduces? .* by .*%",
            r"speeds? up .* by .*x",
            r"achieves? .* accuracy",
            r"enables? .* for the first time",
        ]

        for pattern in result_patterns:
            matches = re.findall(pattern, abstract, re.IGNORECASE)
            findings.extend(matches)

        return list(set(findings))[:5]

    def _identify_limitations(self, abstract: str) -> list[str]:
        """Identify potential limitations from abstract."""
        limitations = []

        limitation_patterns = [
            r"limited to",
            r"only applicable when",
            r"assumes? that",
            r"may not generalize to",
            r"computationally expensive",
            r"requires? large amounts? of",
            r"suffer[s]? from",
        ]

        for pattern in limitation_patterns:
            matches = re.findall(pattern, abstract, re.IGNORECASE)
            limitations.extend(matches)

        return list(set(limitations))[:5]

    def _extract_context(self, text: str, keyword: str, window: int = 50) -> str:
        """Extract context around a keyword."""
        idx = text.lower().find(keyword)
        if idx == -1:
            return ""

        start = max(0, idx - window)
        end = min(len(text), idx + len(keyword) + window)

        return text[start:end].strip()

    def _generate_assessment(self, novelty: dict, methodology: dict) -> str:
        """Generate overall assessment summary."""
        level = novelty["level"]
        score = novelty["score"]
        m_score = methodology["score"]

        if level == "high" and m_score >= 0.7:
            return ("This paper presents a highly novel contribution with strong methodology. "
                    "The work addresses an important problem with significant improvements over prior work.")
        elif level == "high":
            return ("This paper introduces novel ideas but would benefit from stronger experimental validation.")
        elif m_score >= 0.7:
            return ("This paper presents a solid methodology with incremental novelty. "
                    "The experimental evaluation is thorough and well-designed.")
        elif m_score >= 0.5:
            return ("This paper presents a reasonable approach with moderate novelty and adequate methodology.")
        else:
            return ("This paper addresses an interesting problem but would benefit from "
                    "improved methodology and more comprehensive evaluation.")

    def compare_papers(self, papers: list[dict]) -> dict:
        """
        Compare multiple papers in the same domain.

        Args:
            papers: List of paper evaluation dictionaries

        Returns:
            Comparison results
        """
        if not papers:
            return {"message": "No papers to compare"}

        # Sort by innovation score
        sorted_papers = sorted(
            papers,
            key=lambda x: x.get("innovation_score", 0),
            reverse=True,
        )

        return {
            "ranking": [
                {
                    "rank": i + 1,
                    "arxiv_id": p.get("arxiv_id", ""),
                    "title": p.get("title", ""),
                    "innovation_score": p.get("innovation_score", 0),
                    "methodology_score": p.get("methodology_score", 0),
                }
                for i, p in enumerate(sorted_papers[:10])
            ],
            "summary": {
                "total_papers": len(papers),
                "avg_innovation": sum(p.get("innovation_score", 0) for p in papers) / len(papers),
                "avg_methodology": sum(p.get("methodology_score", 0) for p in papers) / len(papers),
            },
        }
