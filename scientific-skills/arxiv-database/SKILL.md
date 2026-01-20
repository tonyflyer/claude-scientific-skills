---
name: arxiv-database
description: Efficient database search tool for arXiv preprint server. Use this skill when searching for computer science, AI, automatic control, and other technology preprints by keywords, authors, date ranges, or categories, retrieving paper metadata, downloading PDFs, or conducting literature reviews.
license: MIT
metadata:
    skill-author: Claude AI Assistant
---

# arXiv Database

## Overview

This skill provides efficient Python-based tools for searching and retrieving preprints from the arXiv database. It enables comprehensive searches by keywords, authors, date ranges, and categories, returning structured JSON metadata that includes titles, abstracts, DOIs, and citation information. The skill also supports PDF downloads for full-text analysis and integrates with peer-review for structured paper evaluation.

## When to Use This Skill

Use this skill when:
- Searching for recent preprints in CS, AI, robotics, and control systems
- Tracking publications by particular authors
- Conducting systematic literature reviews in technology domains
- Analyzing research trends over time periods
- Retrieving metadata for citation management
- Downloading preprint PDFs for analysis
- Filtering papers by arXiv subject categories (cs.AI, cs.LG, stat.ML, etc.)

## Core Search Capabilities

### 1. Keyword Search

Search for preprints containing specific keywords in titles, abstracts, or author lists.

**Basic Usage:**
```python
python scripts/search.py --query "transformer attention" --max-results 50 --output results.json
```

**With Category Filter:**
```python
python scripts/search.py --query "reinforcement learning" --category cs.AI --days-back 180 --output recent_rl.json
```

**Search Fields:**
By default, keywords are searched in both title and abstract. Customize with `--search-fields`:
```python
python scripts/search.py --query "AlphaFold" --search-fields title --days-back 365
```

### 2. Author Search

Find all papers by a specific author within a date range.

**Basic Usage:**
```python
python scripts/search.py --author "Hinton" --start-date 2023-01-01 --output hinton_papers.json
```

**Recent Publications:**
```python
python scripts/search.py --author "LeCun" --days-back 365 --output lecun_recent.json
```

### 3. Category Search

Search by arXiv subject categories.

**Basic Usage:**
```python
python scripts/search.py --category cs.AI --max-results 100 --output ai_papers.json
```

**Multiple Categories:**
```python
python scripts/search.py --categories cs.AI cs.LG stat.ML --output ml_papers.json
```

### 4. Date Range Search

Retrieve all preprints posted within a specific date range.

**Basic Usage:**
```python
python scripts/search.py --start-date 2024-01-01 --end-date 2024-01-31 --output january_2024.json
```

### 5. Paper Details by ID

Retrieve detailed metadata for a specific preprint.

**Basic Usage:**
```python
python scripts/search.py --id 2401.12345 --output paper_details.json
```

### 6. PDF Downloads

Download the full-text PDF of any preprint.

**Basic Usage:**
```python
python scripts/download.py --id 2401.12345 --output paper.pdf
```

**Batch Processing:**
```python
python scripts/download.py --input results.json --output ./papers
```

## Valid Categories

Filter searches by arXiv subject categories:

**Computer Science:**
- `cs.AI` - Artificial Intelligence
- `cs.CL` - Computation and Language
- `cs.CV` - Computer Vision
- `cs.LG` - Machine Learning
- `cs.RO` - Robotics
- `cs.SY` - Systems and Control
- `cs.NE` - Neural and Evolutionary Computing

**Statistics:**
- `stat.ML` - Machine Learning
- `stat.TH` - Statistics Theory

**Physics:**
- `physics.flu-dyn` - Fluid Dynamics
- `physics.comp-ph` - Computational Physics

## Pre-built Workflow Templates

### 1. Quick Literature Review

Get a quick overview of papers in a research area:

```python
python scripts/templates/literature_review.py \
    --query "diffusion models image generation" \
    --years 2023-2025 \
    --max-papers 20 \
    --output literature_review.json
```

### 2. Deep Paper Analysis

Comprehensive analysis of a single paper:

```python
python scripts/templates/deep_analysis.py \
    --paper-id 2401.12345 \
    --output analysis_report.json
```

Includes:
- Metadata extraction
- Innovation assessment
- Methodology analysis
- Peer review generation

### 3. Paper Reproduction

Plan for reproducing paper experiments:

```python
python scripts/templates/reproduction.py \
    --paper-id 2401.12345 \
    --output reproduction_plan.json
```

### 4. Survey Generation

Generate a survey draft for a research topic:

```python
python scripts/templates/survey.py \
    --query "transformer architectures" \
    --years 2020-2025 \
    --max-papers 100 \
    --output survey_draft.md
```

## Output Format

All searches return structured JSON with the following format:

```json
{
  "query": {
    "keywords": ["transformer"],
    "start_date": "2024-01-01",
    "end_date": "2024-12-31",
    "categories": ["cs.AI"]
  },
  "result_count": 42,
  "results": [
    {
      "id": "2401.12345",
      "title": "Paper Title Here",
      "authors": ["Author A", "Author B"],
      "abstract": "Full abstract text...",
      "published": "2024-01-15",
      "updated": "2024-01-20",
      "categories": ["cs.AI", "cs.LG"],
      "pdf_url": "https://arxiv.org/pdf/2401.12345v1.pdf",
      "comment": "12 pages, 3 figures",
      "doi": "10.48550/arXiv.2401.12345"
    }
  ]
}
```

## Python API Usage

For more complex workflows, import and use the ArxivSearcher class directly:

```python
from scripts.arxiv_client import ArxivSearcher

# Initialize
searcher = ArxivSearcher(verbose=True)

# Keyword search
results = searcher.search(
    query="attention mechanism",
    max_results=100,
    category="cs.LG"
)

# Author search
author_results = searcher.search_author(
    author_name="Vaswani",
    start_date="2023-01-01"
)

# Download PDF
searcher.download_pdf("2401.12345", "paper.pdf")
```

## Integration with Other Skills

### Peer Review Integration

Generate structured peer review reports:

```python
from scripts.analysis.reviewer import PaperReviewer

reviewer = PaperReviewer()
review = reviewer.generate_review(paper_id="2401.12345")
```

### Citation Management

Export citations for use with citation-management skill:

```python
from scripts.arxiv_client import ArxivSearcher

searcher = ArxivSearcher()
paper = searcher.get_paper("2401.12345")
citation = searcher.generate_citation(paper, format="bibtex")
```

## Best Practices

1. **Use appropriate date ranges**: Smaller date ranges return faster.

2. **Filter by category**: When possible, use `--category` to reduce data transfer.

3. **Respect rate limits**: The script includes automatic delays. For large-scale data collection, add additional delays.

4. **Cache results**: Save search results to JSON files to avoid repeated API calls.

5. **Handle errors gracefully**: Check the `result_count` in output JSON.

6. **Verbose mode for debugging**: Use `--verbose` flag to see detailed logging.

## Testing the Skill

To verify that the arXiv database skill is working correctly, run the comprehensive test suite.

**Prerequisites:**
```bash
uv pip install -e ".[dev]"
```

**Run tests:**
```bash
python -m pytest tests/
```

The test suite validates:
- **Initialization**: ArxivSearcher class instantiation
- **Search Functionality**: Keyword, author, and category searches
- **Download**: PDF downloading functionality
- **Templates**: All workflow templates

## Reference Documentation

For detailed API specifications, endpoint documentation, and response schemas, refer to:
- `references/api_reference.md` - Complete API documentation
- `references/query_syntax.md` - arXiv query syntax guide
- `references/categories.md` - arXiv category reference
- `references/integration_guide.md` - Integration with other skills

## License

MIT License - See LICENSE file for details.
