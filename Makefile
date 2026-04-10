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

# Usage: make migration message="add users table"
migration:
	docker compose exec backend uv run alembic revision --autogenerate -m "$(message)"

migrate:
	docker compose exec backend uv run alembic upgrade head
