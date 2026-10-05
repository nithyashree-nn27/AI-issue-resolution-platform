# Observability

The issue-resolution platform is designed with observability
in mind so that application behavior, failures, and request
latency can be monitored.

## Application-Level Observability

The public repository demonstrates lightweight application logging.

Each HTTP request records:

- HTTP method
- Request path
- Response status code
- Processing duration

Example:

```text
INFO | HTTP request completed |
method=POST |
path=/api/v1/resolve |
status=200 |
duration_ms=8.42