include ./Makefile.in.mk


.PHONY: format
format:
	$(call log, reorganizing imports & formatting code)
	$(RUN) isort "$(DIR_SRC)"
	$(RUN) black "$(DIR_SRC)"
	$(RUN) flake8 "$(DIR_SRC)"
	$(call log, All good!)


.PHONY: run
run:
	$(call log, starting local web server)
	$(PYTHON) src/manage.py runserver


.PHONY: run-prod
run-prod:
	$(call log, starting local web server)
	$(RUN) gunicorn --config="$(DIR_SCRIPTS)/gunicorn.conf.py" project.wsgi:application


.PHONY: sh
sh:
	$(call log, starting Python shell)
	$(PYTHON) src/manage.py shell


.PHONY: venv
venv:
	$(call log, installing packages)
	$(PIPENV_INSTALL)


.PHONY: venv-dev
venv-dev:
	$(call log, installing development packages)
	$(PIPENV_INSTALL) --dev


.PHONY: data
data: static migrate
	$(call log, preparing data)


.PHONY: static
static:
	$(call log, collecting static)
	$(PYTHON) src/manage.py collectstatic --noinput


.PHONY: su
su:
	$(call log, starting Python shell)
	$(PYTHON) src/manage.py createsuperuser


.PHONY: migrations
migrations:
	$(call log, generating migrations)
	$(PYTHON) src/manage.py makemigrations


.PHONY: migrate
migrate:
	$(call log, applying migrations)
	$(PYTHON) src/manage.py migrate


.PHONY: test
test:
	$(call log, running tests)
	$(PYTHON) src/manage.py test src