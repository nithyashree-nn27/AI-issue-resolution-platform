# Request Flow

## Knowledge-Based Issue Resolution

1. A support user submits a query through Microsoft Teams.
2. The request enters the backend API layer implemented using FastAPI.
3. Authentication and role-based access control determine whether the request can access protected support information.
4. The query is processed and routed according to its intent.
5. AWS Q Business performs knowledge retrieval using the enterprise knowledge source.
6. Relevant knowledge from Confluence is used to provide contextual information.
7. The resolution workflow generates an appropriate response.
8. Ambiguous or unsupported requests follow the fallback path.
9. The response is returned to the user through the support interface.

## Order Information Workflow

For order-related queries, the backend can route the request toward an S3-based data lookup workflow.

```text
User Query
    ↓
FastAPI
    ↓
Issue / Intent Processing
    ↓
Order Query
    ↓
Amazon S3
    ↓
Order Information
    ↓
Response