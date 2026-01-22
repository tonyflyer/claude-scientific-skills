# Integration Workflows

Complete workflows showing how to combine paper-validator with other Claude Scientific Skills for comprehensive paper review and improvement.

---

## Overview

Paper-validator works best as part of an integrated workflow with other skills. This document provides detailed examples of multi-skill workflows for common research tasks.

**Core Skills Ecosystem:**
- `arxiv-database` - Search and fetch papers, extract structure
- `paper-validator` - Systematic quality checking and issue identification
- `peer-review` - Comprehensive review generation
- `literature-review` - Related work analysis and positioning
- `scientific-critical-thinking` - Claims and evidence evaluation
- `scientific-writing` - Content improvement and synthesis

---

## Workflow 1: Complete Paper Review

**Goal**: Perform a comprehensive review of your draft paper before submission.

### Steps

#### 1. Extract Paper Structure (arxiv-database)

```markdown
Use arxiv-database to parse your paper and extract structure.

Command:
python paper_structure_extractor.py \
    --input my_paper.pdf \
    --output paper_structure.json \
    --format json
```

**Output**: Structured JSON with sections, paragraphs, figures, tables, citations.

#### 2. Systematic Validation (paper-validator)

```markdown
Use paper-validator to identify issues across six review areas.

Prompt:
"Use paper-validator skill to validate my paper. Here's the paper content:
[paste paper text or provide file path]

Focus on:
- Arguments (logical gaps, unsupported claims)
- Clarity (ambiguous terms, undefined jargon)
- Evidence (missing baselines, significance tests)
- Alternatives (unexamined assumptions)
- Novelty (unclear contributions)
- Confusion (poor organization, notation issues)"
```

**Output**: Structured list of issues by severity (major, moderate, minor) and category.

**Example Output**:
```
## Major Issues (2)
1. Missing statistical significance tests in Table 2
2. No comparison with recent state-of-the-art (2023-2024)

## Moderate Issues (5)
1. Inconsistent terminology ("model" vs "method" vs "system")
2. Vague quantifiers (6 instances: "large", "many", "significant")
...
```

#### 3. Comprehensive Peer Review (peer-review)

```markdown
Use peer-review skill for detailed review with constructive feedback.

Prompt:
"Use peer-review skill to generate a comprehensive review of my paper
for [target venue, e.g., NeurIPS 2024].

Paper title: [Your Title]
Target venue: NeurIPS 2024
Focus areas: novelty, experimental rigor, clarity"
```

**Output**: Full peer review with scores, strengths, weaknesses, questions.

#### 4. Address Issues (scientific-writing)

```markdown
Use scientific-writing skill to improve identified issues.

Prompt:
"Use scientific-writing skill to help me address these issues from
paper-validator:
1. Replace vague quantifier 'large dataset' with specific number
2. Define acronym 'OOD' on first use
3. Improve clarity of Section 3.2

Original text: [paste relevant sections]"
```

**Output**: Improved text with specific fixes.

#### 5. Re-validate

```markdown
After making changes, run paper-validator again to ensure issues are fixed.

Prompt:
"Use paper-validator to validate my revised paper and confirm that
previous issues have been addressed."
```

**Output**: Updated validation showing remaining issues (should be fewer).

---

## Workflow 2: Literature Review Paper

**Goal**: Write a comprehensive literature review paper with proper positioning and critical analysis.

### Steps

#### 1. Search Literature (arxiv-database)

```markdown
Use arxiv-database to find and fetch relevant papers.

Prompt:
"Use arxiv-database to search for papers on 'attention mechanisms for
medical image segmentation' from 2020-2024. Fetch the top 20 most
cited papers and extract their abstracts, methods, and results."
```

**Output**: Collection of relevant papers with structured information.

#### 2. Analyze Related Work (literature-review)

```markdown
Use literature-review skill to analyze the field and identify gaps.

Prompt:
"Use literature-review skill to analyze these 20 papers on attention
mechanisms for medical imaging. Identify:
- Main approaches and trends
- Research gaps
- Opportunities for contribution
- How to position my work"
```

**Output**: Comprehensive analysis with positioning recommendations.

#### 3. Draft Paper (scientific-writing)

```markdown
Use scientific-writing skill to draft the paper.

Prompt:
"Use scientific-writing skill to help me draft a literature review on
attention mechanisms for medical imaging. Include:
- Taxonomy of approaches
- Critical comparison
- Identified gaps
- Future directions"
```

**Output**: Draft literature review paper.

#### 4. Validate Draft (paper-validator)

```markdown
Use paper-validator to check quality before submission.

Prompt:
"Use paper-validator to validate my literature review draft. Pay special
attention to:
- Citation completeness
- Logical structure
- Balanced coverage
- Clear taxonomy"
```

**Output**: Issues identified across six review areas.

#### 5. Critical Thinking Check (scientific-critical-thinking)

```markdown
Use scientific-critical-thinking to verify claims and arguments.

Prompt:
"Use scientific-critical-thinking skill to evaluate the claims in my
literature review:
1. 'Deep learning has solved medical image segmentation'
2. 'Attention mechanisms always improve performance'
3. 'Transformer architectures are superior to CNNs'

Identify overgeneralizations, unsupported claims, or logical fallacies."
```

**Output**: Critical analysis of claims with recommendations.

#### 6. Final Polish (scientific-writing + paper-validator)

```markdown
Iterate between scientific-writing (for improvements) and paper-validator
(for verification) until all issues resolved.
```

---

## Workflow 3: Quick Paper Check Before Submission

**Goal**: Quick validation pass on nearly-complete paper.

### Fast 30-Minute Workflow

#### 1. Pattern Detection (paper-validator)

```markdown
Prompt:
"Use paper-validator to run pattern detection on my paper:
- Undefined acronyms
- Inconsistent terminology
- Vague quantifiers
- Passive voice overuse
- Missing citations

Here's my paper: [paste text]"
```

**Time**: 5 minutes
**Output**: List of patterns found

#### 2. Structure Check (paper-validator)

```markdown
Prompt:
"Use paper-validator to check my paper structure:
- Does abstract follow best practices?
- Are contributions clearly stated in introduction?
- Are methods reproducible?
- Do results include statistical tests?
- Are limitations discussed?"
```

**Time**: 10 minutes
**Output**: Structural issues identified

#### 3. Priority Fixes (scientific-writing)

```markdown
Focus only on major issues identified.

Prompt:
"Use scientific-writing to fix these major issues:
1. [Issue 1]
2. [Issue 2]
3. [Issue 3]"
```

**Time**: 15 minutes
**Output**: Fixed text for major issues

---

## Workflow 4: Responding to Peer Reviews

**Goal**: Address reviewer comments systematically.

### Steps

#### 1. Analyze Review (scientific-critical-thinking)

```markdown
Prompt:
"Use scientific-critical-thinking to analyze this reviewer comment:

'The paper claims significant improvement but Table 2 shows only 0.4%
difference without error bars or statistical tests.'

Help me understand:
- Is the criticism valid?
- What evidence would address it?
- How should I respond?"
```

**Output**: Analysis of criticism and response strategy.

#### 2. Add Missing Evidence

```markdown
Run additional experiments if needed, then use scientific-writing to
integrate results.

Prompt:
"Use scientific-writing to integrate these new experimental results
into my paper:

New data: 94.7 ± 0.3% (ours) vs 94.3 ± 0.4% (baseline), p < 0.01

Original text: [paste Section 4.2]
Help me revise to include statistical significance tests."
```

#### 3. Validate Changes (paper-validator)

```markdown
Prompt:
"Use paper-validator to verify that my revisions address the reviewer's
concern about statistical significance. Check that:
- Error bars are present in tables
- P-values are reported
- Claims are appropriately hedged"
```

#### 4. Draft Response Letter (scientific-writing)

```markdown
Prompt:
"Use scientific-writing to help me draft a response to this reviewer
comment. Be professional, acknowledge valid points, explain changes made."
```

---

## Workflow 5: Multi-Paper Comparison Study

**Goal**: Compare your work against recent papers systematically.

### Steps

#### 1. Fetch Comparison Papers (arxiv-database)

```markdown
Prompt:
"Use arxiv-database to fetch these papers for comparison:
- TransUNet (arXiv:2102.04306)
- Attention U-Net (arXiv:1804.03999)
- MedSegFormer (arXiv:2401.12345)

Extract their: methods, results on Synapse dataset, computational costs."
```

#### 2. Systematic Comparison (literature-review)

```markdown
Prompt:
"Use literature-review to create a systematic comparison table of these
methods:
- Architecture type
- Attention mechanism (if any)
- Performance on Synapse (Dice score)
- Parameters (millions)
- Inference time

Identify where my method fits in this landscape."
```

#### 3. Position Your Work (scientific-writing)

```markdown
Prompt:
"Use scientific-writing to draft a related work section that positions
my method relative to these baselines. Highlight:
- What my method does differently
- Why those differences matter
- Where my method excels
- Known limitations"
```

#### 4. Validate Positioning (paper-validator)

```markdown
Prompt:
"Use paper-validator to check my related work section for:
- Clear differentiation from prior work
- Fair comparison
- Accurate citations
- Appropriate claims (not overclaimed, not undersold)"
```

---

## Workflow 6: Improving Paper Clarity

**Goal**: Make paper more readable and accessible.

### Steps

#### 1. Identify Clarity Issues (paper-validator)

```markdown
Prompt:
"Use paper-validator to identify all clarity issues in my paper:
- Ambiguous pronouns
- Undefined technical terms
- Inconsistent terminology
- Complex sentences
- Missing intuitive explanations"
```

**Output**: List of specific clarity problems with locations.

#### 2. Simplify Writing (scientific-writing)

```markdown
For each issue, use scientific-writing to improve clarity.

Example prompt:
"Use scientific-writing to improve this paragraph for clarity:

Original: 'The model employs a mechanism that leverages spatial and
channel-wise attention which enables it to focus on relevant features
while suppressing irrelevant ones thereby improving performance.'

Make it clearer, break into multiple sentences if needed, define terms."
```

**Output**:
```
"The model uses a dual attention mechanism. Spatial attention identifies
important locations in the image. Channel attention weights relevant
feature channels. Together, these mechanisms help the model focus on
informative features while ignoring noise, improving segmentation accuracy."
```

#### 3. Add Intuitive Explanations (scientific-writing)

```markdown
Prompt:
"Use scientific-writing to add an intuitive explanation before the
mathematical formulation in Section 3.1.

Current: [starts with equations]

Add: Simple explanation + concrete example + then formalize"
```

#### 4. Verify Improvements (paper-validator)

```markdown
Prompt:
"Use paper-validator to check if clarity has improved:
- Are technical terms now defined?
- Are sentences clearer?
- Is the flow more logical?"
```

---

## Workflow 7: Conference-Specific Preparation

**Goal**: Tailor paper to specific venue requirements.

### Steps

#### 1. Understand Venue Standards (arxiv-database)

```markdown
Prompt:
"Use arxiv-database to fetch 5 recent accepted papers from NeurIPS 2023:
- Search: 'cat:cs.LG venue:NeurIPS 2023'
- Extract: structure, writing style, experimental setup standards"
```

#### 2. Compare Against Standards (paper-validator)

```markdown
Prompt:
"Use paper-validator to check if my paper meets NeurIPS standards based
on these examples:
- Are experiments comprehensive enough?
- Is statistical rigor sufficient?
- Is novelty clearly stated?
- Are baselines appropriate?"
```

#### 3. Adjust to Venue (scientific-writing)

```markdown
Prompt:
"Use scientific-writing to help me adjust my paper for NeurIPS:
- Add theoretical analysis (NeurIPS values theory)
- Expand ablation studies (NeurIPS requires thorough ablations)
- Strengthen baselines (NeurIPS expects strong comparisons)"
```

---

## Workflow 8: Addressing Specific Review Areas

### Focus on Arguments

```markdown
1. Identify argument issues (paper-validator):
   "Check for logical gaps, unsupported claims, missing evidence"

2. Evaluate claims (scientific-critical-thinking):
   "Evaluate whether each main claim is sufficiently supported"

3. Add supporting evidence (scientific-writing):
   "Help me add evidence for this claim: [specific claim]"

4. Verify logic (paper-validator):
   "Check if logical gaps have been filled"
```

### Focus on Evidence

```markdown
1. Check evidence (paper-validator):
   "Identify missing: baselines, significance tests, ablations, error bars"

2. Plan experiments:
   "What additional experiments would address these gaps?"

3. Integrate results (scientific-writing):
   "Help me add these new results to my paper: [data]"

4. Verify completeness (paper-validator):
   "Check if experimental validation is now sufficient"
```

### Focus on Novelty

```markdown
1. Check contribution clarity (paper-validator):
   "Is my contribution clearly stated and differentiated?"

2. Position against related work (literature-review):
   "How does my work differ from [specific prior work]?"

3. Improve contribution statement (scientific-writing):
   "Help me rewrite my contributions to be more specific"

4. Verify positioning (paper-validator):
   "Is novelty now clear and appropriately claimed?"
```

---

## Best Practices for Multi-Skill Workflows

### 1. Start with Validation

Always run paper-validator first to identify issues before attempting fixes.

**Why**: Saves time by focusing efforts on actual problems.

### 2. Iterate

Don't expect perfection in one pass. Cycle through:
```
validate → fix → validate → fix → ...
```

### 3. Use Right Tool for Each Job

| Task | Best Skill |
|------|-----------|
| Find issues | paper-validator |
| Fix writing | scientific-writing |
| Analyze related work | literature-review |
| Evaluate claims | scientific-critical-thinking |
| Generate reviews | peer-review |
| Search papers | arxiv-database |

### 4. Track Progress

Keep a checklist of issues to address:
```
Major Issues:
- [ ] Add statistical tests (Section 4.2)
- [ ] Include recent baselines (Section 5)

Moderate Issues:
- [ ] Fix terminology (global)
- [ ] Replace vague quantifiers (6 instances)
...
```

### 5. Prioritize

Address issues in order:
1. Major (blocking) issues
2. Moderate (important) issues
3. Minor (polish) issues

### 6. Document Changes

Keep track of what you've fixed for your response letter:
```
Reviewer 1, Comment 2:
- Issue: Missing statistical tests
- Action: Added 5-run experiments, p-values in Table 2
- Result: Now shows p < 0.01 for main results
- Location: Section 4.2, Table 2
```

---

## Common Workflow Patterns

### Pattern 1: Issue Detection → Fix → Verification

```
paper-validator (detect) →
scientific-writing (fix) →
paper-validator (verify)
```

### Pattern 2: Research → Write → Validate

```
arxiv-database (research) →
scientific-writing (draft) →
paper-validator (check) →
scientific-writing (revise)
```

### Pattern 3: Review → Response → Revision

```
peer-review (understand criticism) →
scientific-critical-thinking (evaluate validity) →
scientific-writing (address concerns) →
paper-validator (verify fixes)
```

### Pattern 4: Comprehensive Quality Check

```
arxiv-database (extract structure) →
paper-validator (find issues) →
peer-review (detailed review) →
scientific-critical-thinking (evaluate claims) →
scientific-writing (improve) →
paper-validator (final check)
```

---

## Integration Examples by Research Stage

### Early Draft Stage
- ✅ Use scientific-writing to create initial draft
- ✅ Use paper-validator for structure check
- ⏸️ Too early for detailed validation

### Mid-Stage (Content Complete)
- ✅ Use paper-validator for comprehensive check
- ✅ Use literature-review to strengthen related work
- ✅ Use scientific-critical-thinking to verify claims
- ✅ Use scientific-writing to address major issues

### Pre-Submission Stage
- ✅ Use paper-validator for final validation
- ✅ Use peer-review for mock review
- ✅ Use scientific-writing for polish
- ✅ Focus on major and moderate issues

### Post-Review Stage
- ✅ Use scientific-critical-thinking to evaluate reviewer feedback
- ✅ Use scientific-writing to address concerns
- ✅ Use paper-validator to verify changes
- ✅ Track all changes for response letter

---

## Time Estimates

| Workflow | Duration | When to Use |
|----------|----------|-------------|
| Quick validation | 30 min | Before submission |
| Comprehensive review | 2-3 hours | Mid-stage draft |
| Literature review | 3-4 hours | Early stage |
| Revision cycle | 1-2 hours | Addressing reviews |
| Clarity improvement | 1-2 hours | Anytime |
| Evidence strengthening | 2-4 hours | Mid-to-late stage |

---

## Troubleshooting

### "Too many issues identified"
- Focus on major issues first
- Address moderate issues in batches
- Minor issues can wait until final polish

### "Issues persist after fixing"
- Re-read validation output carefully
- Use scientific-writing for specific fixes
- Verify you've addressed root cause, not symptom

### "Unclear how to fix an issue"
- Ask scientific-critical-thinking for analysis
- Look at example_validation_report.md for patterns
- Check writing_standards.md for guidelines

### "Skills giving conflicting advice"
- paper-validator identifies issues (objective)
- scientific-writing suggests fixes (subjective)
- You make final decision based on context
- When in doubt, ask scientific-critical-thinking

---

## Advanced Workflows

### Workflow: Collaborative Paper Writing

When multiple authors are involved:

1. **Structure agreement** (paper-validator)
   - Validate outline before writing
   - Ensure all sections planned

2. **Parallel writing** (scientific-writing)
   - Different authors draft different sections

3. **Integration** (scientific-writing)
   - Merge sections, ensure consistency

4. **Unified validation** (paper-validator)
   - Check entire paper for consistency
   - Identify terminology conflicts

5. **Iterative improvement** (scientific-writing + paper-validator)
   - Fix identified issues
   - Re-validate until clean

### Workflow: Paper Comparison for Grant Application

When you need to compare your papers for impact assessment:

1. **Fetch your papers** (arxiv-database)
   - Extract structure and metrics from all your papers

2. **Compare positioning** (literature-review)
   - How do your papers build on each other?
   - What's the research trajectory?

3. **Synthesize impact** (scientific-writing)
   - Draft impact statement
   - Highlight progression and cumulative contributions

---

## Conclusion

These workflows demonstrate how paper-validator integrates with other Claude Scientific Skills to provide comprehensive paper review and improvement capabilities. The key is to:

1. **Use paper-validator for systematic issue detection**
2. **Combine with other skills for comprehensive analysis**
3. **Iterate between validation and improvement**
4. **Focus on high-priority issues first**
5. **Track progress throughout**

For more details on specific skills, see their respective SKILL.md files.

---

**Next Steps**:
- Try Workflow 1 (Complete Paper Review) on your current draft
- Adapt workflows to your specific needs
- Combine skills flexibly based on your goals
- Use paper-validator regularly throughout paper development

**Questions?** Each skill has comprehensive documentation in its SKILL.md file.
