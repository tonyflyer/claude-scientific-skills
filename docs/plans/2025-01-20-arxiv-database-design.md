# arxiv-database Skill Design Document

**Date**: 2025-01-20
**Author**: Claude AI Assistant
**Status**: Approved for Implementation

## Overview

Design document for adding arXiv paper search and analysis capabilities to claude-scientific-skills project, targeting computer science, AI, and automatic control research domains.

## Goals

- Extend scientific skills from biomedical domain to CS/AI/control domains
- Provide complete academic workflow: search → download → analysis → peer review → revision
- Reuse existing skills where possible (peer-review, citation-management, scientific-writing)
- Follow project conventions (参照 biorxiv-database structure)

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│         预置工作流模板层 (Templates)                      │
│  快速文献调研 | 深度论文分析 | 论文复现 | 综述撰写        │
├─────────────────────────────────────────────────────────┤
│         高级分析模块层 (Advanced Analysis)               │
│  论文解析 | 创新点评估 | 方法论分析 | 修订建议           │
├─────────────────────────────────────────────────────────┤
│         基础检索模块层 (Core Search - 自建)              │
│  关键词搜索 | 作者搜索 | 分类搜索 | 下载管理             │
└─────────────────────────────────────────────────────────┘
```

## Directory Structure

```
scientific-skills/arxiv-database/
├── SKILL.md
├── pyproject.toml
├── references/
│   ├── api_reference.md
│   ├── query_syntax.md
│   ├── categories.md
│   └── integration_guide.md
├── scripts/
│   ├── __init__.py
│   ├── arxiv_client.py
│   ├── search.py
│   ├── download.py
│   ├── parse.py
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── extractor.py
│   │   ├── evaluator.py
│   │   └── reviewer.py
│   └── templates/
│       ├── __init__.py
│       ├── literature_review.py
│       ├── deep_analysis.py
│       ├── reproduction.py
│       └── survey.py
└── tests/
    ├── __init__.py
    ├── test_search.py
    ├── test_download.py
    └── test_templates.py
```

## Dependencies

- `arxiv` - arXiv API wrapper (community library)
- `requests` - HTTP requests
- `pydantic` - Data validation
- `beautifulsoup4` - PDF metadata parsing

## Core Modules

### 1. Core Search Module

**Features**:
- Keyword search (all:, ti:, au:, abs:, co:)
- Category search (cs.AI, cs.LG, stat.ML, etc.)
- Author search
- ID lookup
- Date range filtering
- Batch download

**Output**: Structured JSON with paper metadata

### 2. Advanced Analysis Module

**Parser**:
- Extract metadata, abstract, sections, figures, tables, equations, references

**Evaluator**:
- Innovation score and novelty points
- Methodology strengths/weaknesses
- Key findings extraction
- Limitation identification

**Review Generator**:
- Reuses peer-review skill
- Generates structured review reports
- Provides revision suggestions

### 3. Pre-built Templates

| Template | Use Case | Output |
|----------|----------|--------|
| Literature Review | Quick domain overview | Summary + Bibliography |
| Deep Analysis | Comprehensive paper study | Analysis Report + Peer Review |
| Reproduction | Reproduce paper experiments | Code + Analysis Report |
| Survey | Write domain survey | Draft + Trend Analysis |

## Integration Points

- **peer-review**: Generate structured peer review reports
- **citation-management**: Export citations in standard formats
- **scientific-writing**: Assist with document generation
- **hypothesis-generation**: Support research hypothesis development

## Implementation Priority

1. **High Priority**: Basic search and download functionality
2. **Medium Priority**: Paper parsing and metadata extraction
3. **Medium Priority**: Deep analysis templates
4. **Low Priority**: Advanced templates (reproduction, survey)

## Success Criteria

- [ ] arxiv-database skill follows project conventions
- [ ] All templates produce valid output
- [ ] Integration with existing skills works correctly
- [ ] Tests pass for core functionality
