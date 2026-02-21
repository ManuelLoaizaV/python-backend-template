# Minimal template TODO

## Design

1. Is domain.ports neccesary?
2. Classes or functions on repository/service?
3. Simplify implementation examples


## Setup

1. Add Makefile, just to remember some commands
2. Add Alembic support as the default schema-management approach.
3. Update `app.py` lifecycle so startup does not auto-create tables when using migrations.
4. Configure test database strategy explicitly for migrations + isolated tests.
5. Add Docker Compose for Postgres + Redis and test configuration. Maybe ```make test-full``` or ```make test-pytest```?
