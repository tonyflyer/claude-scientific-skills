# arXiv Query Syntax Guide

## Overview

This guide explains how to construct effective search queries for the arXiv API.

## Basic Query Structure

### Field Prefixes

| Prefix | Field | Example |
|--------|-------|---------|
| `all` | All fields | `all:transformer` |
| `ti` | Title | `ti:attention` |
| `au` | Author | `au:hinton` |
| `abs` | Abstract | `abs:reinforcement learning` |
| `co` | Comment | `co: NeurIPS` |
| `jr` | Journal Reference | `jr:ICML` |
| `cat` | Category | `cat:cs.AI` |

### Boolean Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `AND` | All terms required | `ti:attention AND ti:transformer` |
| `OR` | Any term | `ti:CNN OR ti:convolutional` |
| `ANDNOT` | Exclude term | `ti:image ANDNOT classification` |

### Examples

#### Simple Searches
```bash
# Search for "transformer" anywhere
python scripts/search.py --query "transformer"

# Search in title only
python scripts/search.py --query "ti:transformer"

# Search for specific author
python scripts/search.py --author "Vaswani"
```

#### Complex Queries
```bash
# Papers about transformers in NLP
python scripts/search.py --query "ti:transformer AND abs:nlp"

# Papers by Hinton on deep learning
python scripts/search.py --query "au:Hinton AND abs:deep learning"

# Papers NOT about image classification
python scripts/search.py --query "all:segmentation ANDNOT ti:classification"

# Papers with "attention" in title OR abstract
python scripts/search.py --query "ti:attention OR abs:attention"
```

#### Combined with Categories
```bash
# ML papers about transformers
python scripts/search.py --query "transformer" --category cs.LG

# CV papers about detection
python scripts/search.py --query "detection" --categories cs.CV eess.IV
```

## Advanced Query Techniques

### Phrase Searches
```bash
# Exact phrase
python scripts/search.py --query '"attention is all you need"'
```

### Wildcards
```bash
# Single character wildcard
python scripts/search.py --query "neural networ?"

# Multiple character wildcard
python scripts/search.py --query "neura* network"
```

### Grouping
```bash
# Grouped OR
python scripts/search.py --query "(CNN OR RNN OR transformer) AND ti:survey"
```

### Field Ranges
```bash
# Date range
python scripts/search.py --start-date 2024-01-01 --end-date 2024-06-30

# Combined with category
python scripts/search.py --query "diffusion" --category cs.CV --start-date 2024-01-01
```

## Special Characters

The following characters are reserved and must be escaped with backslash:

```
+ - & | ( ) { } [ ] ^ " ~ * ? : \ /
```

Example:
```bash
python scripts/search.py --query "C\\+\\+ AND ti:programming"
```

## Query Best Practices

### Do
- Use specific queries to get relevant results
- Combine multiple fields (title + abstract)
- Use categories to filter early
- Use date ranges for recent work

### Don't
- Use overly broad queries (e.g., just "AI")
- Search without category filters for large topics
- Forget to escape special characters

## Common Query Patterns

### Find Survey Papers
```bash
python scripts/search.py --query "ti:survey AND (cs.LG OR cs.AI OR cs.CV)"
```

### Find Recent High-Impact Work
```bash
python scripts/search.py --query "state-of-the-art" --category cs.LG --days-back 180
```

### Find Papers by Institution (in comments)
```bash
python scripts/search.py --query "co:Google OR co:DeepMind OR co:Meta"
```

### Find Benchmark Papers
```bash
python scripts/search.py --query "benchmark AND (ImageNet OR COCO)"
```

### Find Code Availability
```bash
python scripts/search.py --query "co:GitHub OR co:code available"
```
