#!/usr/bin/env python3
"""
Document Creator Script
Creates documents in /docs with automatic category-based folder structure.

Usage:
    python create_doc.py <category> <filename> [--content <content>]

Examples:
    python create_doc.py plan feature-spec.md --content "# Feature Spec"
    python create_doc.py api user-api.md
    python create_doc.py requirements srs-v1.md
"""

import argparse
import os
from datetime import datetime
from pathlib import Path

# Document categories and their descriptions
CATEGORIES = {
    "plan": "Planning documents (feature plans, roadmaps, proposals)",
    "api": "API documentation",
    "requirements": "Requirements specifications (SRS, functional requirements)",
    "architecture": "Architecture and design documents",
    "readme": "README and project documentation",
    "guide": "User guides and tutorials",
    "reference": "Reference documentation",
}


def get_project_root() -> Path:
    """Find project root by looking for common root indicators."""
    current = Path.cwd()

    # Look for common project root indicators
    indicators = [".git", "package.json", "pyproject.toml", "Cargo.toml"]

    for parent in [current] + list(current.parents):
        for indicator in indicators:
            if (parent / indicator).exists():
                return parent

    return current


def create_document(category: str, filename: str, content: str = None) -> Path:
    """
    Create a document in the appropriate category folder.

    Args:
        category: Document category (plan, api, requirements, etc.)
        filename: Name of the document file
        content: Optional content to write to the file

    Returns:
        Path to the created document
    """
    project_root = get_project_root()
    docs_dir = project_root / "docs" / category

    # Create directory if it doesn't exist
    docs_dir.mkdir(parents=True, exist_ok=True)

    # Ensure filename has .md extension
    if not filename.endswith(".md"):
        filename = f"{filename}.md"

    filepath = docs_dir / filename

    # Generate default content if not provided
    if content is None:
        content = generate_default_content(category, filename)

    # Write content to file
    filepath.write_text(content, encoding="utf-8")

    return filepath


def generate_default_content(category: str, filename: str) -> str:
    """Generate default document content based on category."""
    title = filename.replace(".md", "").replace("-", " ").replace("_", " ").title()
    date = datetime.now().strftime("%Y-%m-%d")

    templates = {
        "plan": f"""# {title}

## Overview

[Brief description of the plan]

## Objectives

- Objective 1
- Objective 2

## Scope

### In Scope
-

### Out of Scope
-

## Timeline

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 1 | | Pending |

## Resources

## Risks and Mitigations

---
*Created: {date}*
""",
        "api": f"""# {title}

## Overview

## Base URL

`/api/v1`

## Endpoints

### GET /endpoint

**Description**:

**Parameters**:
| Name | Type | Required | Description |
|------|------|----------|-------------|

**Response**:
```json
{{}}
```

---
*Created: {date}*
""",
        "requirements": f"""# {title}

## 1. Introduction

### 1.1 Purpose

### 1.2 Scope

## 2. Functional Requirements

### FR-001:
- **Description**:
- **Priority**: High
- **Acceptance Criteria**:

## 3. Non-Functional Requirements

### NFR-001:
- **Category**: Performance
- **Description**:

---
*Created: {date}*
""",
        "architecture": f"""# {title}

## Overview

## System Components

## Data Flow

## Design Decisions

| Decision | Rationale | Alternatives Considered |
|----------|-----------|------------------------|

## Dependencies

---
*Created: {date}*
""",
        "readme": f"""# {title}

## Overview

## Installation

```bash
```

## Usage

## Configuration

## Contributing

---
*Created: {date}*
""",
        "guide": f"""# {title}

## Introduction

## Prerequisites

## Getting Started

### Step 1

### Step 2

## Troubleshooting

---
*Created: {date}*
""",
        "reference": f"""# {title}

## Overview

## Reference

---
*Created: {date}*
""",
    }

    return templates.get(category, f"# {title}\n\n---\n*Created: {date}*\n")


def list_categories():
    """Print available categories."""
    print("\nAvailable categories:")
    print("-" * 50)
    for cat, desc in CATEGORIES.items():
        print(f"  {cat:<15} {desc}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Create documents in /docs with category-based folder structure"
    )
    parser.add_argument(
        "category",
        nargs="?",
        help="Document category (plan, api, requirements, architecture, readme, guide, reference)",
    )
    parser.add_argument("filename", nargs="?", help="Document filename")
    parser.add_argument("--content", "-c", help="Document content (optional)")
    parser.add_argument(
        "--list", "-l", action="store_true", help="List available categories"
    )

    args = parser.parse_args()

    if args.list or not args.category:
        list_categories()
        return

    if not args.filename:
        print("Error: filename is required")
        parser.print_help()
        return

    # Validate category
    if args.category not in CATEGORIES:
        print(f"Error: Unknown category '{args.category}'")
        list_categories()
        return

    # Create the document
    filepath = create_document(args.category, args.filename, args.content)
    print(f"✅ Created: {filepath}")


if __name__ == "__main__":
    main()
