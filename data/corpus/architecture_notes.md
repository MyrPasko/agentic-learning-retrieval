# Architecture Notes

## API Gateway

- Public traffic enters through `api-gateway`.
- `api-gateway` routes payment requests to `payments-api`.
- Authentication is handled before the request reaches backend services.

## Reliability Notes

- The current system does not use a graph database.
- Retrieval for Project 3 should start with a simple document corpus and explicit workflow boundaries.
- Confidence should drop when the corpus lacks direct evidence for a claim.

## Logging Rule

- Services must emit request IDs in logs.
- Financial write paths should also emit idempotency key presence as a boolean audit field.
