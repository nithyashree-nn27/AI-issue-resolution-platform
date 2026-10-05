# AWS Infrastructure

This directory documents the AWS components used as part of the
internship architecture for the AI Issue Resolution Platform.

## AWS Components

### AWS Q Business

Used for enterprise knowledge retrieval and AI-powered interaction
with the organization's knowledge sources.

### AWS Lambda

Used as part of the serverless processing architecture for
backend issue-resolution workflows.

### Amazon API Gateway

Used as the API-facing layer within the serverless architecture.

### Amazon S3

Used for object storage and data lookup workflows, including
the order-data workflow represented in the architecture.

### Confluence

Used as the enterprise knowledge source connected to the
knowledge-retrieval workflow.

## Architecture

```text
Microsoft Teams
       │
       ▼
API / Backend Layer
       │
       ├───────────────┐
       ▼               ▼
AWS Q Business        S3
       │               │
       ▼               ▼
Confluence          Order Data
       │               │
       └───────┬───────┘
               ▼
       Contextual Response