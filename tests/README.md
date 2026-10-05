# Testing

The repository contains unit and integration tests for the
sanitized representative implementation.

## Unit Tests

Unit tests cover:

- Role-based access control
- Issue classification
- Fallback handling
- Knowledge retrieval

## Integration Tests

Integration tests validate:

- Health endpoint
- Issue-resolution API
- Authorization behavior
- Fallback behavior

## Running Tests

From the repository root:

```bash
python -m unittest discover -s tests -v