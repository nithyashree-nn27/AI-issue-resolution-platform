# System Architecture

## Overview

The AI Issue Resolution Platform was designed as an
API-driven enterprise support automation solution.

The system combines a Python backend, REST APIs,
AWS Q Business, Retrieval-Augmented Generation (RAG),
enterprise knowledge sources, role-based access control,
and fallback handling to provide contextual responses
to support queries.

## High-Level Flow

```text
Microsoft Teams
      |
      v
Microsoft Bot Framework
      |
      v
API Gateway
      |
      v
Backend / API Layer
      |
      +----------------------+
      |                      |
      v                      v
     RBAC              Query Processing
                             |
                             v
                       AWS Q Business
                             |
                             v
                          RAG
                             |
                             v
                       Confluence
                             |
                             v
                    Contextual Resolution
                             |
                             v
                       Fallback
                             |
                             v
                    Microsoft Teams