# From Idea to Production: A Complete Pipeline Development Guide

## Purpose

This document provides a systematic process for building data pipelines—from initial concept through production-ready code. It's designed for developers who want to learn best practices *as part of the build process*, not as a prerequisite.

The key principle: **understand before you implement, implement before you optimize**.

---

## Table of Contents

1. [Phase 1: Idea Clarification](#phase-1-idea-clarification)
2. [Phase 2: Technical Research](#phase-2-technical-research)
3. [Phase 3: Architecture Design](#phase-3-architecture-design)
4. [Phase 4: Interface Definition](#phase-4-interface-definition)
5. [Phase 5: Project Setup](#phase-5-project-setup)
6. [Phase 6: Implementation](#phase-6-implementation)
7. [Phase 7: Testing & Validation](#phase-7-testing--validation)
8. [Phase 8: Refinement & Production Readiness](#phase-8-refinement--production-readiness)
9. [Appendix: Research Prompt Templates](#appendix-research-prompt-templates)
10. [Appendix: Decision Frameworks](#appendix-decision-frameworks)

---

## Phase 1: Idea Clarification

**Goal:** Transform a vague idea into a concrete problem statement with clear boundaries.

### 1.1 The Problem Statement Template

Answer these questions in writing before doing anything else:

```markdown
## Problem Statement

### What problem am I solving?
[One sentence describing the core problem]

### Who/what is the input?
[What data do I have? Where does it come from? What format?]

### Who/what is the output?
[What do I want at the end? A report? A database? An API response?]

### What does success look like?
[How will I know this works? Be specific.]

### What are the constraints?
- Data size: [rough estimate]
- Frequency: [one-time, daily, real-time?]
- Environment: [local only, cloud, shared?]
- Timeline: [when do I need this working?]
```

### 1.2 Scope Boundaries

Define what's IN and OUT of scope explicitly:

```markdown
## Scope

### In Scope (Version 1)
- [ ] Feature/capability 1
- [ ] Feature/capability 2
- [ ] Feature/capability 3

### Out of Scope (Future Versions)
- [ ] Nice-to-have 1
- [ ] Nice-to-have 2

### Non-Goals (Will never do)
- [ ] Thing that seems related but isn't part of this project
```

### 1.3 Questions to Surface Unknowns

Before moving to research, list everything you don't know:

```markdown
## Open Questions

### Technical Unknowns
- What's the best way to [specific technical challenge]?
- How do I handle [edge case]?
- What library/tool is appropriate for [task]?

### Domain Unknowns
- What does [domain term] actually mean?
- How is [process] typically done in industry?

### Data Unknowns
- What's the actual structure of my input data?
- How dirty is the data? What cleaning will I need?
- How large is this likely to get?
```

---

## Phase 2: Technical Research

**Goal:** Understand the landscape of solutions before committing to an approach.

### 2.1 Research Categories

For any data pipeline, research these areas systematically:

#### Data Storage & Access
- **Questions to answer:**
  - Where should raw data live? Processed data?
  - Do I need a database? What kind?
  - How will I query this data later?
  
- **Research prompts:**
  ```
  I'm building [brief description]. My data is [size estimate], 
  updated [frequency], and I need to [query patterns].
  
  Compare these storage options for my use case:
  1. Flat files (CSV, Parquet, JSON)
  2. SQLite
  3. PostgreSQL
  4. [Other relevant options]
  
  For each, explain: when it's appropriate, limitations, 
  and complexity to set up.
  ```

#### Data Processing
- **Questions to answer:**
  - What transformations do I need?
  - What's the appropriate tool (pandas, polars, SQL)?
  - How do I handle data that doesn't fit in memory?

- **Research prompts:**
  ```
  I need to [list transformations] on data that is [size].
  
  What's the modern best practice for this in Python?
  Include: recommended libraries, patterns to follow, 
  patterns to avoid, and how to handle [specific edge case].
  ```

#### Domain-Specific Techniques (e.g., NLP)
- **Questions to answer:**
  - What are the standard approaches to my problem?
  - What's "good enough" vs. state-of-the-art?
  - What are the tradeoffs (accuracy vs. speed vs. complexity)?

- **Research prompts:**
  ```
  I'm working on [NLP/ML task] for [use case].
  
  Give me a progression of approaches from simplest to most complex:
  1. Baseline approach (fast to implement, good enough for prototyping)
  2. Intermediate approach (better results, reasonable complexity)
  3. Advanced approach (best results, significant complexity)
  
  For each: explain the technique, when to use it, required libraries,
  and rough implementation effort.
  ```

#### Embeddings & Vector Storage
- **Questions to answer:**
  - Do I need embeddings? For what purpose?
  - How do I store them efficiently?
  - How do I avoid recomputing them?

- **Research prompts:**
  ```
  I need to [semantic search / similarity matching / clustering] 
  on [data type] data. Expected volume: [count] items.
  
  Explain:
  1. What embedding model is appropriate (local vs. API)?
  2. How to store embeddings to avoid recomputation
  3. FAISS vs. ChromaDB vs. other options for my scale
  4. How to handle incremental updates (new data added over time)
  ```

### 2.2 Complexity Calibration

**Critical question:** What's the right level of complexity for THIS project?

Use this framework:

| Factor | Simple Solution | Complex Solution |
|--------|-----------------|------------------|
| Data size | < 100MB | > 1GB |
| Users | Just me | Multiple/team |
| Lifespan | Days/weeks | Months/years |
| Updates | Rare/manual | Frequent/automated |
| Errors | I can fix them | Need to be handled gracefully |

**Rule of thumb:** Start with the simplest solution that could work. Add complexity only when you hit a concrete limitation, not because it "might" be needed.

### 2.3 Research Output Template

Document your research findings:

```markdown
## Technical Decisions

### Data Storage: [Choice]
- **Why:** [1-2 sentence justification]
- **Alternatives considered:** [What else you looked at]
- **When to revisit:** [What would make you change this decision]

### Processing Approach: [Choice]
- **Why:** [1-2 sentence justification]
- **Key patterns to follow:** [List]
- **Patterns to avoid:** [List]

### [Domain-Specific]: [Choice]
- **Why:** [1-2 sentence justification]
- **Tradeoffs accepted:** [What you're giving up]

### Libraries/Dependencies
| Purpose | Library | Version | Why |
|---------|---------|---------|-----|
| Data manipulation | pandas | >=2.0 | Standard, good for [size] |
| Embeddings | sentence-transformers | latest | Local, no API costs |
| Vector storage | faiss-cpu | latest | Fast, persistent to disk |
```

---

## Phase 3: Architecture Design

**Goal:** Design the data flow and component boundaries before writing code.

### 3.1 Data Flow Diagram

Sketch your pipeline as a series of transformations:

```
[Input Source] 
    → [Ingestion] 
    → [Validation] 
    → [Processing/Transformation] 
    → [Analysis/ML] 
    → [Output/Storage]
```

For each arrow, define:
- What data format goes in
- What data format comes out
- What can go wrong

### 3.2 Component Responsibilities

Define what each module does and—critically—what it does NOT do:

```markdown
## Module: Ingestion

### Responsibility
Load raw data from source files/APIs into memory.

### Does
- Read CSV/JSON/Parquet files
- Validate file existence
- Handle encoding issues
- Log source and row counts

### Does Not
- Clean data (that's processing)
- Transform schema (that's processing)
- Store results (that's output)

### Inputs
- file_path: str or Path
- Optional: config dict for parsing options

### Outputs
- pandas DataFrame with raw data
- Raises FileNotFoundError or ValueError on problems

### Error Handling
- Missing file → raise with clear message
- Malformed file → raise with line number if possible
- Empty file → return empty DataFrame with warning log
```

Repeat this for each module in your pipeline.

### 3.3 Data Contracts

Define the shape of data at each stage:

```markdown
## Data Contracts

### Raw Input Schema
| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| id | str | No | Unique identifier |
| timestamp | str | No | ISO format datetime |
| content | str | Yes | Main text content |
| category | str | Yes | Optional category label |

### Cleaned Schema (after processing)
| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| id | str | No | Unique identifier |
| timestamp | datetime | No | Parsed datetime |
| content | str | No | Cleaned text (empty string if null) |
| category | str | No | Category or "uncategorized" |
| content_length | int | No | Character count |

### Analysis Output Schema
| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| id | str | No | Unique identifier |
| embedding | np.array | No | 384-dim vector |
| cluster_id | int | No | Assigned cluster |
| sentiment | float | No | -1 to 1 score |
```

---

## Phase 4: Interface Definition

**Goal:** Define function signatures and data types BEFORE implementation.

### 4.1 Why Interfaces First?

This is the key to making Copilot work well. When you define:
- Function name
- Input types
- Output types
- Docstring with behavior description

...you've done the thinking. Copilot just fills in the implementation.

### 4.2 Interface Template

For each function, write this BEFORE implementing:

```python
def function_name(
    param1: InputType1,
    param2: InputType2,
    *,  # Force keyword arguments after this
    optional_param: OptionalType = default_value,
) -> OutputType:
    """One-line description of what this function does.
    
    Longer description if needed, explaining the transformation
    or business logic involved.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        optional_param: Description and when to use non-default
    
    Returns:
        Description of return value, including structure if complex
    
    Raises:
        ValueError: When [specific condition]
        FileNotFoundError: When [specific condition]
    
    Example:
        >>> result = function_name(input1, input2)
        >>> print(result)
        expected_output
    """
    # TODO: Implementation
    raise NotImplementedError
```

### 4.3 Module Interface Example

```python
# src/call_analysis/processing/cleaners.py
"""Data cleaning functions for call analysis pipeline.

All functions in this module:
- Take a DataFrame as first argument
- Return a new DataFrame (never modify in place)
- Handle edge cases: empty DataFrames, missing columns
- Log warnings for data quality issues
"""

from pandas import DataFrame


def remove_duplicates(
    df: DataFrame,
    *,
    subset: list[str] | None = None,
    keep: str = "first",
) -> DataFrame:
    """Remove duplicate rows from DataFrame.
    
    Args:
        df: Input DataFrame
        subset: Columns to consider for duplicates. 
                If None, uses all columns.
        keep: Which duplicate to keep ('first', 'last', False)
    
    Returns:
        DataFrame with duplicates removed.
        Logs count of removed rows.
    
    Raises:
        ValueError: If subset contains columns not in df
    
    Example:
        >>> clean_df = remove_duplicates(df, subset=['id'])
    """
    raise NotImplementedError


def normalize_text_column(
    df: DataFrame,
    column: str,
    *,
    lowercase: bool = True,
    strip_whitespace: bool = True,
    remove_special_chars: bool = False,
) -> DataFrame:
    """Normalize text in specified column.
    
    Args:
        df: Input DataFrame
        column: Name of column to normalize
        lowercase: Convert to lowercase
        strip_whitespace: Remove leading/trailing whitespace
        remove_special_chars: Remove non-alphanumeric characters
    
    Returns:
        DataFrame with normalized text column.
        Original column is replaced (not added as new column).
    
    Raises:
        ValueError: If column not in DataFrame
        TypeError: If column is not string type
    
    Example:
        >>> df = normalize_text_column(df, 'content', lowercase=True)
    """
    raise NotImplementedError


def fill_missing_values(
    df: DataFrame,
    fill_rules: dict[str, any],
) -> DataFrame:
    """Fill missing values according to specified rules.
    
    Args:
        df: Input DataFrame
        fill_rules: Dict mapping column names to fill values.
                   Use callable for dynamic fills (e.g., lambda: datetime.now())
    
    Returns:
        DataFrame with missing values filled.
        Logs count of fills per column.
    
    Raises:
        ValueError: If fill_rules contains columns not in df
    
    Example:
        >>> rules = {
        ...     'category': 'uncategorized',
        ...     'count': 0,
        ...     'processed_at': lambda: datetime.now()
        ... }
        >>> df = fill_missing_values(df, rules)
    """
    raise NotImplementedError
```

### 4.4 Type Definitions

For complex data structures, define types explicitly:

```python
# src/call_analysis/types.py
"""Type definitions for call analysis pipeline."""

from dataclasses import dataclass
from datetime import datetime
from typing import TypedDict

import numpy as np
from numpy.typing import NDArray


# For structured dictionaries
class CallRecord(TypedDict):
    """Single call record from raw data."""
    id: str
    timestamp: str
    duration_seconds: int
    transcript: str
    agent_id: str


class AnalysisResult(TypedDict):
    """Result of analyzing a single call."""
    id: str
    sentiment_score: float
    topics: list[str]
    summary: str
    embedding: NDArray[np.float32]


# For objects with behavior
@dataclass
class ProcessingConfig:
    """Configuration for processing pipeline."""
    input_path: str
    output_path: str
    batch_size: int = 100
    embedding_model: str = "all-MiniLM-L6-v2"
    
    def validate(self) -> None:
        """Validate configuration values."""
        if self.batch_size < 1:
            raise ValueError("batch_size must be positive")
```

---

## Phase 5: Project Setup

**Goal:** Create the project structure and configuration files.

### 5.1 Directory Structure

```
project_name/
├── .github/
│   ├── copilot-instructions.md       # Global context
│   ├── prompts/                      # Reusable prompts
│   │   ├── add-function.prompt.md
│   │   └── review-code.prompt.md
│   └── instructions/                 # Auto-applied by file pattern
│       ├── ingestion.instructions.md
│       ├── processing.instructions.md
│       ├── analysis.instructions.md
│       └── tests.instructions.md
│
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── main.py                   # Orchestration / entry point
│       ├── config.py                 # Settings and configuration
│       ├── types.py                  # Type definitions
│       │
│       ├── ingestion/
│       │   ├── __init__.py
│       │   └── loaders.py
│       │
│       ├── processing/
│       │   ├── __init__.py
│       │   ├── cleaners.py
│       │   └── transformers.py
│       │
│       ├── analysis/
│       │   ├── __init__.py
│       │   ├── embeddings.py
│       │   └── insights.py
│       │
│       ├── output/
│       │   ├── __init__.py
│       │   └── exporters.py
│       │
│       └── utils/
│           ├── __init__.py
│           ├── logging.py
│           └── validators.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                   # Shared fixtures
│   ├── test_ingestion/
│   ├── test_processing/
│   ├── test_analysis/
│   └── test_output/
│
├── data/
│   ├── raw/                          # Original data (never modify)
│   ├── processed/                    # Intermediate results
│   └── output/                       # Final outputs
│
├── notebooks/                        # Exploration (optional)
├── scripts/                          # CLI entry points
│
├── pyproject.toml
└── README.md
```

### 5.2 Configuration Files

#### pyproject.toml

```toml
[project]
name = "project_name"
version = "0.1.0"
description = "Brief description"
requires-python = ">=3.11"
dependencies = [
    # Core
    "pandas>=2.0",
    "pydantic>=2.0",
    
    # Add your researched dependencies here
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-cov>=4.0",
    "ruff>=0.4",
    "mypy>=1.0",
]

[tool.ruff]
line-length = 88
select = ["E", "F", "I", "UP", "B", "SIM"]
ignore = ["E501"]  # Line length handled separately

[tool.ruff.isort]
known-first-party = ["project_name"]

[tool.mypy]
python_version = "3.11"
strict = true
ignore_missing_imports = true

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --tb=short"
```

#### .github/copilot-instructions.md

```markdown
# Project: [Project Name]

## Overview
[2-3 sentences describing what this project does]

## Tech Stack
- Python 3.11+
- pandas [version] for data manipulation
- [Other libraries from your research]

## Project Structure
- src/project_name/ — main package
  - ingestion/ — data loading from [sources]
  - processing/ — cleaning, transformation
  - analysis/ — [domain-specific analysis]
  - output/ — exports and reports
- tests/ — mirrors src/ structure
- data/ — raw, processed, output subdirectories

## Code Conventions
- Type hints on ALL function signatures
- Google-style docstrings with Args, Returns, Raises, Example
- Functions do ONE thing
- Return new objects; never modify inputs in place
- Validate inputs at function boundaries
- Use early returns for error conditions

## Error Handling
- Raise specific exceptions (ValueError, TypeError, FileNotFoundError)
- Include actionable error messages
- Log errors before raising
- Never silently ignore errors

## Data Conventions
- Raw data in data/raw/ is NEVER modified
- DataFrames are immutable—always return new copies
- Null handling: [your decision from research]
- Date parsing: [your standard format]

## Testing Requirements
- Every public function needs tests
- Test happy path, edge cases, error cases
- Use pytest fixtures for test data
- Mock external dependencies

## Dependencies
[List from your research with brief "why"]
```

### 5.3 Module-Specific Instructions

Create one for each module. Example:

#### .github/instructions/analysis.instructions.md

```markdown
---
applyTo: "src/project_name/analysis/**"
---

## Analysis Module Guidelines

This module contains domain-specific analysis logic.

### Embeddings (embeddings.py)
- Use [model name] for embeddings
- Cache embeddings to [location] to avoid recomputation
- Check cache before computing new embeddings
- Handle batching for large datasets

### Insights (insights.py)
- Input: processed DataFrame with embeddings
- Output: DataFrame with analysis columns added
- Each analysis function adds ONE type of insight
- Compose multiple analyses in main.py

### Performance
- For >10k records, use batching
- Log progress for long-running operations
- Provide estimated time remaining when possible
```

---

## Phase 6: Implementation

**Goal:** Implement the pipeline module by module, with tests.

### 6.1 Implementation Order

Build from the edges inward:

1. **Types and configuration** — Define your data structures
2. **Utilities** — Logging, validation helpers
3. **Ingestion** — Get data into the system
4. **Output** — Get results out of the system
5. **Processing** — Transform data
6. **Analysis** — Domain-specific logic
7. **Main** — Wire everything together

Why this order? You can test each layer with simple inputs/outputs before connecting them.

### 6.2 Implementation Workflow

For each function:

```
1. Write the interface (signature + docstring)
2. Write 2-3 tests for expected behavior
3. Run tests (they should fail)
4. Implement the function
5. Run tests (they should pass)
6. Add edge case tests
7. Implement edge case handling
8. Run all tests
9. Move to next function
```

### 6.3 Using Copilot Effectively

**Before asking Copilot to implement:**
- Interface is fully defined (signature, types, docstring)
- You understand what the function should do
- You could explain the algorithm in plain English

**Prompting pattern:**
```
Implement this function according to its docstring.
Follow the project conventions in copilot-instructions.md.
Handle these edge cases: [list them]
```

**After Copilot generates:**
1. Read every line—do you understand it?
2. Would you have written it similarly?
3. Ask: "What edge cases does this miss?"
4. Ask: "Review this for production readiness"
5. Run your tests

### 6.4 Common Implementation Patterns

#### Loading Data with Caching

```python
def load_with_cache(
    source_path: Path,
    cache_path: Path,
    loader_fn: Callable[[Path], DataFrame],
    *,
    force_reload: bool = False,
) -> DataFrame:
    """Load data, using cache if available and current.
    
    Cache is invalidated if source file is newer than cache.
    """
    if not force_reload and cache_path.exists():
        source_mtime = source_path.stat().st_mtime
        cache_mtime = cache_path.stat().st_mtime
        
        if cache_mtime > source_mtime:
            logger.info(f"Loading from cache: {cache_path}")
            return pd.read_parquet(cache_path)
    
    logger.info(f"Loading from source: {source_path}")
    df = loader_fn(source_path)
    
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(cache_path)
    logger.info(f"Cached to: {cache_path}")
    
    return df
```

#### Embedding with Cache Check

```python
def get_or_compute_embeddings(
    texts: list[str],
    ids: list[str],
    cache_path: Path,
    model: SentenceTransformer,
) -> dict[str, NDArray]:
    """Get embeddings, computing only what's not cached."""
    
    # Load existing cache
    if cache_path.exists():
        with open(cache_path, 'rb') as f:
            cache = pickle.load(f)
    else:
        cache = {}
    
    # Find what needs computing
    to_compute = [(id_, text) for id_, text in zip(ids, texts) 
                  if id_ not in cache]
    
    if to_compute:
        logger.info(f"Computing {len(to_compute)} new embeddings")
        new_ids, new_texts = zip(*to_compute)
        new_embeddings = model.encode(list(new_texts), show_progress_bar=True)
        
        for id_, embedding in zip(new_ids, new_embeddings):
            cache[id_] = embedding
        
        # Save updated cache
        with open(cache_path, 'wb') as f:
            pickle.dump(cache, f)
    
    return {id_: cache[id_] for id_ in ids}
```

#### Pipeline Step with Logging

```python
def pipeline_step(
    step_name: str,
) -> Callable:
    """Decorator for pipeline steps with logging and timing."""
    def decorator(fn: Callable) -> Callable:
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            logger.info(f"Starting: {step_name}")
            start = time.time()
            
            try:
                result = fn(*args, **kwargs)
                elapsed = time.time() - start
                logger.info(f"Completed: {step_name} ({elapsed:.2f}s)")
                return result
            except Exception as e:
                logger.error(f"Failed: {step_name} - {e}")
                raise
        
        return wrapper
    return decorator
```

---

## Phase 7: Testing & Validation

**Goal:** Ensure each component works correctly in isolation and together.

### 7.1 Test Categories

#### Unit Tests
Test individual functions with controlled inputs:

```python
# tests/test_processing/test_cleaners.py

def test_remove_duplicates_removes_exact_duplicates():
    """Exact duplicate rows should be removed."""
    df = pd.DataFrame({
        'id': ['1', '1', '2'],
        'value': ['a', 'a', 'b']
    })
    
    result = remove_duplicates(df)
    
    assert len(result) == 2
    assert result['id'].tolist() == ['1', '2']


def test_remove_duplicates_with_subset():
    """Only specified columns considered for duplicates."""
    df = pd.DataFrame({
        'id': ['1', '1', '2'],
        'value': ['a', 'b', 'c']  # Different values, same id
    })
    
    result = remove_duplicates(df, subset=['id'])
    
    assert len(result) == 2


def test_remove_duplicates_empty_dataframe():
    """Empty DataFrame returns empty DataFrame."""
    df = pd.DataFrame({'id': [], 'value': []})
    
    result = remove_duplicates(df)
    
    assert len(result) == 0
    assert list(result.columns) == ['id', 'value']


def test_remove_duplicates_invalid_subset_raises():
    """Invalid subset column raises ValueError."""
    df = pd.DataFrame({'id': ['1'], 'value': ['a']})
    
    with pytest.raises(ValueError, match="not_a_column"):
        remove_duplicates(df, subset=['not_a_column'])
```

#### Integration Tests
Test components working together:

```python
# tests/test_integration.py

def test_load_and_process_pipeline(tmp_path):
    """Data flows correctly from ingestion through processing."""
    # Setup: Create test file
    test_data = pd.DataFrame({
        'id': ['1', '2', '2'],
        'content': ['  Hello  ', 'World', 'World']
    })
    input_file = tmp_path / "input.csv"
    test_data.to_csv(input_file, index=False)
    
    # Execute pipeline steps
    raw = load_csv(input_file)
    cleaned = remove_duplicates(raw, subset=['id'])
    normalized = normalize_text_column(cleaned, 'content')
    
    # Verify
    assert len(normalized) == 2
    assert normalized.loc[0, 'content'] == 'hello'
```

#### Data Validation Tests
Test that real data matches expectations:

```python
# tests/test_data_validation.py

def test_raw_data_schema():
    """Raw data has expected columns and types."""
    df = load_csv(Path("data/raw/sample.csv"))
    
    required_columns = {'id', 'timestamp', 'content'}
    assert required_columns.issubset(set(df.columns))
    
    assert df['id'].dtype == 'object'
    assert df['id'].notna().all()


def test_no_data_loss_through_pipeline():
    """All valid records make it through processing."""
    raw = load_csv(Path("data/raw/sample.csv"))
    valid_raw_count = len(raw[raw['id'].notna()])
    
    processed = run_full_processing(raw)
    
    # May have fewer due to deduplication, but not more
    assert len(processed) <= valid_raw_count
```

### 7.2 Test Fixtures

```python
# tests/conftest.py

import pytest
import pandas as pd
from pathlib import Path


@pytest.fixture
def sample_df():
    """Basic DataFrame for testing."""
    return pd.DataFrame({
        'id': ['1', '2', '3'],
        'content': ['Hello world', 'Test content', 'More text'],
        'timestamp': ['2024-01-01', '2024-01-02', '2024-01-03'],
    })


@pytest.fixture
def empty_df():
    """Empty DataFrame with expected schema."""
    return pd.DataFrame({
        'id': pd.Series([], dtype='str'),
        'content': pd.Series([], dtype='str'),
        'timestamp': pd.Series([], dtype='str'),
    })


@pytest.fixture
def df_with_nulls():
    """DataFrame with various null patterns."""
    return pd.DataFrame({
        'id': ['1', '2', None],
        'content': ['Hello', None, 'World'],
        'timestamp': [None, '2024-01-02', '2024-01-03'],
    })


@pytest.fixture
def tmp_data_dir(tmp_path):
    """Temporary directory structure matching project layout."""
    (tmp_path / "raw").mkdir()
    (tmp_path / "processed").mkdir()
    (tmp_path / "output").mkdir()
    return tmp_path
```

### 7.3 Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/project_name --cov-report=term-missing

# Run specific test file
pytest tests/test_processing/test_cleaners.py

# Run tests matching pattern
pytest -k "test_remove_duplicates"

# Run with verbose output
pytest -v

# Stop on first failure
pytest -x
```

---

## Phase 8: Refinement & Production Readiness

**Goal:** Polish the implementation and prepare for ongoing use.

### 8.1 Code Quality Checklist

```markdown
## Pre-Production Checklist

### Code Quality
- [ ] All functions have type hints
- [ ] All public functions have docstrings
- [ ] No unused imports or variables (ruff check)
- [ ] Consistent code style (ruff format)
- [ ] No type errors (mypy)

### Testing
- [ ] All tests pass
- [ ] Test coverage > 80% for core modules
- [ ] Edge cases covered
- [ ] Integration test exists

### Error Handling
- [ ] All error paths have tests
- [ ] Error messages are actionable
- [ ] No bare except clauses
- [ ] Logging configured for errors

### Documentation
- [ ] README explains how to run
- [ ] Configuration options documented
- [ ] Example usage provided

### Data Safety
- [ ] Raw data never modified
- [ ] Intermediate results can be regenerated
- [ ] No hardcoded paths
- [ ] Credentials not in code
```

### 8.2 Performance Review

Questions to ask before considering done:

```markdown
## Performance Check

### Memory
- [ ] Tested with realistic data size
- [ ] No memory leaks in long-running operations
- [ ] Large files processed in chunks if needed

### Speed
- [ ] Acceptable runtime for expected data size
- [ ] Caching implemented where beneficial
- [ ] No unnecessary recomputation

### Scalability
- [ ] What happens with 10x data?
- [ ] What's the bottleneck?
- [ ] Is the bottleneck acceptable?
```

### 8.3 Logging Configuration

```python
# src/project_name/utils/logging.py

import logging
import sys
from pathlib import Path


def setup_logging(
    level: int = logging.INFO,
    log_file: Path | None = None,
) -> logging.Logger:
    """Configure logging for the application.
    
    Args:
        level: Logging level (default INFO)
        log_file: Optional file path for logs
    
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger("project_name")
    logger.setLevel(level)
    
    # Console handler
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(level)
    console_format = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console.setFormatter(console_format)
    logger.addHandler(console)
    
    # File handler (if specified)
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_format = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(funcName)s:%(lineno)d | %(message)s'
        )
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)
    
    return logger
```

### 8.4 Main Entry Point Pattern

```python
# src/project_name/main.py

"""Main entry point for the pipeline."""

import argparse
import sys
from pathlib import Path

from .config import load_config
from .utils.logging import setup_logging
from .ingestion import load_data
from .processing import clean_data, transform_data
from .analysis import analyze_data
from .output import export_results


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Run the data analysis pipeline"
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config.yaml"),
        help="Path to configuration file"
    )
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to input data"
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Path for output results"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    return parser.parse_args()


def main() -> int:
    """Run the pipeline.
    
    Returns:
        Exit code (0 for success, 1 for failure)
    """
    args = parse_args()
    
    # Setup
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logger = setup_logging(level=log_level)
    
    try:
        logger.info("Starting pipeline")
        config = load_config(args.config)
        
        # Pipeline steps
        logger.info("Loading data")
        raw_data = load_data(args.input)
        
        logger.info("Cleaning data")
        cleaned = clean_data(raw_data, config)
        
        logger.info("Transforming data")
        transformed = transform_data(cleaned, config)
        
        logger.info("Analyzing data")
        results = analyze_data(transformed, config)
        
        logger.info("Exporting results")
        export_results(results, args.output)
        
        logger.info("Pipeline completed successfully")
        return 0
        
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        return 1
    except ValueError as e:
        logger.error(f"Invalid data: {e}")
        return 1
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

---

## Appendix: Research Prompt Templates

Use these to research unfamiliar technical areas:

### General Framework Research

```
I'm building [brief description] in Python.

I need to understand [specific topic]. Please explain:
1. What is this and why would I use it?
2. What are the common approaches/libraries?
3. For my use case ([specifics]), which approach fits best?
4. What are the gotchas/common mistakes?
5. Show me a minimal working example

Keep it practical—I want to implement this, not write a paper about it.
```

### "Should I Use X?" Decision

```
I'm considering using [technology/library] for [purpose].

My constraints:
- Data size: [estimate]
- Frequency: [how often]
- Team size: [just me / small team / etc.]
- This is: [local only / needs to be shared / production service]

Is [technology] the right choice? If not, what should I use instead?
Give me the honest tradeoffs, not just the marketing pitch.
```

### Best Practices Research

```
What are the current best practices (2024-2025) for [specific task] in Python?

I want to know:
1. The "don't think, just do this" default approach
2. When that default doesn't apply
3. Common anti-patterns to avoid
4. Recommended libraries and why

Be specific and opinionated. I want guidance, not a literature review.
```

### Learning a Library

```
I need to use [library] for [task]. I've never used it before.

Give me:
1. The core concepts I need to understand (not everything, just what matters)
2. A minimal example that does [specific thing I need]
3. The most common mistakes beginners make
4. Where to look when I get stuck (docs, common error messages)
```

---

## Appendix: Decision Frameworks

### When to Use a Database vs. Files

| Use Files When | Use SQLite When | Use PostgreSQL When |
|----------------|-----------------|---------------------|
| Data fits in memory | Need SQL queries | Multiple concurrent users |
| One-time analysis | Need transactions | High availability required |
| Simple read patterns | Single user/process | Complex relationships |
| Data is write-once | Local development | Production service |

### When to Add Complexity

**Add it when:**
- You've hit a concrete limitation
- You have a test proving the current approach fails
- The cost of NOT adding it is measurable

**Don't add it when:**
- It "might" be needed later
- It's what "real" projects use
- It's more interesting to build

### Naming Conventions

| Thing | Convention | Example |
|-------|------------|---------|
| Module | lowercase, underscores | `data_loaders.py` |
| Function | lowercase, underscores | `load_csv_data()` |
| Class | PascalCase | `DataProcessor` |
| Constant | UPPERCASE, underscores | `MAX_BATCH_SIZE` |
| Private | Leading underscore | `_internal_helper()` |

---

## Quick Reference: Implementation Checklist

For each module:

```markdown
- [ ] Types defined in types.py
- [ ] Interfaces defined (signatures + docstrings)
- [ ] Tests written for expected behavior
- [ ] Implementation complete
- [ ] Edge case tests added
- [ ] Edge cases handled
- [ ] All tests pass
- [ ] Code formatted (ruff format)
- [ ] Type checked (mypy)
- [ ] Docstrings complete
```

For the project:

```markdown
- [ ] copilot-instructions.md complete
- [ ] Module-specific instructions created
- [ ] pyproject.toml configured
- [ ] README documents usage
- [ ] All modules implemented
- [ ] Integration tests pass
- [ ] Performance acceptable
- [ ] Logging configured
```