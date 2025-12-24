---
name: doc-creator
description: Create technical documentation and requirements documents in /docs folder with automatic category-based structure. Use when users ask to generate, write, or create documentation such as API docs, README files, architecture documents, requirements specifications (SRS), functional specifications, or any technical documentation. Triggers on phrases like "create documentation", "write docs", "generate requirements document", "make API documentation", "write technical spec".
---

# Doc Creator

Technical documentation and requirements document generator. Creates documents in `/docs` folder with automatic category-based folder structure.

## Quick Start

Always use the `create_doc.py` script to create documents:

```bash
python scripts/create_doc.py <category> <filename> [--content <content>]
```

## Categories

| Category | Folder | Description |
|----------|--------|-------------|
| plan | /docs/plan | Planning documents, feature plans, roadmaps |
| api | /docs/api | API documentation |
| requirements | /docs/requirements | SRS, functional requirements |
| architecture | /docs/architecture | Architecture and design documents |
| readme | /docs/readme | README and project documentation |
| guide | /docs/guide | User guides and tutorials |
| reference | /docs/reference | Reference documentation |

## Workflow

1. Determine the appropriate category for the document
2. Run the script with category and filename
3. Edit the generated document with actual content

Example:
```bash
# Create a feature plan
python scripts/create_doc.py plan feature-auth.md

# Create API documentation
python scripts/create_doc.py api user-api.md

# Create requirements spec
python scripts/create_doc.py requirements srs-v1.md

# Create with custom content
python scripts/create_doc.py plan roadmap.md --content "# Roadmap\n\n## Q1 Goals"
```

## Templates

For detailed template formats, see:
- [references/api-docs-template.md](references/api-docs-template.md) - API documentation
- [references/readme-template.md](references/readme-template.md) - README files
- [references/srs-template.md](references/srs-template.md) - Requirements specifications

## Output Guidelines

- Use clear, concise language
- Include code examples where applicable
- Follow consistent formatting (Markdown)
- Add table of contents for documents > 100 lines
