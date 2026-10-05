# Testing Strategy

The project uses automated unit and integration tests to verify
the core issue-resolution workflow.

## Test Structure

```text
tests/
├── unit/
│   ├── test_authorization.py
│   ├── test_fallback.py
│   ├── test_issue_resolution.py
│   └── test_retriever.py
│
├── integration/
│   └── test_api.py
│
└── README.md