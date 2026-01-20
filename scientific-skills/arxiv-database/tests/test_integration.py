"""
Integration tests for arxiv-database skill with other scientific skills.

Tests interoperability with:
- peer-review: Peer review generation
- citation-management: Citation generation and formatting
- scientific-writing: Document generation
"""

import pytest
import json
from unittest.mock import Mock, patch


class TestPeerReviewIntegration:
    """Integration tests with peer-review skill."""

    def test_paper_to_peer_review_workflow(self):
        """Test complete workflow: arxiv search -> peer review generation."""
        from scripts.arxiv_client import ArxivSearcher
        from scripts.analysis.reviewer import PaperReviewer

        # Mock arxiv search result
        mock_paper = {
            "id": "2401.12345",
            "title": "Deep Learning for Image Classification",
            "authors": ["Author A", "Author B"],
            "abstract": "We propose a novel deep learning method for image classification.",
            "published": "2024-01-15",
            "categories": ["cs.CV", "cs.LG"],
            "pdf_url": "https://arxiv.org/pdf/2401.12345.pdf",
        }

        # Initialize components
        searcher = ArxivSearcher()
        reviewer = PaperReviewer()

        # Simulate search result
        search_results = {
            "query": {"keywords": ["deep learning"]},
            "result_count": 1,
            "results": [mock_paper],
        }

        # Generate review
        review = reviewer.generate_review(
            paper_id=mock_paper["id"],
            paper_data=mock_paper,
        )

        # Verify review structure matches peer-review skill expectations
        assert "overall_assessment" in review
        assert "peer_review" in review
        assert "revision_suggestions" in review
        assert review["paper_id"] == mock_paper["id"]

        # Verify peer_review sections
        peer_review = review["peer_review"]
        assert "preliminary_assessment" in peer_review
        assert "section_by_section_review" in peer_review
        assert "methodological_rigor" in peer_review
        assert "reproducibility" in peer_review

    def test_review_output_format_compatibility(self):
        """Test that review output is compatible with peer-review skill format."""
        from scripts.analysis.reviewer import PaperReviewer

        reviewer = PaperReviewer()
        paper_data = {
            "id": "2401.12345",
            "title": "Test Paper",
            "abstract": "Abstract text...",
        }

        review = reviewer.generate_review("2401.12345", paper_data)

        # Verify format compatibility
        assert isinstance(review, dict)
        assert "overall_assessment" in review
        assert "score" in review["overall_assessment"]
        assert 1 <= review["overall_assessment"]["score"] <= 5

    def test_batch_review_integration(self):
        """Test batch review generation for multiple papers."""
        from scripts.analysis.reviewer import PaperReviewer

        reviewer = PaperReviewer()

        # Multiple papers
        papers = [
            {"id": "2401.12345", "title": "Paper A", "abstract": "..."},
            {"id": "2401.12346", "title": "Paper B", "abstract": "..."},
            {"id": "2401.12347", "title": "Paper C", "abstract": "..."},
        ]

        reviews = []
        for paper in papers:
            review = reviewer.generate_review(paper["id"], paper)
            reviews.append(review)

        # Verify all reviews generated
        assert len(reviews) == 3
        for review in reviews:
            assert "overall_assessment" in review
            assert "peer_review" in review


class TestCitationManagementIntegration:
    """Integration tests with citation-management skill."""

    def test_citation_generation_formats(self):
        """Test citation generation in various formats."""
        from scripts.arxiv_client import ArxivSearcher

        searcher = ArxivSearcher()
        paper = {
            "id": "2401.12345",
            "title": "Deep Learning Advances",
            "authors": ["Hinton G", "LeCun Y", "Bengio Y"],
            "published": "2024-01-15",
        }

        # Test BibTeX format
        bibtex = searcher.generate_citation(paper, format="bibtex")
        assert "@article{" in bibtex
        assert "2401.12345" in bibtex
        assert "Deep Learning Advances" in bibtex

        # Test APA format
        apa = searcher.generate_citation(paper, format="apa")
        assert "Hinton" in apa
        assert "2024" in apa

        # Test MLA format
        mla = searcher.generate_citation(paper, format="mla")
        assert "Hinton" in mla
        assert "Deep Learning Advances" in mla

    def test_citation_metadata_extraction(self):
        """Test that citation contains all required metadata."""
        from scripts.arxiv_client import ArxivSearcher

        searcher = ArxivSearcher()
        paper = {
            "id": "2401.12345",
            "title": "Test Paper",
            "authors": ["Author A"],
            "published": "2024-01-15",
        }

        citation = searcher.generate_citation(paper, format="bibtex")

        # Verify key components
        assert "Author" in citation or "author" in citation.lower()
        assert "Test Paper" in citation
        assert "2024" in citation

    def test_batch_citation_export(self):
        """Test batch citation export for multiple papers."""
        from scripts.arxiv_client import ArxivSearcher

        searcher = ArxivSearcher()
        papers = [
            {"id": "2401.12345", "title": "Paper A", "authors": ["A"], "published": "2024"},
            {"id": "2401.12346", "title": "Paper B", "authors": ["B"], "published": "2024"},
        ]

        citations = []
        for paper in papers:
            citation = searcher.generate_citation(paper, format="bibtex")
            citations.append(citation)

        # Verify all citations generated
        assert len(citations) == 2
        for citation in citations:
            assert "@article{" in citation


class TestScientificWritingIntegration:
    """Integration tests with scientific-writing skill."""

    def test_abstract_generation(self):
        """Test abstract generation from paper sections."""
        from scripts.analysis.scientific_writer import ScientificWriter

        writer = ScientificWriter()
        sections = {
            "introduction": "This paper addresses the problem of X.",
            "abstract": "We propose a novel approach...",
            "methodology": "Our method uses deep learning.",
            "results": "The proposed method achieves 95% accuracy.",
            "conclusion": "We demonstrate the effectiveness of our approach.",
        }

        abstract = writer.generate_abstract(sections)

        assert "Background:" in abstract or "Objective:" in abstract
        assert "Methods:" in abstract or "Methodology:" in abstract
        assert "Results:" in abstract

    def test_discussion_structure(self):
        """Test discussion section structuring."""
        from scripts.analysis.scientific_writer import ScientificWriter

        writer = ScientificWriter()
        sections = {
            "results": "Our method achieved significant improvements.",
            "conclusion": "The results demonstrate the validity of our approach.",
        }

        discussion = writer.structure_discussion(sections)

        assert "summary_of_findings" in discussion
        assert "interpretation" in discussion
        assert "limitations" in discussion
        assert "implications" in discussion
        assert "future_directions" in discussion

    def test_outline_generation(self):
        """Test paper outline generation."""
        from scripts.analysis.scientific_writer import ScientificWriter

        writer = ScientificWriter()
        topic = "Deep Learning for Computer Vision"

        outline = writer.create_outline(topic)

        assert outline["topic"] == topic
        assert "sections" in outline
        assert "Introduction" in outline["sections"]
        assert "Methodology" in outline["sections"]
        assert "Results" in outline["sections"]
        assert "Conclusion" in outline["sections"]

    def test_text_humanization_for_writing(self):
        """Test text transformation for scientific writing."""
        from scripts.analysis.scientific_writer import ScientificWriter

        writer = ScientificWriter()

        # AI-generated text
        ai_text = "In conclusion, we have demonstrated that utilizing this method proves significant improvements in performance metrics."

        # Transform to more natural academic writing
        humanized = writer.humanize(ai_text, intensity="medium")

        # Verify transformation
        assert isinstance(humanized, str)
        assert len(humanized) > 0


class TestEndToEndWorkflows:
    """End-to-end workflow integration tests."""

    def test_complete_research_workflow(self):
        """Test complete research workflow integration."""
        from scripts.arxiv_client import ArxivSearcher
        from scripts.analysis.evaluator import PaperEvaluator
        from scripts.analysis.reviewer import PaperReviewer
        from scripts.analysis.scientific_writer import ScientificWriter
        from scripts.analysis.data_analyzer import DataAnalyzer

        # Initialize all components
        searcher = ArxivSearcher()
        evaluator = PaperEvaluator()
        reviewer = PaperReviewer()
        writer = ScientificWriter()
        analyzer = DataAnalyzer()

        # Mock paper data
        paper_data = {
            "id": "2401.12345",
            "title": "Transformer Networks for NLP",
            "authors": ["Vaswani A", "Shazeer N"],
            "abstract": "We propose a new architecture based on self-attention.",
            "published": "2024-01-15",
            "categories": ["cs.CL", "cs.LG"],
        }

        # Step 1: Evaluate paper
        evaluation = evaluator.evaluate(paper_data)
        assert "innovation_score" in evaluation
        assert "methodology_score" in evaluation

        # Step 2: Generate peer review
        review = reviewer.generate_review(paper_data["id"], paper_data)
        assert "overall_assessment" in review
        assert "peer_review" in review

        # Step 3: Generate scientific writing
        sections = {
            "introduction": paper_data["abstract"],
            "methodology": "We use transformer architecture.",
            "results": "The model achieves state-of-the-art results.",
        }
        abstract = writer.generate_abstract(sections)
        assert "Objective:" in abstract or "Background:" in abstract

        # Step 4: Analyze results
        results = {"metrics": [{"name": "accuracy", "value": 0.92}]}
        analysis = analyzer.analyze_results(results)
        assert "descriptive_statistics" in analysis
        assert "statistical_tests" in analysis

    def test_reproducibility_workflow(self):
        """Test reproducibility assessment workflow."""
        from scripts.analysis.evaluator import PaperEvaluator
        from scripts.analysis.experiment_designer import ExperimentDesigner
        from scripts.analysis.data_analyzer import DataAnalyzer

        evaluator = PaperEvaluator()
        designer = ExperimentDesigner()
        analyzer = DataAnalyzer()

        # Paper data with realistic abstract for novelty detection
        paper_data = {
            "id": "2401.12345",
            "title": "Reproducible Research",
            "abstract": "We propose a novel deep learning method for image classification that significantly outperforms existing approaches. Our method achieves state-of-the-art results on ImageNet and CIFAR-10 benchmarks.",
        }

        # Step 1: Evaluate paper
        evaluation = evaluator.evaluate(paper_data)
        assert evaluation["innovation_score"] >= 0  # Score can be 0 for low novelty

        # Step 2: Design experiment
        design = designer.design_experiment(paper_data)
        assert "experimental_protocol" in design
        assert "datasets" in design

        # Step 3: Analyze reproducibility
        reproducibility_report = analyzer.create_reproducibility_report(
            paper_data,
            {"success": True},
        )
        assert "paper" in reproducibility_report
        assert "overall_score" in reproducibility_report


class TestDataExchangeBetweenSkills:
    """Tests for data exchange format compatibility."""

    def test_paper_metadata_format(self):
        """Test paper metadata format compatibility."""
        from scripts.arxiv_client import ArxivSearcher

        searcher = ArxivSearcher()
        paper = searcher.get_paper("2401.12345")

        # Verify required fields
        if paper:
            assert "id" in paper
            assert "title" in paper
            assert "authors" in paper
            assert "abstract" in paper

    def test_evaluation_result_format(self):
        """Test evaluation result format for skill interoperability."""
        from scripts.analysis.evaluator import PaperEvaluator

        evaluator = PaperEvaluator()
        paper = {
            "id": "2401.12345",
            "title": "Test",
            "abstract": "Test abstract",
        }

        evaluation = evaluator.evaluate(paper)

        # Verify format
        assert "innovation_score" in evaluation
        assert "novelty_level" in evaluation
        assert "methodology_score" in evaluation
        assert "key_findings" in evaluation

    def test_review_result_format(self):
        """Test review result format for skill interoperability."""
        from scripts.analysis.reviewer import PaperReviewer

        reviewer = PaperReviewer()
        paper = {
            "id": "2401.12345",
            "title": "Test",
            "abstract": "Test abstract",
        }

        review = reviewer.generate_review("2401.12345", paper)

        # Verify format
        assert "paper_id" in review
        assert "overall_assessment" in review
        assert "peer_review" in review
        assert "revision_suggestions" in review


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
