# Common Issues in Scientific Papers

A comprehensive guide to the most frequent problems found during paper validation, organized by review area.

---

## Arguments Issues

### 1. Unsupported Claims

**Problem:** Statements presented as facts without evidence

**Examples:**
```
❌ "Our method is significantly better than all existing approaches."
   (No evidence, no comparison, no metrics)

❌ "Deep learning has solved the problem of image recognition."
   (Overgeneralization, ignores limitations)

❌ "This proves that our hypothesis is correct."
   (Confusion between correlation and causation)
```

**Fix:**
```
✅ "Our method achieves 95.3% accuracy on ImageNet, outperforming
   the previous best result of 92.1% [Citation] by 3.2 percentage points."

✅ "Deep learning methods have achieved human-level performance on
   specific image recognition benchmarks [Citations], though challenges
   remain in adversarial robustness and few-shot learning."

✅ "These results support our hypothesis that [X], though alternative
   explanations such as [Y] cannot be ruled out."
```

**Validator Question:**
"Can you provide experimental evidence supporting the claim in Line 145 that [your method] is better than existing approaches? Including specific metrics and comparisons would strengthen this claim."

---

### 2. Logical Fallacies

**Common fallacies:**

#### Post Hoc Ergo Propter Hoc
```
❌ "Sales increased after we launched the campaign, therefore the
   campaign caused the increase."
```
**Issue:** Correlation doesn't imply causation

#### Hasty Generalization
```
❌ "We tested on three samples and observed X, therefore X is always true."
```
**Issue:** Insufficient sample size

#### Circular Reasoning
```
❌ "Method A is better because it achieves higher performance, and it
   achieves higher performance because it's a better method."
```
**Issue:** Conclusion assumed in premise

#### False Dichotomy
```
❌ "Either we use our method or we accept poor performance."
```
**Issue:** Ignores other alternatives

**Validator Question:**
"The reasoning in Section 3.2 appears to assume [X] when concluding [Y]. Could you clarify the logical connection or provide additional steps in the argument?"

---

### 3. Missing Logical Steps

**Problem:** Jumping from evidence to conclusion without intermediate steps

**Example:**
```
❌ "We observed that parameter α affects performance. Therefore,
   our method is superior to baselines."
```

**Missing steps:**
1. How does α relate to baseline methods?
2. What parameter values did baselines use?
3. Is the comparison fair?

**Fix:**
```
✅ "We observed that parameter α significantly affects performance
   (Table 2). Unlike baseline methods [Citations] which fix α=0.5,
   our method learns α adaptively. When baselines are enhanced with
   learned α, performance improves but remains below our method
   (Table 3), suggesting our gains come from both adaptive α and
   our novel architecture."
```

---

## Clarity Issues

### 1. Ambiguous Pronouns

**Problem:** "It", "this", "that" without clear antecedent

**Examples:**
```
❌ "The model processes input and generates output. It then optimizes
   the result."
   (What does "it" refer to? Model? Input? Output?)

❌ "We trained on dataset A and tested on dataset B. This showed
   better performance."
   (What showed better performance? Training? Testing? The dataset?)
```

**Fix:**
```
✅ "The model processes input and generates output. The model then
   optimizes the generated output."

✅ "We trained on dataset A and tested on dataset B. Testing on B
   showed better generalization than in-domain evaluation."
```

**Validator Question:**
"In Section 3.2, Line 156, what does 'it' refer to in the sentence [quote]? Clarifying this would improve readability."

---

### 2. Undefined Technical Terms

**Problem:** Using jargon or specialized terms without definition

**Examples:**
```
❌ "We use a GAN to generate samples."
   (First use of "GAN" - undefined)

❌ "The model exhibits strong OOD performance."
   (What is "OOD"?)

❌ "We employ a transformer-based architecture."
   (For general audience, needs brief explanation)
```

**Fix:**
```
✅ "We use a Generative Adversarial Network (GAN) [Citation] to
   generate samples. GANs consist of..."

✅ "The model exhibits strong out-of-distribution (OOD) performance,
   meaning it generalizes well to data from different domains."

✅ "We employ a transformer-based architecture [Citation], which uses
   self-attention mechanisms to process sequential data."
```

---

### 3. Inconsistent Terminology

**Problem:** Using multiple terms for the same concept

**Examples:**
```
❌ Using "model", "system", "method", "approach", "technique"
   interchangeably for the same thing

❌ Switching between "accuracy", "performance", "effectiveness"

❌ "dataset" vs. "data set" vs. "data-set" inconsistently
```

**Fix:**
```
✅ Choose one term (e.g., "method") and use consistently
✅ Use "accuracy" for metrics, "performance" for overall evaluation
✅ Standardize spelling: "dataset" (one word)
```

**Validator Question:**
"The paper uses 'model', 'system', and 'method' interchangeably. Consider standardizing to a single term for consistency."

---

### 4. Vague Quantifiers

**Problem:** Using imprecise terms without specifics

**Examples:**
```
❌ "We tested on a large dataset."
   (How large?)

❌ "Many papers have addressed this problem."
   (How many? Which papers?)

❌ "Our method is significantly faster."
   (How much faster? Statistical significance?)

❌ "The model performs well."
   (What metric? What value?)
```

**Fix:**
```
✅ "We tested on ImageNet, which contains 1.2 million training images."

✅ "15 papers published at top conferences (ICML, NeurIPS, ICLR) in
   the last 3 years have addressed this problem [Citations]."

✅ "Our method is 3.2× faster than the best baseline (p < 0.01),
   reducing training time from 24 hours to 7.5 hours."

✅ "The model achieves 94.7% accuracy on the test set, exceeding
   the 90% threshold required for deployment."
```

---

## Evidence Issues

### 1. Missing Baselines

**Problem:** Comparing only against weak or outdated methods

**Examples:**
```
❌ Comparing against methods from >5 years ago
❌ Comparing only against your own prior work
❌ Omitting the current state-of-the-art
❌ Cherry-picking easy baselines
```

**Fix:**
```
✅ Include recent SOTA methods from last 2 years
✅ Compare with multiple strong baselines
✅ Justify any omissions ("Method X is not comparable because...")
✅ Use standard benchmarks where available
```

**Validator Question:**
"Method Z [Citation, Year] appears to be the current state-of-the-art for this task according to [Benchmark]. How does your method compare? Including this comparison would better position your contribution."

---

### 2. No Statistical Significance

**Problem:** Reporting results without error bars or significance tests

**Examples:**
```
❌ Table showing: "Our method: 92.3%, Baseline: 91.9%"
   (Is 0.4% difference significant?)

❌ Claiming "improved performance" with only single runs
❌ No confidence intervals reported
❌ No discussion of variance across runs
```

**Fix:**
```
✅ "Our method: 92.3 ± 0.4%, Baseline: 91.9 ± 0.5% (p < 0.01, t-test)"
✅ Report mean ± std over multiple runs (typically 3-5)
✅ Include confidence intervals when appropriate
✅ Discuss variance: "Results are consistent across runs (low variance)"
```

**Validator Question:**
"Can you provide statistical significance tests for the results in Table 2? The improvements are small (0.4-0.8%), so demonstrating statistical significance would strengthen the claims."

---

### 3. Missing Ablations

**Problem:** Not showing which components contribute to performance

**Examples:**
```
❌ Proposing method with 3 novel components A, B, C but only
   evaluating full system

❌ No analysis of which component matters most
❌ No study of component interactions
❌ Can't determine if all components are necessary
```

**Fix:**
```
✅ Ablation table showing:
   - Full system: 94.5%
   - Without A: 92.1% (A contributes 2.4%)
   - Without B: 93.8% (B contributes 0.7%)
   - Without C: 90.3% (C contributes 4.2%)
   - Baseline: 89.5%

✅ Conclusion: "Component C contributes most (4.2%), followed by A
   (2.4%). Component B has smaller but consistent impact (0.7%)."
```

**Validator Question:**
"Your method has three key components (A, B, C mentioned in Section 3). Can you provide an ablation study showing the contribution of each? This would justify the design choices and show which components are most important."

---

### 4. Limited Evaluation Scope

**Problem:** Testing only on one dataset or scenario

**Examples:**
```
❌ Evaluating only on MNIST (too easy)
❌ Testing only one domain
❌ Single dataset evaluation
❌ No cross-dataset generalization
❌ No robustness tests
```

**Fix:**
```
✅ Test on multiple datasets from different domains
✅ Include cross-dataset evaluation (train on A, test on B)
✅ Test robustness to noise, corruptions, adversarial examples
✅ Evaluate on different data scales
✅ Test failure cases and limitations
```

**Validator Question:**
"The evaluation is limited to [Dataset X]. Would testing on additional datasets such as [Y] or [Z] help demonstrate the generalizability of your approach?"

---

## Alternatives Issues

### 1. Unexamined Assumptions

**Problem:** Making assumptions without justification or testing

**Examples:**
```
❌ "We assume the data is i.i.d."
   (Is this tested? What if violated?)

❌ "We assume labels are noise-free."
   (Realistic? What about noisy labels?)

❌ "We assume computational resources are unlimited."
   (What about resource-constrained settings?)
```

**Fix:**
```
✅ "We assume data is i.i.d., which holds for standard benchmark
   datasets [Citation]. Section 5.3 examines performance when this
   assumption is violated (non-i.i.d. scenarios)."

✅ "While we assume noise-free labels for main experiments, Section
   5.4 evaluates robustness to label noise (5-20% corruption rates)."

✅ "Main experiments assume typical research settings (GPU access).
   Section 5.5 evaluates resource-constrained scenarios."
```

**Validator Question:**
"The method assumes [X] (stated in Section 3.1). How would performance degrade if this assumption doesn't hold? A brief robustness analysis would strengthen the paper."

---

### 2. Ignoring Failure Cases

**Problem:** Only showing successes, not discussing when method fails

**Examples:**
```
❌ No discussion of limitations
❌ Only showing cherry-picked examples
❌ Not examining failure modes
❌ No error analysis
```

**Fix:**
```
✅ "Our method performs well on [scenarios], but struggles with
   [specific cases]. Figure 5 shows failure examples where..."

✅ "Limitations: (1) Requires large training data (10K+ samples),
   (2) Struggles with extreme class imbalance (>100:1),
   (3) Computational cost limits real-time applications."

✅ "Error analysis (Section 5.6) reveals most failures occur in
   [specific scenario]. This suggests future work should focus on..."
```

---

### 3. Missing Alternative Explanations

**Problem:** Not considering other interpretations of results

**Examples:**
```
❌ "Method A beats Method B, therefore A's architecture is better."
   (Could be: hyperparameters, implementation, dataset bias, luck)

❌ "Adding component X improves performance, so X is necessary."
   (Could be: any regularization helps, overfitting reduced, etc.)
```

**Fix:**
```
✅ "Method A outperforms B in our experiments. To isolate the
   architectural contribution, we: (1) tuned both equally carefully,
   (2) used the same implementation framework, (3) averaged over 5
   seeds. This suggests architectural differences drive the gains,
   though further investigation of training dynamics is warranted."

✅ "Adding component X improves performance. We hypothesize this is
   due to [specific mechanism]. To test this, we compare with
   alternative regularization approaches (Table 4), which show
   smaller gains, supporting our hypothesis."
```

---

## Novelty Issues

### 1. Unclear Contribution

**Problem:** Not clearly stating what's new

**Examples:**
```
❌ "We propose a novel deep learning method."
   (What's novel? Architecture? Loss? Training?)

❌ Introduction doesn't highlight contributions
❌ Related work doesn't differentiate from prior work
❌ Methods section looks like incremental change
```

**Fix:**
```
✅ "Our contributions are: (1) A new attention mechanism that...
   Unlike prior work [Citation] which..., our approach...,
   (2) A training procedure that..., and (3) State-of-the-art
   results on 3 benchmarks, with 4.2% average improvement."

✅ "While [Prior Work] proposed [X], they assumed [limitation].
   Our key insight is [new idea], which enables [capability]."
```

---

### 2. Missing Related Work Citations

**Problem:** Not citing relevant prior work

**Examples:**
```
❌ Claiming first to do X when similar work exists
❌ Ignoring concurrent work
❌ Missing key papers in the field
❌ Outdated related work (all citations >3 years old)
```

**Fix:**
```
✅ Comprehensive literature review
✅ Include work from last 2 years
✅ Cite both historical foundations and recent advances
✅ Acknowledge concurrent work if applicable
✅ Differentiate clearly from each cited work
```

**Validator Question:**
"Reference [X, Year] appears to propose a similar approach using [technique]. Can you clarify how your work differs in Section 2? Explicitly stating the key differences would strengthen the novelty claim."

---

### 3. Overclaimed Novelty

**Problem:** Claiming too much novelty for incremental work

**Examples:**
```
❌ "We propose the first method to..."
   (When prior work exists)

❌ "Revolutionary approach that..."
   (Hyperbole without evidence)

❌ Calling standard technique "novel"
   (E.g., calling batch normalization novel in 2024)
```

**Fix:**
```
✅ "We extend [Prior Work] by adding [specific modification],
   which enables [new capability]."

✅ "Our contributions are incremental but important: we show that
   [small change] leads to [significant impact]."

✅ "While [technique] is well-established, our application to
   [new domain] is, to our knowledge, the first demonstration of..."
```

---

## Confusion Issues

### 1. Poor Organization

**Problem:** Illogical structure or missing sections

**Examples:**
```
❌ Methods described before motivation
❌ Results presented before methods
❌ Related work at the end (hard to position contributions)
❌ Jumping between topics within sections
❌ No clear narrative flow
```

**Fix:**
```
✅ Standard structure:
   Abstract → Introduction → Related Work (or after Methods) →
   Methods → Results → Discussion → Conclusion

✅ Each section has clear purpose
✅ Smooth transitions between sections
✅ Logical progression of ideas
```

---

### 2. Notation Before Definition

**Problem:** Using symbols before defining them

**Examples:**
```
❌ Equation 3 uses θ, defined later in Section 3.3
❌ Figure 2 shows α, β without explanation
❌ Algorithm uses notation not in text
```

**Fix:**
```
✅ Define notation when first used
✅ Include notation table if many symbols
✅ Be consistent across equations, figures, algorithms
✅ Use standard notation when possible
```

**Validator Question:**
"Notation θ is used in Equation 3 before being defined. Can you define it when first introduced? This would prevent reader confusion."

---

### 3. Missing Intuitive Explanation

**Problem:** Jumping straight into math without intuition

**Examples:**
```
❌ Section starts with complex equation
❌ No example before formalization
❌ No figure showing key idea
❌ Technical details before big picture
```

**Fix:**
```
✅ Start with intuitive explanation
✅ Provide simple example
✅ Show figure illustrating concept
✅ Then give formal definition
✅ Walk through example using formal definition
```

**Example structure:**
```
"Intuitively, our method works by [simple explanation]. For example,
consider [concrete case]. Now we formalize this intuition. Let X be
[definition]... Returning to our example, we see that..."
```

---

## Severity Assessment

### How to Determine Severity

**🔴 Major (Must Fix):**
- Affects validity of results
- Fundamental flaws in methodology
- Main claims unsupported
- Critical experiments missing
- Prevents publication

**🟡 Moderate (Should Fix):**
- Affects interpretation of results
- Missing important comparisons
- Unclear explanations of key points
- Limits impact or generalizability
- Weakens but doesn't block publication

**🟢 Minor (Nice to Fix):**
- Affects presentation quality
- Grammar, typos, formatting
- Minor clarity improvements
- Doesn't affect scientific validity
- Polish for better readability

---

## Prevention Strategies

### During Writing
1. **Define terms immediately** - Don't use before defining
2. **Support all claims** - Add [Citation needed] markers
3. **Be specific** - Avoid "many", "large", "significant" without numbers
4. **Test assumptions** - Include robustness experiments early
5. **Ablate components** - Test each independently

### Before Submission
1. **Fresh read-through** - Wait 24 hours, read again
2. **Read aloud** - Catches awkward phrasing
3. **Peer review** - Have colleague read
4. **Use paper-validator** - Systematic check
5. **Compare with accepted papers** - Match quality standards

---

This reference is part of the Claude Scientific Skills ecosystem.
Use the `paper-validator` skill for systematic issue detection.
