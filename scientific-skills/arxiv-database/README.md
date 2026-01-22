# arXiv Database Skill

A focused tool for searching, retrieving, and parsing papers from arXiv. Part of the [Claude Scientific Skills](https://github.com/K-Dense-AI/claude-scientific-skills) ecosystem.

## Quick Start

```bash
# Install dependencies
cd scientific-skills/arxiv-database
uv pip install -e .

# Search for papers
python scripts/search.py --query "transformer attention" --max-results 20 --output results.json

# Extract paper structure
python scripts/paper_structure_extractor.py arxiv:2401.12345 -o structure.json
```

## Advanced Workflow Examples

### Workflow 1: Systematic Literature Review

**Scenario:** You're writing a survey paper on "Large Language Models for Code Generation" and need to collect, organize, and analyze relevant papers.

```bash
# Step 1: Search arXiv for relevant papers
python scripts/search.py \
    --query "large language model code generation" \
    --category cs.CL \
    --days-back 365 \
    --max-results 100 \
    --output llm_code_papers.json

# Step 2: Filter by specific sub-topics
python scripts/search.py --query "copilot code completion" --output copilot_papers.json
python scripts/search.py --query "codex program synthesis" --output codex_papers.json

# Step 3: Download key papers for detailed analysis
python scripts/download.py --input llm_code_papers.json --output ./papers --limit 20

# Step 4: Extract structure from key papers
for pdf in papers/*.pdf; do
    python scripts/paper_structure_extractor.py "$pdf" -o "${pdf%.pdf}_structure.json"
done
```

**Next Steps (using other skills):**
- Use `literature-review` skill to deduplicate and organize results
- Use `citation-management` skill to generate BibTeX references
- Use `scientific-writing` skill to draft the survey

---

### Workflow 2: Conference Paper Review Preparation

**Scenario:** You're reviewing a paper submission and need to understand its context, find related work, and assess its novelty.

```bash
# Step 1: Parse the submitted paper
python scripts/paper_structure_extractor.py submission.pdf -o submission_structure.json -f json

# Step 2: Extract key concepts from the abstract
# (The structure.json contains metadata.abstract)

# Step 3: Search for related prior work
python scripts/search.py \
    --query "neural architecture search efficient" \
    --days-back 730 \
    --max-results 50 \
    --output related_work.json

# Step 4: Find papers by the same authors (check for self-citation)
python scripts/search.py \
    --author "Smith" \
    --start-date 2020-01-01 \
    --output author_papers.json

# Step 5: Check if similar titles exist
python scripts/search.py \
    --query "efficient neural architecture" \
    --search-fields title \
    --output similar_titles.json
```

**Next Steps (using other skills):**
- Use `paper-validator` skill to check clarity, evidence, and arguments
- Use `peer-review` skill to generate structured review with scores
- Use `scientific-critical-thinking` skill to assess evidence strength

---

### Workflow 3: Research Gap Analysis

**Scenario:** You're a PhD student exploring potential research directions in "Robotics + Reinforcement Learning".

```bash
# Step 1: Collect comprehensive literature
python scripts/search.py \
    --query "reinforcement learning robot manipulation" \
    --categories cs.RO cs.LG cs.AI \
    --max-results 200 \
    --output rl_robotics_all.json

# Step 2: Analyze by time period (identify trends)
python scripts/search.py \
    --query "reinforcement learning robot" \
    --start-date 2023-01-01 \
    --output rl_robotics_2023_2024.json

python scripts/search.py \
    --query "reinforcement learning robot" \
    --start-date 2021-01-01 \
    --end-date 2022-12-31 \
    --output rl_robotics_2021_2022.json

# Step 3: Focus on specific sub-areas
python scripts/search.py --query "sim-to-real transfer robot" --output sim2real.json
python scripts/search.py --query "offline reinforcement learning robot" --output offline_rl.json
python scripts/search.py --query "foundation model robot control" --output foundation_robot.json

# Step 4: Extract structures from seminal papers
python scripts/paper_structure_extractor.py arxiv:2301.xxxxx -o paper1_structure.json
python scripts/paper_structure_extractor.py arxiv:2305.xxxxx -o paper2_structure.json
```

**Next Steps (using other skills):**
- Use `literature-review` skill to identify themes and gaps
- Use `hypothesis-generation` skill to generate research hypotheses
- Use `research-lookup` skill to verify latest progress
- Use `scientific-writing` skill to draft research proposal

---

### Workflow 4: Multi-Format Paper Processing

**Scenario:** You have papers in different formats (PDF from arXiv, DOCX from collaborators, LaTeX source) and need unified structured data.

```bash
# Process PDF from arXiv
python scripts/paper_structure_extractor.py arxiv:2401.12345 -o arxiv_paper.json

# Process local PDF
python scripts/paper_structure_extractor.py ./local_paper.pdf -o local_paper.json

# Process DOCX (e.g., paper draft from Word)
python scripts/paper_structure_extractor.py ./draft.docx -o draft_structure.json

# Process LaTeX source (requires pylatexenc)
pip install pylatexenc>=2.10
python scripts/paper_structure_extractor.py ./paper.tex -o latex_paper.json

# Generate markdown reports for all
python scripts/paper_structure_extractor.py ./paper.pdf -o report.md -f markdown
```

**Output Structure (JSON):**
```json
{
  "metadata": {
    "title": "Paper Title",
    "authors": ["Author One", "Author Two"],
    "abstract": "Full abstract...",
    "arxiv_id": "2401.12345"
  },
  "sections": {
    "Introduction": {"title": "Introduction", "content": "...", "level": 1}
  },
  "figures": [{"number": "1", "caption": "..."}],
  "tables": [{"number": "1", "caption": "..."}],
  "references": [{"id": "1", "text": "...", "arxiv_id": "..."}]
}
```

---

### Workflow 5: Citation Network Exploration

**Scenario:** You found a key paper and want to explore its citation network (papers it cites and papers that cite it).

```bash
# Step 1: Get the key paper and extract its structure
python scripts/paper_structure_extractor.py arxiv:2301.00001 -o key_paper.json

# Step 2: The structure.json contains references with arxiv_ids
# Extract referenced arXiv papers programmatically

# Step 3: Search for papers by key authors from the reference list
python scripts/search.py --author "Vaswani" --output vaswani_papers.json
python scripts/search.py --author "Devlin" --output devlin_papers.json

# Step 4: Search for papers that likely cite this work (by title keywords)
python scripts/search.py \
    --query "attention is all you need transformer" \
    --start-date 2017-06-01 \
    --output citing_papers.json
```

---

### Workflow 6: Batch Processing for Meta-Analysis

**Scenario:** You need to extract data from 50+ papers for a meta-analysis.

```bash
# Step 1: Search and collect paper IDs
python scripts/search.py \
    --query "BERT fine-tuning benchmark" \
    --max-results 100 \
    --output bert_papers.json

# Step 2: Download all PDFs
python scripts/download.py \
    --input bert_papers.json \
    --output ./bert_pdfs \
    --limit 50

# Step 3: Batch extract structures (shell script)
mkdir -p structures
for pdf in bert_pdfs/*.pdf; do
    filename=$(basename "$pdf" .pdf)
    python scripts/paper_structure_extractor.py "$pdf" -o "structures/${filename}.json" 2>/dev/null
    echo "Processed: $filename"
done

# Step 4: Combine all structures for analysis
python -c "
import json
import glob

all_papers = []
for f in glob.glob('structures/*.json'):
    with open(f) as fp:
        all_papers.append(json.load(fp))

with open('combined_structures.json', 'w') as fp:
    json.dump(all_papers, fp, indent=2)
print(f'Combined {len(all_papers)} papers')
"
```

---

## Python API Usage

For programmatic access:

```python
from scripts.arxiv_client import ArxivSearcher
from scripts.review import PdfParser

# Search
searcher = ArxivSearcher(verbose=True)
results = searcher.search(
    query="attention mechanism",
    max_results=50,
    category="cs.LG"
)

# Download
for paper in results[:5]:
    searcher.download_pdf(paper['id'], f"papers/{paper['id']}.pdf")

# Parse
parser = PdfParser(verbose=True)
structure = parser.parse("papers/2401.12345.pdf")

# Access data
print(f"Title: {structure.metadata.title}")
print(f"Sections: {list(structure.sections.keys())}")
print(f"References: {len(structure.references)}")

# Generate citations
bibtex = searcher.generate_citation(results[0], format="bibtex")
apa = searcher.generate_citation(results[0], format="apa")
```

## Integration with Other Skills

| Your Goal | Use arxiv-database for | Then use |
|-----------|----------------------|----------|
| Write survey paper | Search & collect papers | `literature-review` → `scientific-writing` |
| Review a submission | Parse structure, find related work | `paper-validator` → `peer-review` |
| Find research gaps | Collect & analyze trends | `hypothesis-generation` |
| Prepare references | Search papers | `citation-management` |
| Deep paper analysis | Extract structure | `scientific-critical-thinking` |

## Resources

- **SKILL.md** - Complete skill specification and detailed documentation
- **scripts/** - Python scripts for search, download, and parsing
- **references/** - API documentation and query syntax guides
- **tests/** - Unit tests for validation

## License

MIT License - See LICENSE file for details.
