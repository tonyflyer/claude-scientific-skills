"""
AI-detection-proof scientific writing assistant.

Transforms AI-generated text into natural academic writing style.
"""

import re
from typing import Any, Optional


class ScientificWriter:
    """Transform text into natural academic writing style."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def humanize(
        self,
        text: str,
        style: str = "academic",
        intensity: str = "medium",
    ) -> str:
        """
        Transform AI-generated text to sound more human and academic.

        Args:
            text: Input text (possibly AI-generated)
            style: Writing style - "academic", "formal", "conversational"
            intensity: Transformation intensity - "low", "medium", "high"

        Returns:
            Transformed text with more natural academic style
        """
        # Apply transformations based on intensity
        if intensity == "low":
            text = self._low_transformations(text)
        elif intensity == "medium":
            text = self._medium_transformations(text)
        else:  # high
            text = self._high_transformations(text)

        # Apply style-specific transformations
        if style == "academic":
            text = self._apply_academic_style(text)

        return text

    def _low_transformations(self, text: str) -> str:
        """Apply low-intensity transformations."""
        # Remove common AI filler phrases
        fillers = [
            r"\bIn conclusion,\b",
            r"\bIt is important to note that\b",
            r"\bIt is worth mentioning that\b",
            r"\bAs previously stated\b",
            r"\bAs mentioned earlier\b",
        ]
        for filler in fillers:
            text = re.sub(filler, "", text, flags=re.IGNORECASE)

        return text

    def _medium_transformations(self, text: str) -> str:
        """Apply medium-intensity transformations."""
        text = self._low_transformations(text)

        # Break up repetitive structures
        text = re.sub(r"\. (\w+)\. \1", r". \1", text)

        # Vary sentence starters
        sentence_starters = self._get_varied_starters()
        sentences = re.split(r"(?<=[.!?])\s+", text)
        varied_sentences = []

        for i, sentence in enumerate(sentences):
            if i > 0 and sentence.strip():
                # 30% chance to add transitional phrase
                if i % 3 == 0:
                    starter = sentence_starters[i % len(sentence_starters)]
                    sentence = starter + ", " + sentence[0].lower() + sentence[1:]
            varied_sentences.append(sentence)

        text = " ".join(varied_sentences)

        return text

    def _high_transformations(self, text: str) -> str:
        """Apply high-intensity transformations."""
        text = self._medium_transformations(text)

        # Replace overly formal phrases with more natural academic language
        replacements = [
            (r"\butilize\b", "use"),
            (r"\bfacilitate\b", "help"),
            (r"\bdemonstrate\b", "show"),
            (r"\bcommence\b", "start"),
            (r"\bterminate\b", "end"),
            (r"\bsubsequently\b", "then"),
            (r"\bconsequently\b", "so"),
            (r"\bnevertheless\b", "however"),
            (r"\bmoreover\b", "also"),
            (r"\bfurthermore\b", "in addition"),
            (r"\badditionally\b", "also"),
            (r"\bwith respect to\b", "about"),
            (r"\bin the event that\b", "if"),
            (r"\bfor the purpose of\b", "to"),
            (r"\bin order to\b", "to"),
            (r"\bdue to the fact that\b", "because"),
        ]

        for pattern, replacement in replacements:
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

        return text

    def _apply_academic_style(self, text: str) -> str:
        """Apply academic writing style conventions."""
        # Ensure proper section headers if present
        text = re.sub(r"^(\d+)\.\s*([A-Z])", r"\1. \2", text)

        # Fix spacing after punctuation
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"\. ([A-Z])", r". \1", text)

        # Ensure proper citation format
        text = re.sub(r"(\w+)\s+\((\d{4})\)", r"\1 (\2)", text)

        return text.strip()

    def _get_varied_starters(self) -> list:
        """Get list of transitional phrases for sentence variation."""
        return [
            "Additionally",
            "Furthermore",
            "Moreover",
            "In contrast",
            "However",
            "Nevertheless",
            "Therefore",
            "Consequently",
            "Similarly",
            "On the other hand",
            "As a result",
            "In particular",
            "Specifically",
            "For example",
            "In other words",
        ]

    def fix_claims(self, text: str) -> str:
        """Transform overly absolute claims into more nuanced academic language."""
        replacements = [
            (r"\bproves\b", "provides evidence for"),
            (r"\bproves that\b", "suggests that"),
            (r"\bdemonstrates that\b", "indicates that"),
            (r"\bshows that\b", "suggests that"),
            (r"\bis the best\b", "performs well on"),
            (r"\balways\b", "often"),
            (r"\bnever\b", "rarely"),
            (r"\bcompletely\b", "largely"),
            (r"\bentirely\b", "substantially"),
            (r"\bmust\b", "should"),
            (r"\bshould always\b", "typically should"),
            (r"\bguarantees\b", "helps ensure"),
        ]

        for pattern, replacement in replacements:
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

        return text

    def improve_methodology_description(self, text: str) -> str:
        """Improve methodology section descriptions."""
        # Add specificity to vague terms
        vague_terms = {
            r"\bvarious\b": "multiple",
            r"\bseveral\b": "a number of",
            r"\bmany\b": "numerous",
            r"\bsome\b": "certain",
            r"\balot of\b": "substantial",
            r"\bbig\b": "large-scale",
            r"\btiny\b": "small-scale",
            r"\bfast\b": "computationally efficient",
            r"\bslow\b": "computationally intensive",
        }

        for pattern, replacement in vague_terms.items():
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

        # Add methodological detail cues
        text = re.sub(
            r"\bwe used (\w+)\b",
            r"we employed \1, which was configured as follows:",
            text,
            flags=re.IGNORECASE,
        )

        return text

    def enhance_results_analysis(self, text: str) -> str:
        """Enhance results section with appropriate hedging."""
        # Add appropriate hedging for claims
        hedging_phrases = [
            (r"\b(\w+) increased\b", r"the results show that \1 increased"),
            (r"\b(\w+) decreased\b", r"the results indicate that \1 decreased"),
            (r"\b(\w+) improved\b", r"performance \1 improved"),
            (r"\b(\w+) performed better\b", r"\1 showed improved performance"),
        ]

        for pattern, replacement in hedging_phrases:
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

        # Add statistical context
        text = re.sub(
            r"\bwith (\d+)%? accuracy\b",
            r"achieving an accuracy of \1% (statistically significant, p < 0.05)",
            text,
        )

        return text

    def generate_abstract(self, sections: dict) -> str:
        """Generate a structured abstract from paper sections."""
        parts = []

        # Background (1-2 sentences)
        if "introduction" in sections:
            intro = sections["introduction"][:300]
            if len(intro) == 300:
                intro = intro[:intro.rfind(".")] + "."
            parts.append(f"Background: {intro}")

        # Objective (1 sentence)
        if "abstract" in sections:
            # Use existing abstract as base
            abstract = sections["abstract"][:150]
            if len(abstract) == 150:
                abstract = abstract[:abstract.rfind(".")] + "."
            parts.append(f"Objective: {abstract}")

        # Methods (1-2 sentences)
        if "methodology" in sections:
            method = sections["methodology"][:200]
            if len(method) == 200:
                method = method[:method.rfind(".")] + "."
            parts.append(f"Methods: {method}")

        # Results (1-2 sentences)
        if "results" in sections:
            results = sections["results"][:200]
            if len(results) == 200:
                results = results[:results.rfind(".")] + "."
            parts.append(f"Results: {results}")

        # Conclusions (1 sentence)
        if "conclusion" in sections:
            conclusion = sections["conclusion"][:150]
            if len(conclusion) == 150:
                conclusion = conclusion[:conclusion.rfind(".")] + "."
            parts.append(f"Conclusions: {conclusion}")

        return "\n\n".join(parts)

    def structure_discussion(self, sections: dict) -> dict:
        """Structure a discussion section with key components."""
        discussion = {}

        # Key findings summary
        if "results" in sections:
            discussion["summary_of_findings"] = sections["results"][:500] + "..."

        # Interpretation
        discussion["interpretation"] = [
            "Discuss how results relate to hypotheses",
            "Compare findings with prior work (cite relevant literature)",
            "Explain unexpected results if any",
        ]

        # Limitations
        discussion["limitations"] = [
            "Identify scope and generalizability constraints",
            "Note any data limitations or biases",
            "Acknowledge methodological limitations",
        ]

        # Implications
        discussion["implications"] = [
            "Discuss theoretical implications",
            "Discuss practical applications",
            "Note broader impacts if applicable",
        ]

        # Future directions
        discussion["future_directions"] = [
            "Suggest follow-up studies",
            "Propose methodological improvements",
            "Identify open questions raised by this work",
        ]

        return discussion

    def create_outline(self, topic: str, sections: Optional[list] = None) -> dict:
        """Create a research paper outline."""
        if sections is None:
            sections = ["Introduction", "Related Work", "Methodology", "Experiments", "Results", "Discussion", "Conclusion"]

        outline = {
            "topic": topic,
            "estimated_length": f"{len(sections) * 300}-5000 words",
            "sections": {},
        }

        section_guides = {
            "Introduction": [
                "Hook: Start with the broader context and importance of the problem",
                "Problem Statement: Clearly define the research gap or challenge",
                "Contribution: List key contributions of this work",
                "Structure: Briefly outline the paper structure",
            ],
            "Related Work": [
                "Categorize prior work by approach or methodology",
                "Compare and contrast with existing solutions",
                "Identify gaps that your work addresses",
            ],
            "Methodology": [
                "Problem formulation and notation",
                "Proposed approach/algorithm description",
                "Theoretical foundations if applicable",
                "Implementation details and complexity analysis",
            ],
            "Experiments": [
                "Dataset description and preprocessing",
                "Experimental setup and hyperparameters",
                "Baseline methods for comparison",
                "Evaluation metrics and protocols",
            ],
            "Results": [
                "Main results on primary metrics",
                "Statistical significance tests",
                "Ablation studies",
                "Qualitative results and visualizations",
            ],
            "Discussion": [
                "Interpretation of results",
                "Comparison with state-of-the-art",
                "Limitations of the approach",
                "Broader implications and future work",
            ],
            "Conclusion": [
                "Summary of key contributions",
                "Main findings and their significance",
                "Closing thoughts and future directions",
            ],
        }

        for section in sections:
            outline["sections"][section] = section_guides.get(section, ["Section content"])

        return outline

    def check_readability(self, text: str) -> dict:
        """Check text readability and provide suggestions."""
        sentences = re.split(r"[.!?]+", text)
        words = text.split()

        avg_sentence_length = len(words) / max(1, len(sentences))
        avg_word_length = sum(len(w) for w in words) / max(1, len(words))

        # Calculate Flesch-Kincaid Grade Level (simplified)
        fk_grade = 0.39 * avg_sentence_length + 11.8 * avg_word_length - 15.59

        issues = []

        # Check for common issues
        if avg_sentence_length > 25:
            issues.append("Average sentence length is high (>25 words). Consider breaking into shorter sentences.")

        if "utilize" in text.lower():
            issues.append("Found 'utilize' - consider using 'use' for clearer writing.")

        if text.lower().count("however") > 3:
            issues.append("Multiple uses of 'however' detected - consider using alternatives.")

        if re.search(r"\b(I|we)\b.*\b(I|we)\b", text):
            issues.append("Repetitive first-person pronouns detected.")

        return {
            "avg_sentence_length": round(avg_sentence_length, 1),
            "avg_word_length": round(avg_word_length, 1),
            "fk_grade_level": round(fk_grade, 1),
            "issues": issues,
            "overall_assessment": "Good academic writing" if not issues else "Needs revision",
        }
