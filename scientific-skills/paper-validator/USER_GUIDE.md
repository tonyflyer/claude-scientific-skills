# Paper Validator User Guide

Complete guide to using the paper-validator skill for systematic scientific paper validation.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [What is Paper Validator?](#what-is-paper-validator)
3. [When to Use](#when-to-use)
4. [How It Works](#how-it-works)
5. [Usage Examples](#usage-examples)
6. [Understanding Output](#understanding-output)
7. [Best Practices](#best-practices)
8. [Integration with Other Skills](#integration-with-other-skills)
9. [Troubleshooting](#troubleshooting)
10. [FAQ](#faq)

---

## Quick Start

### For Impatient Researchers

**Step 1**: Have your paper ready (PDF, DOCX, LaTeX, or plain text)

**Step 2**: Use paper-validator:
```markdown
"Use paper-validator skill to validate my paper.

[Paste paper content or provide file path]

Focus on major issues that would block publication."
```

**Step 3**: Review the output - you'll get:
- List of issues by severity (major, moderate, minor)
- Specific locations (sections, line numbers)
- Constructive questions for improvement
- Priority order for fixes

**Step 4**: Address major issues first, then moderate, then minor

**Step 5**: Re-validate after fixes to confirm improvements

**Time**: 30-60 minutes for complete validation + fixes

---

## What is Paper Validator?

### Purpose

paper-validator is a systematic quality checking tool for scientific papers. It identifies issues across six key review areas before submission, saving you from reviewer criticism.

### What It Does

✅ **Identifies Issues**:
- Logical gaps and weak reasoning
- Ambiguous or unclear writing
- Missing evidence or baselines
- Unexamined assumptions
- Unclear novelty claims
- Structural problems

✅ **Provides Constructive Feedback**:
- Questions that guide improvement
- Specific locations of issues
- Severity levels (major/moderate/minor)
- Examples of fixes

✅ **Saves Time**:
- Catches issues before submission
- Prevents reviewer criticism
- Focuses effort on real problems
- Systematic approach (nothing missed)

### What It Doesn't Do

❌ **Not a Reviewer**:
- Doesn't judge scientific merit
- Doesn't assess novelty impact
- Doesn't make accept/reject decisions
- → Use `peer-review` skill for comprehensive reviews

❌ **Not an Editor**:
- Doesn't rewrite text
- Doesn't fix issues automatically
- Doesn't generate content
- → Use `scientific-writing` skill for improvements

❌ **Not a Search Engine**:
- Doesn't fetch related papers
- Doesn't find citations
- Doesn't compare with literature
- → Use `arxiv-database` and `literature-review` skills

### Six Core Principles

paper-validator follows six core principles for quality assessment:

1. **Clarity and Precision**: Technical writing must be unambiguous
2. **Fluency**: Text should read naturally and smoothly
3. **Appropriate Vocabulary**: Use field-appropriate terminology
4. **Logical Cohesion**: Arguments connect without gaps
5. **Format Integrity**: LaTeX/formatting preserved
6. **Constructive Framing**: Feedback as questions, not criticism

### Six Review Areas

Issues are identified across six areas:

1. **Arguments**: Logical gaps, weak reasoning, unsupported claims
2. **Clarity**: Ambiguous statements, undefined jargon, vague terms
3. **Evidence**: Missing benchmarks, statistical tests, ablations
4. **Alternatives**: Unexamined assumptions, missing counterarguments
5. **Novelty**: Unclear contributions, missing differentiation
6. **Confusion**: Poor organization, missing context, notation issues

---

## When to Use

### Ideal Use Cases

✅ **Before Submission**:
- Final check before conference/journal submission
- Ensure no obvious issues
- Verify all claims supported
- Check writing quality

✅ **During Revision**:
- Systematic review of draft
- Identify weak sections
- Prioritize improvements
- Track progress

✅ **After Reviewer Feedback**:
- Verify changes address concerns
- Ensure no new issues introduced
- Check consistency after edits
- Prepare for resubmission

✅ **Collaborative Writing**:
- Ensure consistency across authors
- Check unified terminology
- Verify logical flow
- Identify integration issues

### When NOT to Use

❌ **Very Early Drafts**:
- Outline or notes stage
- Incomplete sections
- Missing experiments
→ Wait until content is complete

❌ **For Content Generation**:
- Generating new text
- Writing related work
- Creating figures
→ Use `scientific-writing` instead

❌ **For Literature Search**:
- Finding related papers
- Identifying gaps
- Positioning work
→ Use `arxiv-database` and `literature-review`

---

## How It Works

### The 5-Step Workflow

paper-validator follows a systematic 5-step process:

#### Step 1: Read Files
- Understand content and structure
- Identify sections (Abstract, Intro, Methods, etc.)
- Note figures, tables, equations
- Build mental model of paper

#### Step 2: Search for Patterns
- Undefined acronyms (e.g., "GAN" without definition)
- Passive voice overuse (>40% of sentences)
- Inconsistent terminology (model vs. method vs. system)
- Vague quantifiers ("large", "many", "significant")
- Missing citations (claims without references)

#### Step 3: Analyze Structure
- Check section organization
- Verify logical flow
- Ensure completeness (all expected sections present)
- Check figure/table integration
- Assess readability

#### Step 4: Identify Issues by Area
- **Arguments**: Are claims supported? Logic sound?
- **Clarity**: Is writing clear and precise?
- **Evidence**: Sufficient experimental validation?
- **Alternatives**: Assumptions examined? Counterarguments?
- **Novelty**: Contributions clear? Differentiated?
- **Confusion**: Organization logical? Context provided?

#### Step 5: Provide Consolidated Feedback
- Group issues by severity
- Provide specific locations
- Frame as constructive questions
- Prioritize actionable feedback

### Severity Levels

Issues are categorized by impact:

#### 🔴 Major (Blocking)
- **Impact**: Prevents publication
- **Examples**:
  - Unsupported main claims
  - Missing critical experiments
  - Fundamental logical flaws
  - Missing key baselines
- **Action**: Must fix before submission

#### 🟡 Moderate (Important)
- **Impact**: Weakens paper significantly
- **Examples**:
  - Unclear contribution statement
  - Missing ablation studies
  - Inconsistent terminology
  - Vague quantifiers
- **Action**: Should fix to strengthen paper

#### 🟢 Minor (Polish)
- **Impact**: Affects quality but not validity
- **Examples**:
  - Typos and grammar
  - Formatting inconsistencies
  - Minor clarity improvements
  - Citation formatting
- **Action**: Fix if time permits

---

## Usage Examples

### Example 1: Complete Paper Validation

**Scenario**: You have a complete draft ready for submission to NeurIPS.

**Prompt**:
```markdown
Use paper-validator skill to comprehensively validate my paper before
NeurIPS submission.

Title: "Attention-Enhanced Neural Networks for Medical Image Segmentation"
Target Venue: NeurIPS 2024

[Paste paper content or attach PDF]

Please check all six review areas and identify issues at all severity levels.
```

**What You Get**:
- Complete validation report
- Issues by severity and area
- Specific locations for each issue
- Constructive questions for improvement
- Priority order for addressing issues

**Time**: 15-30 minutes to review output, 2-4 hours to address issues

---

### Example 2: Quick Pre-Submission Check

**Scenario**: Paper is mostly ready, need quick final check.

**Prompt**:
```markdown
Use paper-validator skill for quick pre-submission check.

Focus on:
- Undefined acronyms
- Vague quantifiers
- Missing statistical tests
- Major logical issues

[Paste paper or provide file]
```

**What You Get**:
- Focused analysis on specified areas
- Only major and moderate issues
- Quick turnaround

**Time**: 10 minutes to review, 30-60 minutes to fix

---

### Example 3: Specific Section Review

**Scenario**: You revised your Methods section and want to verify quality.

**Prompt**:
```markdown
Use paper-validator skill to check my Methods section (Section 3).

Focus on:
- Reproducibility (are details sufficient?)
- Notation clarity (all variables defined?)
- Logical flow (is presentation clear?)

[Paste Section 3]
```

**What You Get**:
- Focused feedback on Methods section
- Reproducibility assessment
- Notation issues identified

**Time**: 5 minutes to review, 15-30 minutes to fix

---

### Example 4: Post-Revision Verification

**Scenario**: You addressed reviewer comments and want to verify fixes.

**Prompt**:
```markdown
Use paper-validator to verify that I've addressed reviewer concerns.

Reviewer said:
"Table 2 lacks statistical significance tests. Results appear marginal
without error bars or p-values."

I added 5-run experiments with mean ± std and p-values.

Please check:
1. Are statistical tests properly reported?
2. Are claims appropriately hedged given results?
3. Are any related issues introduced?

[Paste revised Section 4 and Table 2]
```

**What You Get**:
- Verification that issue is fixed
- Check for new issues introduced
- Confirmation of appropriate claims

**Time**: 5 minutes to review

---

### Example 5: Consistency Check for Multi-Author Paper

**Scenario**: Three authors wrote different sections; need consistency check.

**Prompt**:
```markdown
Use paper-validator to check consistency across sections.

Authors:
- Author A wrote Introduction (Section 1)
- Author B wrote Methods (Section 3)
- Author C wrote Results (Section 4)

Check for:
- Terminology consistency (do we use "model" vs "method" consistently?)
- Notation consistency (same symbols throughout?)
- Writing style consistency (similar voice and tense?)

[Paste full paper]
```

**What You Get**:
- Terminology conflicts identified
- Notation inconsistencies
- Style variations noted

**Time**: 10 minutes to review, 1-2 hours to harmonize

---

## Understanding Output

### Output Structure

paper-validator provides structured output:

```markdown
## Executive Summary
[2-3 sentences on overall quality and main issues]

## Validation Statistics
[Table showing issue counts by severity and area]

## Major Issues (Must Fix)
[Detailed description of each major issue]

## Moderate Issues (Should Fix)
[Detailed description of each moderate issue]

## Minor Issues (Nice to Fix)
[Concise list of minor issues]

## Strengths
[What the paper does well]

## Recommendation
[Ready / Minor Revisions / Major Revisions]
```

### Reading Issue Reports

Each issue includes:

**1. Location**:
```markdown
**Location**: Section 3.2, page 5, line 127
```
→ Tells you exactly where the issue is

**2. Issue Description**:
```markdown
**Issue**: The paper claims "significant improvement" but Table 2
shows only 0.4% difference without statistical tests.
```
→ Explains what's wrong and why it matters

**3. Current Text**:
```markdown
**Current text**:
"Our method achieves 94.7% accuracy, significantly outperforming
the baseline (94.3%)."
```
→ Shows the problematic text

**4. Validator Question**:
```markdown
**Validator Question**: Can you provide statistical significance
tests for the results in Table 2? Given the small margin (0.4%),
demonstrating significance through multiple runs with p-values
would strengthen the claim.
```
→ Constructive question guiding improvement

**5. Severity**:
```markdown
**Severity**: Major - affects validity of main claims
```
→ Helps you prioritize

**6. Suggested Fix** (when applicable):
```markdown
**Suggested fix**:
"Our method achieves 94.7 ± 0.3% accuracy, significantly outperforming
the baseline (94.3 ± 0.4%, p < 0.01)."
```
→ Concrete example of improvement

### Interpreting Severity

**Major Issues** = Show-stoppers
- Must fix before submission
- Will likely cause rejection if unfixed
- Address immediately

**Moderate Issues** = Significant weaknesses
- Should fix to strengthen paper
- May lead to major revision request
- Address in priority order

**Minor Issues** = Polish
- Nice to fix but not critical
- Improves quality and professionalism
- Address if time permits

### Validation Statistics

The statistics table shows issue distribution:

| Category | Major | Moderate | Minor | Total |
|----------|-------|----------|-------|-------|
| Arguments | 0 | 1 | 2 | 3 |
| Clarity | 0 | 3 | 5 | 8 |
| Evidence | 2 | 2 | 1 | 5 |

**How to read**:
- **High evidence issues**: Need more experiments/tests
- **High clarity issues**: Writing needs improvement
- **High novelty issues**: Contribution unclear
- **Balanced distribution**: Paper needs general polish

---

## Best Practices

### 1. Validate at Right Time

✅ **Good timing**:
- After content is complete
- Before submission
- After major revisions
- Before sharing with co-authors

❌ **Too early**:
- During initial drafting
- When experiments incomplete
- Before related work done

### 2. Address Issues in Order

**Priority order**:
1. Major issues (blocking)
2. Moderate issues (important)
3. Minor issues (polish)

**Why**: Major issues affect validity; minor issues are cosmetic.

### 3. Focus on Root Causes

**Example**:
- **Symptom**: "Vague quantifier in 6 places"
- **Root cause**: Need to be more specific throughout
- **Fix**: Global pass replacing vague terms with numbers

Don't fix issues one-by-one; find patterns and fix systematically.

### 4. Iterate

**Don't expect perfection in one pass**:
```
Draft → Validate → Fix Major Issues → Validate → Fix Moderate → Validate → Polish
```

Each validation pass should show fewer issues.

### 5. Use with Other Skills

paper-validator identifies issues; other skills help fix them:

| To Do | Use This Skill |
|-------|---------------|
| Find issues | paper-validator |
| Fix writing | scientific-writing |
| Add evidence | [run experiments] |
| Improve logic | scientific-critical-thinking |
| Position work | literature-review |
| Mock review | peer-review |

### 6. Track Progress

**Keep a checklist**:
```markdown
## Major Issues
- [x] Added statistical tests (Table 2)
- [x] Included recent baselines (Section 5)

## Moderate Issues
- [x] Fixed terminology (global)
- [ ] Replaced vague quantifiers (3/6 done)
- [ ] Defined acronyms (pending: OOD, GAN)

## Minor Issues
- [ ] Fixed typos (5 found)
- [ ] Improved figure captions
```

### 7. Don't Over-Optimize

**When to stop**:
- All major issues fixed ✅
- Most moderate issues addressed ✅
- Paper reads well ✅

**When not to stop**:
- Still have major issues ❌
- Many moderate issues remain ❌
- Unclear to readers ❌

**Balance**: Perfect is the enemy of good. Fix critical issues thoroughly; polish is secondary.

---

## Integration with Other Skills

paper-validator works best as part of an integrated workflow.

### Common Workflows

#### Workflow 1: Complete Paper Review
```
paper-validator (identify issues) →
scientific-writing (fix issues) →
paper-validator (verify fixes)
```

#### Workflow 2: Pre-Submission Check
```
paper-validator (final check) →
peer-review (mock review) →
scientific-writing (polish)
```

#### Workflow 3: Post-Review Revision
```
scientific-critical-thinking (evaluate reviewer feedback) →
[run additional experiments if needed] →
scientific-writing (address concerns) →
paper-validator (verify changes)
```

### Skill Combinations

| Your Goal | Use These Skills |
|-----------|-----------------|
| Complete paper review | paper-validator + peer-review + scientific-writing |
| Improve clarity | paper-validator + scientific-writing |
| Strengthen evidence | paper-validator + [experiments] + scientific-writing |
| Position work | literature-review + paper-validator + scientific-writing |
| Quick check | paper-validator only (focused mode) |

### Example Integration

**Goal**: Improve paper before submission

**Step 1 - Identify issues**:
```markdown
Use paper-validator to identify all issues in my draft.
```

**Step 2 - Fix major issues**:
```markdown
Use scientific-writing to fix these major issues:
1. [Issue 1 from paper-validator]
2. [Issue 2 from paper-validator]
```

**Step 3 - Verify fixes**:
```markdown
Use paper-validator to verify that issues 1 and 2 are now fixed.
```

**Step 4 - Mock review**:
```markdown
Use peer-review skill to generate comprehensive review for NeurIPS.
```

**Step 5 - Final polish**:
```markdown
Use scientific-writing to address reviewer concerns from mock review.
```

For detailed workflow examples, see `references/integration_workflows.md`.

---

## Troubleshooting

### Issue: Too Many Problems Identified

**Symptoms**: 50+ issues across all severity levels

**Solutions**:
1. **Focus on major issues first**
   - Filter for only major issues
   - Address those completely
   - Then tackle moderate issues

2. **Ask for targeted validation**
   ```markdown
   Use paper-validator to identify only major and moderate issues.
   Skip minor issues for now.
   ```

3. **Work section-by-section**
   - Validate and fix Abstract first
   - Then Introduction
   - Then Methods, etc.

**Prevention**: Validate earlier and more often

---

### Issue: Don't Understand How to Fix

**Symptoms**: Validator identified issue but fix isn't obvious

**Solutions**:
1. **Read reference materials**
   - Check `references/common_issues.md`
   - Check `references/writing_standards.md`
   - Look for similar examples

2. **Use scientific-writing skill**
   ```markdown
   Use scientific-writing to help me fix this issue:
   [paste validator's feedback]
   ```

3. **Ask for examples**
   ```markdown
   Can you show me 2-3 examples of how to fix this type of issue?
   [describe the issue]
   ```

---

### Issue: Issue Still Present After Fixing

**Symptoms**: Re-validation shows same issue

**Possible causes**:
1. **Fixed symptom, not root cause**
   - Example: Fixed one vague quantifier, but 5 more remain
   - Solution: Global search and fix all instances

2. **Introduced new instance**
   - Example: Fixed "large dataset" but wrote "many samples"
   - Solution: Search for all related patterns

3. **Didn't fully address**
   - Example: Added p-value but no error bars
   - Solution: Read validator feedback completely

**How to debug**:
```markdown
Use paper-validator to check specifically if [issue] is fixed.
[paste the revised text]
```

---

### Issue: Conflicting Feedback

**Symptoms**: Validator says one thing, advisor says another

**Remember**:
- paper-validator checks **technical quality**
- Advisors assess **scientific merit and positioning**
- Both are important but different

**When in conflict**:
1. **Fix technical quality issues** (validator)
2. **Then adjust for positioning** (advisor)
3. **Scientific merit trumps style** (advisor wins)

**Example**:
- Validator: "Make claims more specific"
- Advisor: "Broaden claims to appeal to wider audience"
- → Follow advisor for positioning, maintain technical accuracy

---

### Issue: Output Too Long

**Symptoms**: Validation report is 20+ pages

**Solutions**:
1. **Request summary only**
   ```markdown
   Use paper-validator to provide only executive summary and
   major issues. Skip moderate and minor issues.
   ```

2. **Validate section-by-section**
   - Break paper into sections
   - Validate each separately
   - Easier to process

3. **Filter by severity**
   ```markdown
   Show only major issues that would block publication.
   ```

---

### Issue: Don't Agree with Feedback

**Symptoms**: Validator identified "issue" but you disagree

**Remember**:
- Validators detect **potential** issues
- You decide if they apply to your context
- Some feedback may not fit your paper

**When to ignore**:
- Field-specific conventions differ
- Your case is exceptional (and explained)
- Trade-off is intentional

**When NOT to ignore**:
- Issue appears in multiple places
- Concerns technical accuracy
- Would confuse readers
- Violates venue requirements

**Best practice**:
If you disagree, ask for second opinion:
```markdown
Use scientific-critical-thinking to evaluate this feedback:
[validator's feedback]

Is this a real issue for my paper? Context: [explain context]
```

---

## FAQ

### Q1: How long does validation take?

**A**: Depends on paper length and detail level:
- Quick check (major issues only): 5-10 minutes
- Standard validation (all areas): 15-30 minutes
- Comprehensive review (with examples): 30-60 minutes

### Q2: Can I validate a paper in another language?

**A**: paper-validator works best with English papers. For other languages:
- Translate to English first
- Or use with caution (may miss language-specific issues)

### Q3: Does it work for all scientific fields?

**A**: Yes! paper-validator is domain-agnostic:
- Works for biology, chemistry, physics, CS, medicine, etc.
- Checks writing quality and logic, not domain expertise
- You need domain expertise to evaluate scientific merit

### Q4: How is this different from peer-review skill?

**A**: Different purposes:

| paper-validator | peer-review |
|----------------|-------------|
| Quality checking | Comprehensive review |
| Identifies issues | Evaluates contribution |
| Technical focus | Scientific merit focus |
| Specific fixes | Overall assessment |
| Fast (minutes) | Thorough (hours) |

Use both: paper-validator first (fix issues), then peer-review (assess merit).

### Q5: Can it write text for me?

**A**: No, paper-validator only identifies issues.

For writing/fixing, use `scientific-writing` skill.

### Q6: Will it find all issues?

**A**: paper-validator is very thorough but not perfect:
- ✅ Catches most common issues
- ✅ Systematic approach minimizes misses
- ❌ May miss domain-specific problems
- ❌ Cannot judge scientific novelty/impact

Always have co-authors and advisors review too.

### Q7: How do I know when paper is ready?

**Signs of readiness**:
- ✅ Zero major issues
- ✅ Few or zero moderate issues
- ✅ Logic is sound
- ✅ Claims are supported
- ✅ Writing is clear
- ✅ Experiments are complete

If paper-validator finds major issues, not ready yet.

### Q8: Can I validate someone else's published paper?

**A**: Yes! Useful for:
- Learning from examples
- Understanding what "good" looks like
- Comparing your work to accepted papers
- Identifying patterns to follow

```markdown
Use paper-validator to analyze this published NeurIPS paper.
What makes it high quality? What could be improved?
[paste paper]
```

### Q9: Does it check for plagiarism?

**A**: No. paper-validator checks quality, not originality.

For plagiarism checking, use specialized tools like:
- iThenticate
- Turnitin
- Copyscape

### Q10: Can it suggest citations?

**A**: No. paper-validator identifies missing citations but doesn't suggest specific papers.

For finding relevant papers, use:
- `arxiv-database` skill
- `literature-review` skill
- Google Scholar
- Semantic Scholar

---

## Getting Help

### Documentation

- **SKILL.md**: Complete skill specification
- **references/validation_checklist.md**: Systematic checklist
- **references/common_issues.md**: Frequent problems and fixes
- **references/writing_standards.md**: Writing conventions
- **references/example_validation_report.md**: Complete example
- **references/integration_workflows.md**: Multi-skill workflows
- **USER_GUIDE.md**: This document

### Support

- **Questions**: Ask Claude for clarification
- **Bug reports**: GitHub issues for claude-scientific-skills
- **Feature requests**: GitHub issues
- **Community**: Slack community

### Examples

The `references/` directory contains:
- 100+ examples of common issues
- Complete validation report example
- 8+ integration workflow examples
- Checklist for self-validation

---

## Conclusion

paper-validator is a powerful tool for systematic paper quality checking. Key takeaways:

✅ **Use it regularly**: Don't wait until submission
✅ **Address major issues first**: Prioritize blocking problems
✅ **Iterate**: Validate → Fix → Validate → Fix
✅ **Integrate with other skills**: Part of comprehensive workflow
✅ **Track progress**: Use checklists to stay organized
✅ **Focus on root causes**: Fix patterns, not individual instances

**Next Steps**:
1. Try it on your current draft
2. Review the example validation report
3. Check integration workflows for your use case
4. Use regularly throughout paper development

**Remember**: paper-validator helps you write better papers by catching issues before reviewers do. Use it early and often for best results.

---

**Document Version**: 1.0.0 (2024-01-15)
**Part of**: Claude Scientific Skills ecosystem
**License**: MIT
**Author**: K-Dense Inc.
