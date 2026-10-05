# Security and Access-Control Flow

The issue-resolution service performs authorization before
processing a support request.

## Security Flow

```text
                    Incoming Request
                           │
                           ▼
                    Request Validation
                           │
                           ▼
                    Authorization Check
                           │
                  ┌────────┴────────┐
                  │                 │
              Authorized        Unauthorized
                  │                 │
                  ▼                 ▼
          Issue Resolution      HTTP 403
                  │
                  ▼
              Retrieval
                  │
                  ▼
              Response