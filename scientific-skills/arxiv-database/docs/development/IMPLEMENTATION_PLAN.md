# Implementation Plan - Following claude-writer Insights

**Date:** 2026-01-22
**Status:** 🟢 In Progress
**Based on:** CLAUDE_WRITER_ANALYSIS.md

---

## Decision: comprehensive_review.py Approach

**Selected:** Option B - Simplify to Structure Extractor

### Rationale

✅ **Keep what's valuable:**
- Parsing functionality (DOCX, PDF) - already refactored to review/parsers.py
- Structure extraction (sections, figures, tables, references)
- Useful foundation for other skills

❌ **Remove what's broken:**
- Hardcoded evaluation logic
- Fake scoring/grading
- Review generation with template values
- Literature comparison (incomplete)

### Implementation Strategy

```
comprehensive_review.py transformation:
├── REMOVE: ComprehensiveReviewWorkflow class
├── REMOVE: All evaluation/scoring methods
├── REMOVE: Review generation logic
├── KEEP: CLI interface for structure extraction
├── SIMPLIFY: Use review/parsers.py modules
└── RENAME: To paper_structure_extractor.py
```

---

## Phase 1: Simplify arxiv-database (Week 1)

### 1.1 Simplify comprehensive_review.py ✅

**Actions:**
- [ ] Rename to `paper_structure_extractor.py`
- [ ] Remove all evaluation classes and methods
- [ ] Remove literature comparison classes
- [ ] Keep only: CLI + parser orchestration
- [ ] Update imports to use review/parsers.py
- [ ] Update help text and documentation

**Target Line Count:** 2065 lines → ~300 lines (85% reduction)

**New Functionality:**
```bash
# Simple structure extraction
python scripts/paper_structure_extractor.py paper.pdf --output structure.json

# Output: Clean JSON with sections, figures, tables, references
{
  "metadata": {...},
  "sections": {...},
  "figures": [...],
  "tables": [...],
  "references": [...]
}
```

### 1.2 Update arxiv-database SKILL.md

**Changes:**
- [ ] Remove "Comprehensive Paper Review" feature
- [ ] Add "Paper Structure Extraction" feature
- [ ] Update description: Focus on search/retrieval + parsing
- [ ] Add collaboration examples with peer-review skill
- [ ] Update use cases to reflect new boundaries
- [ ] Add reference to peer-review and paper-validator skills

### 1.3 Add LaTeX Parser

**Implementation:**
- [ ] Create `LatexParser` class in review/parsers.py
- [ ] Dependencies: Add `pylatexenc>=2.10` to pyproject.toml
- [ ] Extract: sections, equations, figures, tables, references
- [ ] Preserve: Formatting information
- [ ] Handle: Common LaTeX packages (amsmath, graphicx, etc.)

---

## Phase 2: Create peer-review Skill (Week 2)

### 2.1 Create Skill Directory Structure

```
scientific-skills/peer-review/
├── SKILL.md                    # Skill specification
├── pyproject.toml              # No additional dependencies
├── references/
│   ├── review_standards.md     # CS conference standards
│   ├── scoring_rubrics.md      # Evaluation criteria
│   └── examples/
│       ├── good_review.md      # Example of good review
│       └── bad_review.md       # Common mistakes
└── scripts/
    └── review_template.py      # Optional template generator
```

### 2.2 SKILL.md Content (Based on claude-writer)

**Frontmatter:**
```yaml
---
name: peer-review
description: Generate structured peer reviews for scientific papers with evidence-based evaluation and constructive feedback
license: MIT
metadata:
  version: 1.0.0
  author: K-Dense Inc.
  tags: [peer-review, scientific-writing, evaluation, feedback]
  requires: []
  suggests: [arxiv-database, paper-validator, scientific-critical-thinking]
---
```

**Core Features:**
1. Eight-part review structure
2. Evidence-based scoring (0-5 scale)
3. Constructive feedback framing
4. Specific strengths and weaknesses
5. Actionable recommendations
6. Confidence levels
7. Reviewer expertise declaration

**Workflow:**
```
1. Read paper structure (from arxiv-database)
2. Analyze methodology
3. Evaluate novelty
4. Assess evidence
5. Generate structured review
6. Assign scores with justification
7. Provide actionable feedback
```

### 2.3 Implementation Notes

**NOT hardcoded evaluations:**
- Use Claude's analysis capabilities
- Require evidence for every claim
- Generate scores based on explicit criteria
- Provide reasoning for recommendations

**Collaboration with other skills:**
- Input: StructuredPaperData from arxiv-database
- Collaborate: paper-validator for validation
- Collaborate: literature-review for context
- Output: Structured review document

---

## Phase 3: Create paper-validator Skill (Week 3)

### 3.1 Create Skill Directory Structure

```
scientific-skills/paper-validator/
├── SKILL.md
├── pyproject.toml
├── references/
│   ├── validation_criteria.md
│   ├── common_issues.md
│   └── writing_standards.md
└── scripts/
    └── validation_checklist.py
```

### 3.2 SKILL.md Content (Based on claude-writer)

**Six Core Principles:**
1. Clarity and Precision
2. Fluency
3. Appropriate Vocabulary
4. Logical Cohesion
5. Format Integrity (LaTeX, DOCX, etc.)
6. Constructive Framing

**Six Key Review Areas:**
1. Arguments - Logical gaps, weak reasoning
2. Clarity - Ambiguous sentences, undefined jargon
3. Evidence - Missing benchmarks, validation
4. Alternatives - Counterarguments, assumptions
5. Novelty - Contributions, differentiation
6. Confusion - Structural issues, missing context

**Systematic Workflow:**
```
1. Read files
2. Search for patterns
   - Undefined acronyms
   - Passive voice overuse
   - Inconsistent terminology
3. Analyze structure
4. Identify issues by area
5. Provide consolidated feedback
```

### 3.3 Writing Standards Enforced

| Aspect | Standard |
|--------|----------|
| Hyphenation | Avoid for independent clauses; use in compound adjectives |
| Voice | Active preferred; passive when object matters more |
| Tense | Present for contributions; past for prior literature |
| Acronyms | Define on first occurrence |
| Conciseness | Eliminate redundancy |

---

## Phase 4: Update marketplace.json (Week 4)

### 4.1 Add New Skills

```json
{
  "metadata": {
    "version": "2.18.0"  // Increment version
  },
  "plugins": [{
    "skills": [
      // ... existing skills ...
      "scientific-skills/peer-review",
      "scientific-skills/paper-validator"
    ]
  }]
}
```

### 4.2 Update arxiv-database Entry

Ensure arxiv-database description reflects new boundaries:
```json
{
  "path": "scientific-skills/arxiv-database",
  "description": "Search, retrieve, and parse papers from arXiv. Extracts structured data including sections, figures, tables, and references. Works with DOCX, PDF, and LaTeX formats."
}
```

---

## Success Metrics

### Code Quality

| Metric | Before | Target | Status |
|--------|--------|--------|--------|
| comprehensive_review.py lines | 2065 | ~300 | 🔶 Pending |
| Max file size in project | 2065 | <500 | 🔶 Pending |
| Hardcoded evaluations | Yes | None | 🔶 Pending |
| Skills separation | 1 monolithic | 3 focused | 🔶 Pending |
| LaTeX support | No | Yes | 🔶 Pending |

### Skill Ecosystem

| Aspect | Before | Target | Status |
|--------|--------|--------|--------|
| arxiv-database focus | Mixed | Search/retrieval | 🔶 Pending |
| Peer review quality | Hardcoded | Real evaluation | 🔶 Pending |
| Paper validation | None | Systematic | 🔶 Pending |
| Collaboration examples | None | 3+ workflows | 🔶 Pending |

---

## Testing Plan

### Phase 1 Tests
- [ ] Test paper_structure_extractor.py with DOCX files
- [ ] Test paper_structure_extractor.py with PDF files
- [ ] Test paper_structure_extractor.py with LaTeX files
- [ ] Verify JSON output structure
- [ ] Test error handling

### Phase 2 Tests
- [ ] Test peer-review skill with sample papers
- [ ] Verify review structure (8 parts)
- [ ] Check evidence-based scoring
- [ ] Test constructive feedback quality
- [ ] Integration with arxiv-database

### Phase 3 Tests
- [ ] Test paper-validator with sample papers
- [ ] Verify all 6 validation areas
- [ ] Check pattern detection (acronyms, voice, etc.)
- [ ] Test LaTeX format preservation
- [ ] Integration with peer-review

---

## Risk Mitigation

### Risk 1: Breaking Changes for Existing Users
**Mitigation:**
- Keep comprehensive_review.py as deprecated but functional
- Add clear deprecation notice
- Provide migration guide
- Maintain backward compatibility for 1 version cycle

### Risk 2: New Skills Not Meeting Quality Standards
**Mitigation:**
- Extensive testing before release
- Beta phase with select users
- Iterate based on feedback
- Clear documentation of capabilities and limitations

### Risk 3: LaTeX Parsing Complexity
**Mitigation:**
- Start with common LaTeX patterns
- Document supported packages
- Graceful fallback to text extraction
- Iterative improvement based on real papers

---

## Timeline

### Week 1: Simplify arxiv-database
- Days 1-2: Simplify comprehensive_review.py → paper_structure_extractor.py
- Days 3-4: Add LaTeX parser
- Day 5: Update SKILL.md and tests

### Week 2: Create peer-review Skill
- Days 1-2: Create skill structure and SKILL.md
- Days 3-4: Create reference materials and examples
- Day 5: Testing and documentation

### Week 3: Create paper-validator Skill
- Days 1-2: Create skill structure and SKILL.md
- Days 3-4: Create validation criteria and standards
- Day 5: Testing and documentation

### Week 4: Integration and Testing
- Days 1-2: Update marketplace.json
- Days 3-4: Integration testing (multi-skill workflows)
- Day 5: Final documentation and release

---

## Next Actions

### Immediate (Today)
1. ✅ Create this implementation plan
2. 🔶 Read comprehensive_review.py in full
3. 🔶 Create paper_structure_extractor.py (simplified version)
4. 🔶 Update comprehensive_review.py deprecation notice

### This Week
5. 🔶 Add LaTeX parser to review/parsers.py
6. 🔶 Update arxiv-database SKILL.md
7. 🔶 Test simplified structure extractor
8. 🔶 Begin peer-review skill creation

---

## References

- **Analysis:** CLAUDE_WRITER_ANALYSIS.md
- **Strategy:** LONG_TERM_STRATEGY.md
- **Current Review:** REVIEW.md
- **Refactoring Progress:** REFACTORING_PROGRESS.md
- **claude-writer:** https://github.com/minhuw/claude-writer
