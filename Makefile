MANAGE = python3 manage.py

.PHONY: migrate makemigrations createsuperuser runserver shell test

migrate:
	@echo "Applying migrations..."
	$(MANAGE) migrate

makemigrations:
	@echo "Making migrations..."
	$(MANAGE) makemigrations

createsuperuser:
	@echo "Creating superuser..."
	$(MANAGE) createsuperuser

runserver:
	@echo "Starting development server..."
	$(MANAGE) runserver

shell:
	@echo "Starting Django shell..."
	$(MANAGE) shell

test:
	@echo "Running tests..."
	$(MANAGE) test

static:
	@echo "Collecting static files..."
	$(MANAGE) collectstatic --noinput
