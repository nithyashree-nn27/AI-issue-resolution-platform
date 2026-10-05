# Enterprise Retrieval Integration

## Internship Architecture

During the internship, the issue-resolution workflow used an
enterprise knowledge-retrieval approach based on AWS Q Business
and a Confluence-backed knowledge source.

Conceptually:

```text
User Query
    ↓
Issue Resolution API
    ↓
AWS Q Business
    ↓
Enterprise Knowledge Source
    ↓
Confluence
    ↓
Relevant Context
    ↓
Contextual Response