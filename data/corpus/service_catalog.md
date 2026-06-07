# Service Catalog

## Payments API

- Owner team: `payments-platform`
- Primary responsibility: authorize and capture card payments
- Runtime: Python `FastAPI`
- Data store: PostgreSQL
- Downstream dependencies:
  - `ledger-service`
  - `customer-profile-service`
- SLO target: `99.95%`
- Known operational risk: retries without idempotency keys can create duplicate charges

## Ledger Service

- Owner team: `finance-systems`
- Primary responsibility: persist financial transactions and balances
- Runtime: Kotlin
- Data store: PostgreSQL
- Downstream dependencies:
  - `audit-log-pipeline`
- Business rule: all write requests must carry an idempotency key

## Customer Profile Service

- Owner team: `identity-platform`
- Primary responsibility: expose customer profile and billing identity data
- Runtime: Node.js
- Data store: PostgreSQL
- Data classification: contains PII
