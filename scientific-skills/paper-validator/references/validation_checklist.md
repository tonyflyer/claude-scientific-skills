# Paper Validation Checklist

A comprehensive checklist for validating scientific papers before submission.

---

## Quick Reference

Use this checklist to systematically validate your paper across all six review areas.

### ☑️ Arguments

- [ ] All claims supported by evidence
- [ ] No logical fallacies present
- [ ] Causal links clearly established
- [ ] No overgeneralizations
- [ ] Assumptions explicitly stated
- [ ] Counter-arguments addressed

### ☑️ Clarity

- [ ] All technical terms defined
- [ ] Consistent terminology throughout
- [ ] No ambiguous sentences
- [ ] Clear pronoun references
- [ ] Quantifiers specific (not vague)
- [ ] Acronyms defined on first use

### ☑️ Evidence

- [ ] Sufficient experimental validation
- [ ] Appropriate baselines included
- [ ] Statistical significance tests reported
- [ ] Error bars / confidence intervals shown
- [ ] Ablation studies for key components
- [ ] Limitations discussed

### ☑️ Alternatives

- [ ] Alternative explanations considered
- [ ] Assumptions justified
- [ ] Failure cases discussed
- [ ] Competing approaches compared
- [ ] Generalization limits stated

### ☑️ Novelty

- [ ] Contributions clearly stated
- [ ] Differences from prior work explained
- [ ] Related work properly cited
- [ ] Novel aspects highlighted
- [ ] Incremental vs. breakthrough clear

### ☑️ Confusion

- [ ] Logical organization
- [ ] Definitions before use
- [ ] Intuitive examples provided
- [ ] Figures support understanding
- [ ] Consistent notation
- [ ] Smooth transitions

---

## Detailed Validation Guide

### 1. Pre-Validation Setup

**Before starting validation:**
- [ ] Have the complete paper available
- [ ] Access to cited references
- [ ] Understanding of target venue standards
- [ ] Knowledge of field conventions

**Recommended tools:**
- arxiv-database for fetching papers
- Reference manager for citations
- Spell/grammar checker
- LaTeX compiler (if applicable)

---

### 2. Pattern Detection Checklist

#### Undefined Acronyms
**Check for:**
- [ ] All acronyms defined on first occurrence
- [ ] Format: "Long Form (ACRONYM)"
- [ ] Not using acronym before definition
- [ ] Consistent usage after definition

**Common issues:**
```
❌ Bad: "We use GAN to generate images."
✅ Good: "We use Generative Adversarial Networks (GANs) to generate images."
```

#### Passive Voice Overuse
**Check for:**
- [ ] <30% of sentences in passive voice
- [ ] Active voice for your contributions
- [ ] Passive acceptable when object matters more
- [ ] Not obscuring the actor unnecessarily

**Examples:**
```
❌ Passive overuse: "Experiments were conducted and results were obtained."
✅ Active preferred: "We conducted experiments and obtained results."
✅ Passive OK: "Samples were collected from 10 sites." (method matters more)
```

#### Inconsistent Terminology
**Check for:**
- [ ] Single term for each concept
- [ ] No synonyms used interchangeably
- [ ] Consistent naming conventions
- [ ] Same term throughout paper

**Examples:**
```
❌ Inconsistent: "model", "system", "method" for same thing
✅ Consistent: Choose "method" and use throughout
```

#### Vague Quantifiers
**Check for:**
- [ ] Specific numbers instead of "many", "several", "few"
- [ ] Quantified "large", "small", "significant"
- [ ] Precise comparisons
- [ ] Concrete measurements

**Examples:**
```
❌ Vague: "We tested on a large dataset."
✅ Specific: "We tested on a dataset of 10 million samples."
```

#### Missing Citations
**Check for:**
- [ ] Claims backed by citations
- [ ] Prior work properly attributed
- [ ] Baseline methods cited
- [ ] Standard techniques referenced

---

### 3. Structure Validation

#### Abstract
- [ ] Self-contained (understandable alone)
- [ ] States problem clearly
- [ ] Describes approach
- [ ] Summarizes main results
- [ ] ~150-250 words
- [ ] No citations needed

#### Introduction
- [ ] Motivates the problem
- [ ] States research question
- [ ] Previews contributions (often numbered list)
- [ ] Outlines paper structure
- [ ] Engages reader interest

#### Related Work
- [ ] Comprehensive coverage of field
- [ ] Recent work included (last 2-3 years)
- [ ] Positioned appropriately (before or after methods)
- [ ] Fair comparison with prior work
- [ ] Clear differentiation of your contribution

#### Methods
- [ ] Detailed enough for reproduction
- [ ] Clear notation defined
- [ ] Algorithm pseudocode if appropriate
- [ ] Parameters specified
- [ ] Implementation details provided

#### Results
- [ ] Clear presentation (tables/figures)
- [ ] Statistical significance tests
- [ ] Error bars / confidence intervals
- [ ] Ablation studies
- [ ] Comparison with baselines

#### Discussion
- [ ] Interprets results
- [ ] Relates to research question
- [ ] Discusses implications
- [ ] Acknowledges limitations
- [ ] Suggests future work

#### Conclusion
- [ ] Summarizes contributions
- [ ] Restates key findings
- [ ] Discusses broader impact
- [ ] No new information introduced

---

### 4. Writing Quality Checklist

#### Hyphenation
- [ ] Compound adjectives hyphenated ("state-of-the-art")
- [ ] No hyphens between independent clauses
- [ ] Consistent style throughout

#### Voice
- [ ] Active voice for contributions (>70%)
- [ ] Passive acceptable for: standard procedures, when actor unimportant
- [ ] Clear subject in each sentence

#### Tense
- [ ] Present for your contributions
- [ ] Past for prior work
- [ ] Consistent within sections

#### Conciseness
- [ ] No unnecessary words
- [ ] "due to the fact that" → "because"
- [ ] "in order to" → "to"
- [ ] Redundancy eliminated

#### Clarity
- [ ] One idea per sentence
- [ ] Clear subject-verb-object
- [ ] No dangling modifiers
- [ ] Pronouns have clear antecedents

---

### 5. Figure and Table Checklist

#### Figures
- [ ] All figures referenced in text
- [ ] Captions self-explanatory
- [ ] Axes labeled with units
- [ ] Legends clear
- [ ] High resolution (300+ dpi for print)
- [ ] Colorblind-friendly palettes
- [ ] Font sizes readable

#### Tables
- [ ] All tables referenced in text
- [ ] Captions at top
- [ ] Headers clear
- [ ] Units specified
- [ ] Statistical significance indicated
- [ ] Aligned properly

#### Equations
- [ ] All variables defined
- [ ] Numbered if referenced
- [ ] Punctuation correct
- [ ] LaTeX compiles correctly

---

### 6. Citation and Reference Checklist

#### In-text Citations
- [ ] Proper format (e.g., [1] or (Author, Year))
- [ ] All claims cited appropriately
- [ ] Citations in order (if numbered)
- [ ] No broken references
- [ ] Consistent citation style

#### Reference List
- [ ] Complete information for each entry
- [ ] Consistent formatting
- [ ] All cited works included
- [ ] No uncited works listed
- [ ] Alphabetical or numerical order
- [ ] DOIs included when available

---

### 7. Domain-Specific Checklists

#### Computer Science
- [ ] Algorithm time/space complexity analyzed
- [ ] Code availability mentioned
- [ ] Reproducibility information provided
- [ ] Comparison with state-of-the-art
- [ ] Benchmarks standard in field

#### Life Sciences
- [ ] Sample size justified (power analysis)
- [ ] Statistical tests appropriate
- [ ] Controls included
- [ ] Ethics approval stated
- [ ] Data availability statement

#### Physics
- [ ] Units consistent and correct
- [ ] Error propagation calculated
- [ ] Theoretical predictions vs. experimental results
- [ ] Equipment specifications provided
- [ ] Calibration procedures described

#### Chemistry
- [ ] Chemical names IUPAC compliant
- [ ] Synthesis procedures detailed
- [ ] Characterization data complete (NMR, MS, etc.)
- [ ] Safety considerations noted
- [ ] Purity specifications provided

---

### 8. Pre-Submission Final Check

**24 hours before submission:**
- [ ] Fresh read-through (entire paper)
- [ ] All co-authors approved
- [ ] Formatting matches venue requirements
- [ ] Page limit satisfied
- [ ] Supplementary materials prepared
- [ ] Cover letter written
- [ ] Ethics/conflict of interest statements complete

**Common last-minute issues:**
- [ ] Broken LaTeX compilation
- [ ] Missing figures
- [ ] Incorrect author affiliations
- [ ] Abstract/keywords not matching
- [ ] References incomplete

---

## Validation Severity Levels

### 🔴 Major (Blocking)
Issues that prevent publication:
- Fundamental methodological flaws
- Unsupported main claims
- Missing critical experiments
- Logical inconsistencies
- Ethical violations

**Action:** Must fix before submission

### 🟡 Moderate (Important)
Issues that weaken the paper:
- Missing comparisons with important baselines
- Unclear explanations of key concepts
- Insufficient ablations
- Limited scope of evaluation
- Unclear novelty claims

**Action:** Should fix to strengthen paper

### 🟢 Minor (Polish)
Issues that improve quality:
- Typos and grammar
- Formatting inconsistencies
- Minor clarity improvements
- Better figure labels
- Citation formatting

**Action:** Fix if time permits

---

## Validation Workflow

### Sequential Validation
```
1. Pattern Detection (30 min)
   ↓
2. Structure Analysis (45 min)
   ↓
3. Content Review by Area (2-3 hours)
   ↓
4. Writing Quality (1 hour)
   ↓
5. Final Check (30 min)
```

### Parallel Validation (for teams)
```
Validator 1: Arguments + Evidence
Validator 2: Clarity + Confusion
Validator 3: Novelty + Alternatives
↓
Consolidate findings
↓
Prioritize issues
↓
Create revision plan
```

---

## Common Issues by Section

### Abstract
- ❌ Too vague ("we propose a novel method")
- ❌ No results mentioned
- ❌ Citations included
- ❌ Too long (>300 words)

### Introduction
- ❌ Doesn't motivate problem
- ❌ Contributions unclear
- ❌ No paper roadmap
- ❌ Too much related work

### Methods
- ❌ Not reproducible
- ❌ Missing parameters
- ❌ Unclear notation
- ❌ No algorithm description

### Results
- ❌ No statistical tests
- ❌ No error bars
- ❌ Cherry-picked data
- ❌ Unfair comparisons

### Conclusion
- ❌ New information introduced
- ❌ Overclaimed results
- ❌ No limitations mentioned
- ❌ Too brief

---

## Tools for Validation

### Automated Tools
- **Grammar/Spelling:** Grammarly, LanguageTool
- **Citations:** Zotero, Mendeley, BibTeX
- **LaTeX:** Overleaf, TeXstudio
- **Figures:** Matplotlib, ggplot2, Inkscape
- **Statistics:** R, Python (scipy, statsmodels)

### Manual Review
- **Peer review:** Colleagues, advisors
- **paper-validator skill:** Systematic validation
- **peer-review skill:** Mock reviews
- **scientific-critical-thinking skill:** Claims analysis

---

## Example Validation Report Structure

```markdown
# Validation Report: [Paper Title]

## Executive Summary
[2-3 sentences on overall quality and main issues]

## Major Issues (3 issues)
1. [Issue with specific reference to section/line]
2. [Issue with specific reference]
3. [Issue with specific reference]

## Moderate Issues (5 issues)
[List with specific references]

## Minor Issues (7 issues)
[Brief list or grouped categories]

## Strengths (3-5 points)
[What the paper does well]

## Validation Statistics
- Total issues: 15 (3 major, 5 moderate, 7 minor)
- Issues by area: Arguments (2), Clarity (4), Evidence (3), ...
- Sections with most issues: Methods (6), Results (4), ...

## Recommendation
[Ready / Needs Minor Revisions / Needs Major Revisions]
```

---

## Quick Tips

1. **Validate early and often** - Don't wait until submission deadline
2. **Start with major issues** - Fix blocking problems first
3. **Use automated tools** - Let computers handle syntax/style
4. **Get fresh eyes** - Have someone else read it
5. **Read aloud** - Catches awkward phrasing
6. **Check every figure** - Ensure all referenced and clear
7. **Verify all claims** - Evidence for each assertion
8. **Test reproducibility** - Can someone else follow your methods?
9. **Compare with venue standards** - Check recent accepted papers
10. **Budget time** - Validation takes 1-2 days minimum

---

## Resources

- **paper-validator skill:** Systematic validation workflow
- **peer-review skill:** Generate mock reviews
- **scientific-writing skill:** Fix identified issues
- **arxiv-database:** Fetch related papers for comparison

---

This checklist is part of the Claude Scientific Skills ecosystem.
Use `paper-validator` skill for systematic, automated validation.
