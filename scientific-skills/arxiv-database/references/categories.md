# arXiv Category Reference

## Overview

This document provides a comprehensive reference for arXiv subject categories used in computer science, AI, and related fields.

## Computer Science (cs)

| Category | Description |
|----------|-------------|
| `cs.AI` | Artificial Intelligence |
| `cs.CL` | Computation and Language (NLP) |
| `cs.CC` | Computational Complexity |
| `cs.CE` | Computational Engineering, Finance, and Science |
| `cs.CG` | Computational Geometry |
| `cs.GT` | Computer Science and Game Theory |
| `cs.CV` | Computer Vision |
| `cs.CY` | Computers and Society |
| `cs.DB` | Databases |
| `cs.DC` | Distributed Computing |
| `cs.DL` | Digital Libraries |
| `cs.DM` | Discrete Mathematics |
| `cs.DS` | Data Structures and Algorithms |
| `cs.ET` | Emerging Technologies |
| `cs.FL` | Formal Languages and Automata Theory |
| `cs.GL` | General Literature |
| `cs.GR` | Graphics |
| `cs.HC` | Human-Computer Interaction |
| `cs.IR` | Information Retrieval |
| `cs.IT` | Information Theory |
| `cs.LG` | Machine Learning |
| `cs.LO` | Logic in Computer Science |
| `cs.MS` | Mathematical Software |
| `cs.MA` | Multiagent Systems |
| `cs.MM` | Multimedia |
| `cs.NI` | Networking and Internet Architecture |
| `cs.NE` | Neural and Evolutionary Computing |
| `cs.OS` | Operating Systems |
| `cs.OH` | Other Computer Science |
| `cs.PF` | Performance |
| `cs.PL` | Programming Languages |
| `cs.RO` | Robotics |
| `cs.SI` | Social and Information Networks |
| `cs.SE` | Software Engineering |
| `cs.SD` | Sound |
| `cs.SC` | Systems and Control |
| `cs.SY` | Systems and Control (alternative) |

## Statistics (stat)

| Category | Description |
|----------|-------------|
| `stat.ML` | Machine Learning |
| `stat.TH` | Statistics Theory |
| `stat.ME` | Methodology |
| `stat.CO` | Computation |
| `stat.AP` | Applications |

## Physics (physics)

| Category | Description |
|----------|-------------|
| `physics.flu-dyn` | Fluid Dynamics |
| `physics.comp-ph` | Computational Physics |
| `physics.data-an` | Data Analysis, Statistics and Probability |
| `physics.ao-ph` | Atmospheric and Oceanic Physics |
| `physics.geo-ph` | Geophysics |

## Electrical Engineering and Systems Science (eess)

| Category | Description |
|----------|-------------|
| `eess.AS` | Audio and Speech Signal Processing |
| `eess.IV` | Image and Video Processing |
| `eess.SP` | Signal Processing |
| `eess.SY` | Systems and Control |

## Math (math)

| Category | Description |
|----------|-------------|
| `math.OC` | Optimization and Control |
| `math.PR` | Probability |
| `math.ST` | Statistics |
| `math.NA` | Numerical Analysis |
| `math.LO` | Logic |

## Common Category Combinations

### Machine Learning
```
cs.AI, cs.LG, stat.ML
```

### Computer Vision
```
cs.CV, cs.LG, eess.IV
```

### Natural Language Processing
```
cs.CL, cs.LG
```

### Robotics
```
cs.RO, cs.LG, cs.SY
```

### Reinforcement Learning
```
cs.LG, cs.AI, stat.ML
```

### AI Safety
```
cs.AI, cs.LG, cs.HC
```

## Category Search Examples

### Search ML papers from 2024
```bash
python scripts/search.py --category cs.LG --start-date 2024-01-01 --end-date 2024-12-31
```

### Search Computer Vision papers
```bash
python scripts/search.py --categories cs.CV eess.IV --max-results 100
```

### Search Reinforcement Learning
```bash
python scripts/search.py --query "reinforcement learning" --category cs.LG
```

## Category Statistics

As of 2024, the most active arXiv categories by paper count:

1. `cs.LG` - Machine Learning (~50,000 papers/year)
2. `cs.AI` - Artificial Intelligence (~25,000 papers/year)
3. `cs.CV` - Computer Vision (~20,000 papers/year)
4. `cs.CL` - Computation and Language (~15,000 papers/year)
5. `stat.ML` - Statistics ML (~12,000 papers/year)
