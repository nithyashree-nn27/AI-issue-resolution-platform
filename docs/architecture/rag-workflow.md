# RAG Workflow

## Enterprise Internship Workflow

The internship solution used an enterprise knowledge-retrieval
workflow centered around AWS Q Business and a Confluence-backed
knowledge source.

```text
                    User Query
                        │
                        ▼
              Issue Resolution API
                        │
                        ▼
                Query Processing
                        │
                        ▼
                 AWS Q Business
                        │
                        ▼
             Enterprise Knowledge
                  Source
                        │
                        ▼
                  Confluence
                        │
                        ▼
              Relevant Context
                        │
                        ▼
              Contextual Response
                        │
                        ▼
                    User