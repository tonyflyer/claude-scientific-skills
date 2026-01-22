# Scientific Writing Standards

A comprehensive reference for writing standards enforced by the paper-validator skill.

---

## Overview

This document details the writing conventions and standards that paper-validator checks for. Following these standards ensures clarity, consistency, and professionalism in scientific writing.

---

## 1. Hyphenation Rules

### Compound Adjectives

**Rule**: Hyphenate compound adjectives when they appear before the noun they modify.

**Examples:**
```
✅ Correct:
- "state-of-the-art method"
- "peer-reviewed journal"
- "well-established technique"
- "high-performance computing"
- "open-source software"
- "real-time processing"
- "end-to-end training"
- "large-scale dataset"

❌ Incorrect:
- "state of the art method"
- "peer reviewed journal"
- "well established technique"
```

**After the noun (no hyphen needed):**
```
✅ Correct:
- "The method is state of the art."
- "The journal is peer reviewed."
- "This technique is well established."
```

### Common Compound Terms

**Always hyphenated:**
- cross-validation
- multi-layer
- self-attention
- pre-training
- fine-tuning
- meta-learning
- semi-supervised
- non-parametric
- real-world
- trade-off

**Context-dependent (before noun only):**
- deep-learning model (but "deep learning is effective")
- machine-learning algorithm (but "machine learning methods")
- data-driven approach (but "approach is data driven")

### Exceptions

**No hyphen needed:**
- "very" + adjective: "very large dataset" (not "very-large")
- Adverbs ending in "-ly": "recently published paper" (not "recently-published")
- Well-known abbreviations: "RNA seq data" (not "RNA-seq data" unless field convention)

---

## 2. Voice and Tense

### Active vs. Passive Voice

**Guideline**: Prefer active voice (>70% of sentences), especially for your contributions.

**Active voice preferred:**
```
✅ Active (your work):
- "We propose a novel attention mechanism."
- "Our method achieves 95% accuracy."
- "We conducted three experiments to test..."
- "The model learns feature representations."

❌ Passive (weakens impact):
- "A novel attention mechanism is proposed."
- "95% accuracy is achieved by our method."
- "Three experiments were conducted to test..."
- "Feature representations are learned."
```

**Passive voice acceptable:**
```
✅ When method/object is more important than actor:
- "Samples were collected from 10 sites." (where matters, not who)
- "The dataset was filtered to remove outliers." (what matters)
- "Images were preprocessed using standard techniques." (process matters)

✅ For standard procedures:
- "Statistical significance was assessed using t-tests."
- "Parameters were initialized randomly."
- "Results were averaged over 5 runs."

✅ When actor is unknown/unimportant:
- "The theorem was first proven in 1985."
- "This approach has been widely adopted."
```

### Tense Usage

**Present tense** - Your contributions and general truths:
```
✅ Present:
- "Our method achieves..." (your results)
- "Figure 2 shows..." (referring to your figures)
- "The model consists of..." (describing your system)
- "Neural networks are..." (general facts)
- "This approach is effective..." (your findings)
```

**Past tense** - Prior work and your experimental procedures:
```
✅ Past:
- "Smith et al. proposed..." (prior work)
- "Previous approaches used..." (prior work)
- "We trained the model for..." (what you did)
- "The experiments were conducted..." (your procedures)
- "We observed that..." (your observations)
```

**Future tense** - Future work:
```
✅ Future:
- "We will investigate..."
- "Future work could explore..."
- "This approach may enable..."
```

**Consistency within sections:**
- Abstract: Present tense for contributions
- Introduction: Present for motivation, past for prior work
- Methods: Past for what you did, present for descriptions
- Results: Past for observations, present for interpretations
- Discussion: Present for implications
- Conclusion: Present for contributions

---

## 3. Acronyms and Abbreviations

### First Use Definition

**Rule**: Define acronyms on first use with format: "Long Form (ACRONYM)"

**Examples:**
```
✅ Correct:
- "Generative Adversarial Networks (GANs) are..."
- "We use Convolutional Neural Networks (CNNs) for..."
- "The Area Under Curve (AUC) metric shows..."
- "Our Out-Of-Distribution (OOD) detection method..."

❌ Incorrect:
- "GANs are..." (not defined)
- "We use CNNs for..." (not defined)
- "Convolutional Neural Networks (CNN) for..." (wrong form)
- "(CNN) Convolutional Neural Networks are..." (backwards)
```

### Exceptions (Don't define)

**Very common terms** (but use judgment for audience):
- DNA, RNA, CPU, GPU
- HTTP, URL, API
- USA, UK, EU

**Field-standard terms** in specialized venues:
- ML, AI, NLP, CV (in CS/AI venues)
- PCR, ELISA, HPLC (in bio/chem venues)
- MRI, CT, fMRI (in medical venues)

**When in doubt, define it.**

### Plural Forms

```
✅ Correct:
- "multiple CNNs" (not "multiple CNN's")
- "several GANs" (not "several GAN's")
- "both APIs" (not "both API's")
```

### Acronyms in Titles/Headings

**Rule**: Avoid acronyms in paper title unless universally known.

```
✅ Title: "Deep Learning for Medical Image Segmentation"
❌ Title: "DL for Medical Image Segmentation"

✅ Title: "DNA Sequence Analysis Using..."
✅ Title: "GPU-Accelerated Molecular Dynamics"
```

---

## 4. Conciseness

### Eliminate Redundancy

**Wordy phrases → Concise alternatives:**

| Wordy | Concise |
|-------|---------|
| due to the fact that | because |
| in order to | to |
| at this point in time | now |
| for the purpose of | to, for |
| in the event that | if |
| with regard to | about |
| it is important to note that | (often omit) |
| has the ability to | can |
| a number of | several, many |
| a large number of | many |
| in spite of the fact that | although |
| on the basis of | based on |
| make use of | use |
| provide an explanation | explain |
| conduct an investigation | investigate |
| perform an analysis | analyze |

**Examples:**
```
❌ Wordy:
"Due to the fact that the model has the ability to learn from
large amounts of data, it performs well in order to achieve
high accuracy."

✅ Concise:
"Because the model can learn from large datasets, it achieves
high accuracy."
```

### Eliminate Unnecessary Words

```
❌ "It is important to note that the results show..."
✅ "The results show..."

❌ "It can be seen that Figure 2 demonstrates..."
✅ "Figure 2 shows..."

❌ "The model achieved an accuracy of 95%."
✅ "The model achieved 95% accuracy."

❌ "In this paper, we propose..."
✅ "We propose..." (context is clear)
```

### One Idea Per Sentence

```
❌ Long, complex:
"The model, which was trained on ImageNet and consists of 50
layers with residual connections similar to ResNet but with
additional attention mechanisms that allow it to focus on
relevant features, achieves state-of-the-art performance."

✅ Split into multiple sentences:
"The model consists of 50 layers with residual connections and
attention mechanisms. Similar to ResNet, it uses skip connections,
but adds attention to focus on relevant features. When trained on
ImageNet, it achieves state-of-the-art performance."
```

---

## 5. Quantifiers and Specificity

### Vague → Specific

**Avoid vague quantifiers; provide specific numbers:**

| Vague | Specific |
|-------|----------|
| large dataset | 10 million samples |
| many papers | 15 recent studies [Citations] |
| high accuracy | 94.7% accuracy |
| significantly faster | 3.2× speedup (p < 0.01) |
| small error | 2.3% error rate |
| several experiments | five independent runs |
| recent work | studies from 2023-2024 |
| most cases | 87% of instances |
| few failures | 3 out of 100 tests |

**Examples:**
```
❌ Vague:
"Our method is significantly better and runs much faster on
large datasets with good accuracy."

✅ Specific:
"Our method achieves 94.7% accuracy compared to 91.2% for the
baseline (p < 0.01), running 3.2× faster on datasets with
>1 million samples."
```

### Statistical Significance

**Always include:**
- Exact p-values or significance level
- Effect size when claiming "significant"
- Confidence intervals when appropriate

```
✅ Specific:
- "significantly higher (p < 0.01)"
- "statistically significant improvement (p = 0.003, t-test)"
- "95% CI: [0.23, 0.41]"
- "Cohen's d = 0.8, large effect"

❌ Vague:
- "significantly higher" (no stats)
- "notable improvement" (not quantified)
- "substantial effect" (no measure)
```

---

## 6. Terminology Consistency

### Choose One Term

**Problem**: Using multiple terms for the same concept confuses readers.

**Solution**: Choose one term early and use consistently.

**Common inconsistencies:**

| Inconsistent | Consistent Choice |
|--------------|------------------|
| model/system/method/approach | method |
| dataset/data set/data-set | dataset |
| accuracy/performance/effectiveness | accuracy (for metric), performance (for overall) |
| train/training/learn/learning | training (for process), learned (for result) |
| optimize/optimise | optimize (US) or optimise (UK), pick one |
| analyze/analyse | analyze (US) or analyse (UK), pick one |

**Examples:**
```
❌ Inconsistent:
"Our system uses a novel approach. The model achieves high
accuracy. This method outperforms..."

✅ Consistent:
"Our method uses a novel approach. The method achieves high
accuracy. This method outperforms..."
```

### Technical Terms

**Define specialized terms on first use:**

```
✅ Clear:
"We employ a transformer-based architecture [Citation], which
uses self-attention mechanisms to process sequential data by
learning relationships between all positions simultaneously."

❌ Unclear:
"We employ a transformer-based architecture." (no explanation)
```

### Field-Specific Conventions

**Follow your field's standard terminology:**

**Computer Science:**
- "training set" (not "training data")
- "hyperparameters" (not "hyper-parameters")
- "neural network" (not "neural net" in formal writing)

**Biology:**
- "gene expression" (not "gene transcription" unless specific)
- "single-cell RNA sequencing" (not "scRNA-seq" on first use)

**Chemistry:**
- IUPAC naming conventions
- Standardized compound names

---

## 7. Citation Practices

### When to Cite

**Always cite:**
- Prior work you build upon
- Methods/algorithms you use
- Datasets you evaluate on
- Claims of fact from literature
- Baseline methods for comparison
- Theoretical foundations

**Examples:**
```
✅ Properly cited:
"We use the ImageNet dataset [1], which contains 1.2 million
training images across 1000 classes. Our architecture is based
on ResNet [2] but incorporates attention mechanisms [3]."

❌ Missing citations:
"We use the ImageNet dataset. Our architecture is based on
ResNet but incorporates attention mechanisms."
```

### Citation Style

**Follow venue requirements:**
- Numbered: [1], [2], [1, 3-5]
- Author-year: (Smith, 2023), (Smith and Jones, 2024)
- Footnotes: Superscript¹

**Integrate citations smoothly:**
```
✅ Good integration:
"Smith et al. [1] proposed a novel attention mechanism."
"Recent work has shown improved performance [1-3]."
"Transformers [1] have become the dominant architecture."

❌ Poor integration:
"[1] proposed a novel attention mechanism."
"A novel attention mechanism was proposed [1]."
```

---

## 8. Numbers and Units

### Number Format

**Spell out small numbers in text:**
```
✅ "three experiments"
✅ "five datasets"
✅ "10 iterations" (larger numbers use digits)
✅ "100 samples"
```

**Always use digits for:**
- Measurements: "5 mm", "10 kg", "3.2 seconds"
- Statistics: "p = 0.01", "n = 100", "95% CI"
- Equations and math: "x + 3 = 5"
- Large numbers: "1,000 samples", "1.2 million images"

**Special cases:**
```
✅ "5× faster" (with multiplication symbol)
✅ "10-fold cross-validation"
✅ "3-layer network"
```

### Units

**Always include units:**
```
❌ "The model runs in 3.2"
✅ "The model runs in 3.2 seconds"

❌ "Dataset size is 10"
✅ "Dataset size is 10 million samples"

❌ "Memory usage is 2.5"
✅ "Memory usage is 2.5 GB"
```

**Standard units:**
- Time: seconds, minutes, hours (not sec, min, hrs in formal text)
- Memory: GB, MB, TB
- Size: pixels, samples, examples
- Performance: accuracy (%), error rate (%), throughput (samples/sec)

---

## 9. Equations and Mathematical Notation

### Punctuation

**Equations are part of sentences; punctuate accordingly:**

```
✅ Correct:
"The loss function is defined as:
    L = -log(p(y|x)),     (1)
where x is the input and y is the label."

"We minimize the objective:
    J(θ) = ∑ᵢ ||f(xᵢ) - yᵢ||².     (2)"
```

### Variable Definition

**Define all variables:**
```
✅ Clear:
"Let x ∈ ℝᵈ denote the input features, where d is the
dimensionality. The model output is y = f(x; θ), where
θ represents the learnable parameters."

❌ Unclear:
"The model output is y = f(x; θ)."
(Variables not defined)
```

### Consistency

**Use same notation throughout:**
- θ for parameters (not sometimes W, sometimes θ)
- x for input (not sometimes x, sometimes X)
- Distinguish scalars (x), vectors (x or **x**), matrices (X or **X**)

---

## 10. Pronouns and Clarity

### Clear Antecedents

**Problem**: "It", "this", "that" without clear reference.

**Examples:**
```
❌ Ambiguous:
"The model processes the input and generates an output. It is
then optimized."
(What is optimized? Model? Input? Output?)

✅ Clear:
"The model processes the input and generates an output. The
output is then optimized."

❌ Ambiguous:
"We trained on dataset A and tested on dataset B. This showed
better performance."
(What showed better performance?)

✅ Clear:
"We trained on dataset A and tested on dataset B. Cross-dataset
evaluation showed better generalization."
```

### Demonstrative Pronouns

**Use "this/that/these/those" + noun:**
```
❌ Vague:
"We use attention mechanisms. This improves performance."

✅ Clear:
"We use attention mechanisms. This approach improves performance."
or
"We use attention mechanisms. These mechanisms improve performance."
```

---

## 11. Paragraph Structure

### Topic Sentences

**Each paragraph should:**
- Start with a topic sentence stating the main idea
- Provide supporting details
- Maintain single focus

```
✅ Good paragraph structure:

"[TOPIC] Our method outperforms baselines on three metrics.
[SUPPORT] On accuracy, we achieve 94.7% compared to 91.2% for
the best baseline (Table 2). [SUPPORT] Inference speed is 3.2×
faster (0.8ms vs 2.6ms per sample). [SUPPORT] Memory usage is
reduced by 40% (1.2GB vs 2.0GB). [CONCLUSION] These improvements
enable deployment on resource-constrained devices."
```

### Transitions

**Connect ideas smoothly:**
```
✅ Good transitions:
- "However, previous approaches..."
- "In contrast, our method..."
- "Building on this observation..."
- "To address this limitation..."
- "Consequently, we propose..."
```

---

## 12. Common Grammar Issues

### Subject-Verb Agreement

```
❌ Wrong: "The set of features are important."
✅ Correct: "The set of features is important."

❌ Wrong: "Each of the methods have advantages."
✅ Correct: "Each of the methods has advantages."
```

### Dangling Modifiers

```
❌ Dangling: "Trained on ImageNet, the results show..."
✅ Fixed: "Trained on ImageNet, the model achieves..."

❌ Dangling: "Using attention mechanisms, performance improves."
✅ Fixed: "Using attention mechanisms, our method improves performance."
```

### Parallel Structure

```
❌ Not parallel: "Our method is fast, accurate, and uses little memory."
✅ Parallel: "Our method is fast, accurate, and memory-efficient."

❌ Not parallel: "We trained the model, tested it, and evaluation of results."
✅ Parallel: "We trained the model, tested it, and evaluated results."
```

---

## 13. LaTeX-Specific Conventions

### Citations

```latex
% Proper citation integration
Smith et al.~\cite{smith2023} proposed...

% Multiple citations
Recent work~\cite{smith2023,jones2024,brown2024} has shown...

% Citation range
Several studies~\cite{ref1,ref2,ref3,ref4,ref5} have...
% Better: Several studies~\cite{ref1}–\cite{ref5} have...
```

### Non-breaking Spaces

```latex
% Use ~ for non-breaking space
Figure~\ref{fig:results}
Table~\ref{tab:comparison}
Section~\ref{sec:methods}
Equation~\eqref{eq:loss}
```

### Math Mode

```latex
% Inline math: use $ ... $
The parameter $\theta$ controls...

% Display math: use \[ ... \] or equation environment
\[
L(\theta) = \sum_{i=1}^{n} \ell(f(x_i; \theta), y_i)
\]
```

---

## 14. Section-Specific Standards

### Abstract

**Standards:**
- 150-250 words
- Self-contained (no citations needed)
- States: problem, approach, results, conclusions
- Present tense for contributions
- Specific numbers for key results

### Introduction

**Standards:**
- Motivates problem (why it matters)
- States research question clearly
- Previews contributions (often numbered)
- Outlines paper structure
- Cites key related work

### Methods

**Standards:**
- Detailed enough for reproduction
- Notation defined before use
- Algorithm pseudocode when appropriate
- Parameters and hyperparameters specified
- Past tense for what you did

### Results

**Standards:**
- Figures/tables with clear captions
- Statistical significance tests
- Error bars on all measurements
- Comparison with strong baselines
- Ablation studies for key components

### Discussion

**Standards:**
- Interprets results (what do they mean?)
- Relates to research question
- Discusses limitations honestly
- Compares with prior work
- Suggests future directions

### Conclusion

**Standards:**
- Summarizes contributions
- Restates key findings
- Discusses broader impact
- No new information
- Present tense

---

## 15. Reference Standards

### Complete Information

**Required fields:**
- Authors (all, or first N + "et al.")
- Title
- Venue (journal/conference)
- Year
- Pages (journal) or proceedings (conference)
- DOI when available

**Format examples:**
```
Journal:
[1] Smith, J., Jones, A., and Brown, B. "Title of paper."
    Journal Name 15.2 (2023): 123-145. DOI: 10.1234/journal.2023.

Conference:
[2] Johnson, C. and Lee, D. "Paper title." Proceedings of the
    Conference on Topic (2024): 456-470.

Preprint:
[3] Taylor, E. et al. "Preprint title." arXiv:2401.12345 (2024).
```

---

## Checklist Summary

Use this quick checklist for writing review:

- [ ] Compound adjectives hyphenated before nouns
- [ ] Active voice >70%, especially for contributions
- [ ] Present tense for contributions, past for prior work
- [ ] All acronyms defined on first use
- [ ] Eliminated wordy phrases
- [ ] Specific numbers instead of vague quantifiers
- [ ] Consistent terminology throughout
- [ ] All variables defined before use
- [ ] Clear pronoun antecedents
- [ ] Citations for all claims and prior work
- [ ] Units included with all measurements
- [ ] Proper equation punctuation
- [ ] LaTeX non-breaking spaces used
- [ ] Complete reference information

---

This reference guide is part of the Claude Scientific Skills ecosystem.
Use the `paper-validator` skill for systematic application of these standards.
