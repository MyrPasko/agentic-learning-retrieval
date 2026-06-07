# On-Call Runbook

## Incident Severity Guide

- `SEV-1`: revenue loss, payment outage, or customer-facing downtime affecting the majority of users
- `SEV-2`: major degradation with workaround
- `SEV-3`: limited degradation or internal-only impact

## Payments API Triage

1. Check error rate and latency dashboards.
2. Confirm whether duplicate-charge reports are increasing.
3. Inspect recent deploys to `payments-api`.
4. Verify whether idempotency keys are being forwarded to `ledger-service`.
5. If duplicate charges are confirmed, page `payments-platform` and `finance-systems`.

## Escalation Rule

- If payment authorization fails for more than 10 minutes, escalate to `SEV-1`.
- If only reconciliation is delayed and payment capture still succeeds, start at `SEV-2`.
