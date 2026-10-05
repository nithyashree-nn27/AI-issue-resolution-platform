# AI Issue Resolution Platform

### Enterprise AI-powered support automation using RAG, FastAPI & AWS

<p align="center">

<img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/FastAPI-REST%20API-009688?logo=fastapi&logoColor=white" alt="FastAPI"/>
<img src="https://img.shields.io/badge/AWS-Cloud-232F3E?logo=amazonaws&logoColor=white" alt="AWS"/>
<img src="https://img.shields.io/badge/AWS%20Q%20Business-AI%20Retrieval-FF9900?logo=amazonaws&logoColor=white" alt="AWS Q Business"/>
<img src="https://img.shields.io/badge/RAG-Knowledge%20Retrieval-7B61FF" alt="RAG"/>
<img src="https://img.shields.io/badge/RBAC-Authorization-2EA44F" alt="RBAC"/>
<img src="https://img.shields.io/badge/Tests-18%20passing-success" alt="Tests"/>
<img src="https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white" alt="GitHub Actions"/>

</p>

---

> ## Portfolio / Internship Showcase
>
> This repository is a sanitized technical showcase of an
> AI-powered issue-resolution solution I contributed to during
> my software engineering internship at **Titan Company Limited
> (TATA)**.
>
> Production credentials, proprietary knowledge-base content,
> customer/order data, internal URLs, and organization-specific
> infrastructure configuration have been excluded.
>
> The repository contains representative implementation code,
> synthetic data, architecture documentation, workflows, and
> engineering patterns intended to demonstrate the solution and
> my contributions.

---

## Overview

The **AI Issue Resolution Platform** is an enterprise support
automation workflow designed to help users resolve recurring
technical and operational issues through knowledge retrieval
and contextual responses.

The internship solution combined AI-powered enterprise
knowledge retrieval with API-based issue processing,
authorization, fallback handling, and enterprise integrations.

The public repository provides a runnable, sanitized
demonstration of these engineering concepts using synthetic
knowledge data.

---

## Problem

Enterprise support teams frequently receive repetitive issues
that require users or support engineers to manually search
through existing documentation.

This creates challenges such as:

- Repeated manual investigation
- Slow access to relevant knowledge
- Inconsistent responses
- Difficulty handling ambiguous queries
- Unnecessary escalation of known issues

The objective was to create a workflow capable of retrieving
relevant enterprise knowledge and returning contextual support
responses.

---

## Solution

The solution introduced an AI-powered issue-resolution workflow
that:

1. Receives a support request.
2. Validates the incoming request.
3. Performs authorization checks.
4. Processes and classifies the issue.
5. Retrieves relevant knowledge.
6. Builds contextual information for resolution.
7. Returns a structured response.
8. Uses a fallback path when the issue cannot be confidently
   resolved.

The internship architecture used **AWS Q Business** with a
**Confluence-backed knowledge source**.

The public repository uses a synthetic local knowledge base so
that the project can run without enterprise credentials.

---

## Key Features

- AI-powered enterprise knowledge retrieval
- RAG-oriented issue-resolution workflow
- Role-based access control
- REST API using FastAPI
- Request validation
- Fallback handling for unsupported queries
- Application-level observability
- Automated unit and integration testing
- Environment-based configuration
- GitHub Actions CI
- Interactive Swagger / OpenAPI documentation
- Sanitized public architecture with synthetic data
- Retrieval abstraction for replacing the local demo backend
  with an enterprise retrieval implementation

---

# Tech Stack

## Backend & Programming

<p align="left">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"
     width="50"
     height="50"
     alt="Python"/>

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg"
     width="50"
     height="50"
     alt="FastAPI"/>

</p>

**Python** · **FastAPI** · **REST APIs** · **Pydantic**

---

## Cloud & AWS

<p align="left">

<img src="https://logos-world.net/wp-content/uploads/2021/08/Amazon-Web-Services-AWS-Logo.png"
     width="50"
     height="50"
     alt="AWS"/>

</p>

**AWS Q Business** · **AWS Lambda** · **API Gateway** ·
**Amazon S3**

---

## AI & Knowledge Retrieval

<p align="left">

<img src="https://img.shields.io/badge/RAG-Knowledge%20Retrieval-7B61FF?style=for-the-badge"
     alt="RAG"/>

<img src="https://img.shields.io/badge/AWS%20Q%20Business-AI%20Retrieval-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white"
     alt="AWS Q Business"/>

<img src="https://img.shields.io/badge/LLM-AI%20Reasoning-412991?style=for-the-badge"
     alt="LLM"/>

</p>

**RAG** · **AWS Q Business** · **LLM-based knowledge retrieval**
· **Confluence**

---

## Security & API

<p align="left">

<img src="https://img.shields.io/badge/RBAC-Authorization-2EA44F?style=for-the-badge"
     alt="RBAC"/>

<img src="https://img.shields.io/badge/REST-API-009688?style=for-the-badge"
     alt="REST API"/>

<img src="https://img.shields.io/badge/OpenAPI-Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black"
     alt="Swagger"/>

</p>

**RBAC** · **REST APIs** · **OpenAPI / Swagger** ·
**Pydantic Validation**

---

## Enterprise Integration

<p align="left">
   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Microsoft_Office_Teams_%282025%E2%80%93present%29.svg/960px-Microsoft_Office_Teams_%282025%E2%80%93present%29.svg.png" alt="Microsoft Teams" height="40"/>
  <img src="https://logos-world.net/wp-content/uploads/2023/11/Confluence-Emblem.png" alt="Confluence" height="40"/>
</p>

**Microsoft Teams** · **Bot/API Integration** · **Confluence**

---

## Testing & DevOps

<p align="left">

<img src="https://cdn.simpleicons.org/githubactions/ffffff"
     width="50"
     height="50"
     alt="GitHub Actions"/>

<img src="https://cdn.simpleicons.org/git/ffffff"
     width="50"
     height="50"
     alt="Git"/>

<img src="https://cdn.simpleicons.org/github/ffffff"
     width="50"
     height="50"
     alt="GitHub"/>

</p>

**Python unittest** · **GitHub Actions** · **Git** · **GitHub**

> **Note:** AWS Q Business, Confluence, Lambda, API Gateway,
> S3, and Microsoft Teams represent technologies from the
> internship architecture. The public repository uses a local
> synthetic retrieval implementation to avoid exposing
> proprietary systems, data, or credentials.

---

# Architecture

The platform follows a layered architecture that separates
API handling, authorization, issue processing, knowledge
retrieval, and response generation.

### System Architecture

![System Architecture](docs/images/system-architecture.png)

*High-level architecture showing the enterprise issue-resolution
workflow, API layer, authorization, knowledge retrieval, and
response flow.*

### High-Level Flow

```text
Microsoft Teams
      │
      ▼
API / Backend Layer
      │
      ▼
Authentication / RBAC
      │
      ▼
Issue Processing
      │
      ├───────────────┐
      ▼               ▼
AWS Q Business        S3
      │               │
      ▼               ▼
Confluence         Order Data
      │               │
      └───────┬───────┘
              ▼
      Contextual Response
              │
              ▼
       Microsoft Teams

---

# RAG Workflow

The issue-resolution workflow follows a **Retrieval-Augmented Generation (RAG)** approach to ground responses in relevant enterprise knowledge.

### Internship Architecture

During the internship, the workflow used:

- AWS Q Business for enterprise knowledge retrieval
- Confluence as a knowledge source
- Backend/API services for request processing
- Role-based access control
- Contextual response generation
- Fallback handling for unsupported or low-confidence requests

### Public Repository

Because the original enterprise knowledge base and AWS environment are no longer accessible, this repository uses a **sanitized local retrieval implementation** with synthetic support examples.

This demonstrates the same core engineering concepts without exposing proprietary information.

![RAG Workflow](docs/images/rag-workflow.png)

---

# Security & RBAC

The platform includes a role-based authorization layer before issue-resolution processing.

### Request Flow

```text
User Request
     |
     v
Authentication / Role Validation
     |
     +---- Unauthorized ----> HTTP 403
     |
     v
Issue Resolution Workflow
     |
     v
Knowledge Retrieval
     |
     v
Contextual Response

---
