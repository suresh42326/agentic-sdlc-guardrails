---
name: migration-writer
description: Writes a safe schema migration for PostgreSQL following expand, then migrate, then contract, with row-level security for tenant tables. Use whenever a task changes the database schema.
---

# migration-writer

Schema migrations are high-risk. They need a second reviewer, one of them the person accountable for the architecture.

## Steps

1. Update the models first. Generate a migration with the project's tool (for Alembic: `uv run alembic revision --autogenerate -m "<id>: <what>"`).
2. Read the generated file and fix it. Generators miss renames, server defaults, enum changes, and row-level security.
3. Classify every operation:

| Kind | Examples | In this release? |
|---|---|---|
| Expand | add a nullable column, add a table, add an index concurrently | Yes |
| Migrate | backfill in batches | Yes, as its own migration |
| Contract | drop a column, add `NOT NULL`, rename | Only in a later release, after no code reads the old shape |

Do not ship expand and contract for the same change in one release.

4. Every new tenant-owned table gets:
   - a non-null `tenant_id` and an index that leads with it
   - row-level security enabled and forced
   - a policy that compares `tenant_id` to the tenant id set for the session, not to a value from the client
5. Create indexes on existing tables concurrently, outside a transaction that would lock writes.
6. Provide a working downgrade, or say in the pull request why the migration cannot be reversed.
7. Prove it against a local test database: upgrade, downgrade, upgrade again. Run a migration linter on the SQL.

## Rules

- Do not run migrations against a shared or remote database.
- Do not edit a migration that is already merged. Write a new one.
