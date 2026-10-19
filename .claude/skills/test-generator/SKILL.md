---
name: test-generator
description: Proposes API and end-to-end test scenarios from a spec, mapped to acceptance criteria, for a human to review. Use when someone asks to generate tests for a feature id.
---

# test-generator

You propose tests. A human owns them. A generated test is not proof of a criterion until a human has reviewed it.

## Steps

1. Read the spec and, if it exists, the traceability report. List every acceptance criterion that has no test, or only a happy-path test.
2. For each gap, propose scenarios: happy path, boundaries, invalid input, the wrong role, the wrong tenant, and concurrency where two people can race (for example, two staff members assigning the same ticket).
3. Write the tests where the project keeps QA tests. Put the criterion id in the test name. Use synthetic data from factories. Do not use real personal data.
4. Run them. A failure is either a product bug (report it) or a bad test (fix the test). Label each failure as one or the other.
5. Output a table of criterion, new tests, and result, for a human to review.

## Rules

- Do not change application code. Do not change existing approved tests.
- Use stable selectors (`getByRole`, `data-testid`). Do not sleep; wait for a condition the product exposes.
