dev:
	docker compose up -d backend postgres --build
	@echo "Dev server starting..."
	@echo "API: http://localhost:8000"
	@echo "Docs: http://localhost:8000/docs"
	@echo "Logs: make logs"

stop:
	docker compose down --remove-orphans

stop-all:
	docker compose down --volumes --remove-orphans

logs:
	docker compose logs -f backend

test:
	docker compose up -d postgres-test
	docker compose run --rm backend uv run pytest tests
	docker compose stop postgres-test

# Usage: make migration message="add users table"
migration:
	docker compose exec backend uv run alembic revision --autogenerate -m "$(message)"

migrate:
	docker compose exec backend uv run alembic upgrade head
