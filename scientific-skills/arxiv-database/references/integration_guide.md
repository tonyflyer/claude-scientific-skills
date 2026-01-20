# Integration Guide

## Overview

This guide explains how to integrate the arxiv-database skill with other skills in the claude-scientific-skills project.

## Integration Points

### 1. Peer Review Skill

Generate structured peer review reports using the peer-review skill.

```python
from arxiv_database.scripts.arxiv_client import ArxivSearcher
from arxiv_database.scripts.analysis.reviewer import PaperReviewer

# Get paper data
searcher = ArxivSearcher()
paper = searcher.get_paper("2401.12345")

# Generate review (integrates with peer-review skill)
reviewer = PaperReviewer()
review = reviewer.generate_review("2401.12345", paper)

# The review output is compatible with peer-review skill format
print(review["overall_assessment"]["summary"])
```

### 2. Citation Management Skill

Export citations for use with citation-management skill.

```python
from arxiv_database.scripts.arxiv_client import ArxivSearcher

searcher = ArxivSearcher()
paper = searcher.get_paper("2401.12345")

# Generate BibTeX citation
bibtex = searcher.generate_citation(paper, format="bibtex")

# Can be passed to citation-management skill
print(bibtex)
```

### 3. Scientific Writing Skill

Use paper analysis to support document generation.

```python
from arxiv_database.scripts.arxiv_client import ArxivSearcher
from arxiv_database.scripts.analysis.evaluator import PaperEvaluator

searcher = ArxivSearcher()
paper = searcher.get_paper("2401.12345")

# Evaluate paper
evaluator = PaperEvaluator()
evaluation = evaluator.evaluate(paper)

# Use in scientific writing context
# - Novelty points for related work
# - Methodology analysis for methods section
# - Key findings for results discussion
```

### 4. Hypothesis Generation Skill

Support research hypothesis development.

```python
from arxiv_database.scripts.arxiv_client import ArxivSearcher
from arxiv_database.scripts.analysis.extractor import PaperExtractor

# Search for related work
searcher = ArxivSearcher()
papers = searcher.search(query="novel approach", max_results=20)

# Extract key contributions
extractor = PaperExtractor()
for paper in papers["results"][:5]:
    extraction = extractor.extract(paper)
    # Use extracted information for hypothesis generation
```

## Workflow Templates

### Complete Research Workflow

```python
# 1. Literature Search
from arxiv_database.scripts.arxiv_client import ArxivSearcher

searcher = ArxivSearcher()
literature = searcher.search(
    query="transformer architecture",
    categories=["cs.LG", "cs.AI"],
    max_results=100
)

# 2. Deep Analysis
from arxiv_database.scripts.templates.deep_analysis import main as analyze

# 3. Peer Review
from arxiv_database.scripts.analysis.reviewer import PaperReviewer

reviewer = PaperReviewer()
for paper in literature["results"][:5]:
    review = reviewer.generate_review(paper["id"])

# 4. Citation Management
from arxiv_database.scripts.arxiv_client import ArxivSearcher

citations = []
for paper in literature["results"]:
    bibtex = searcher.generate_citation(paper, format="bibtex")
    citations.append(bibtex)
```

### Comparative Analysis Workflow

```python
from arxiv_database.scripts.arxiv_client import ArxivSearcher
from arxiv_database.scripts.analysis.evaluator import PaperEvaluator

searcher = ArxivSearcher()

# Get papers on similar topic
papers = searcher.search(
    query="image generation",
    categories=["cs.CV"],
    max_results=50
)["results"]

# Evaluate each paper
evaluator = PaperEvaluator()
evaluations = []
for paper in papers:
    eval_result = evaluator.evaluate(paper)
    eval_result["arxiv_id"] = paper["id"]
    eval_result["title"] = paper["title"]
    evaluations.append(eval_result)

# Compare
comparison = evaluator.compare_papers(evaluations)
print(comparison["ranking"])
```

## Error Handling

### Graceful Degradation

```python
from arxiv_database.scripts.arxiv_client import ArxivSearcher

searcher = ArxivSearcher()

try:
    paper = searcher.get_paper("2401.12345")
    if paper is None:
        print("Paper not found - trying alternative ID format")
        # Try without version
        paper = searcher.get_paper("2401.12345v1")
except Exception as e:
    print(f"Error retrieving paper: {e}")
    # Fallback to manual search
```

### Rate Limit Handling

The client automatically handles rate limits. For manual control:

```python
import time
from arxiv_database.scripts.arxiv_client import ArxivSearcher

searcher = ArxivSearcher(delay_seconds=5.0)  # Slower for sensitive operations

for paper_id in paper_ids:
    try:
        paper = searcher.get_paper(paper_id)
        process(paper)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        time.sleep(searcher.delay_seconds)  # Ensure delay between requests
```

## Output Formats

### JSON Output (Default)

```json
{
  "query": {"keywords": ["transformer"]},
  "result_count": 42,
  "results": [
    {
      "id": "2401.12345",
      "title": "...",
      "authors": ["..."],
      "abstract": "...",
      "categories": ["cs.LG"],
      "pdf_url": "..."
    }
  ]
}
```

### BibTeX Output

```bibtex
@article{Hinton2024,
  title = {Paper Title},
  author = {Hinton, Geoffrey},
  journal = {arXiv preprint},
  year = {2024},
  eprint = {2401.12345},
  url = {https://arxiv.org/abs/2401.12345}
}
```

### Markdown Report

Compatible with scientific-writing skill:

```markdown
# Paper Analysis

## Overview
- **Title:** Paper Title
- **Authors:** Author A, Author B
- **arXiv ID:** 2401.12345

## Innovation Assessment
- **Score:** 0.85
- **Key Contributions:**
  - Novel approach to X
  - Improved performance on Y

## Methodology
- Strength: Comprehensive experiments
- Weakness: Limited dataset
```
