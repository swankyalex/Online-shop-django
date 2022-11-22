### Online Shop

[![Make](https://img.shields.io/badge/Make-%23008FBA.svg?style=for-the-badge&logo=gnu&logoColor=white)](https://www.gnu.org/software/make/)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Lines of code](https://img.shields.io/tokei/lines/github/swankyalex/Online-shop-django)](https://github.com/swankyalex/Online-shop-django/tree/master)
[![main](https://github.com/swankyalex/Online-shop-django/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/swankyalex/Online-shop-django/actions)
![license](https://img.shields.io/badge/license-Apache%202-blue)

[![python](https://img.shields.io/github/pipenv/locked/python-version/swankyalex/Online-shop-django)](https://www.python.org/)
[![dynaconf](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/Online-shop-django/dynaconf)](https://www.dynaconf.com/)
[![postgresql](https://img.shields.io/badge/PostgreSQL-15.1-blue)](https://postgresql.org)

[![django](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/Online-shop-django/django)](https://www.djangoproject.com/)
[![celery](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/Online-shop-django/celery)](https://docs.celeryq.dev/en/stable/)
[![redis](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/Online-shop-django/django-redis)](https://redis.io/)

[![code size](https://img.shields.io/github/languages/code-size/swankyalex/Online-shop-django)](./)
[![repo size](https://img.shields.io/github/repo-size/swankyalex/Online-shop-django)](./)


### This is a web-service (online shop), written on Django and Django Templates. Functionality:
- Online shop with different categories of goods;
- User registration with confirmation email sending;
- Work with goods in cart for every user;
- Main profile page (editing personal data) for users;
- Github authorization for users;
- Tests for all applications;
- Celery with Redis for delayed tasks

## Usage
1. Clone this repository to your machine.
2. Make sure Python and [Pipenv](https://pipenv.pypa.io/en/latest/) are installed on your machine.
3. Install the project dependencies (*run this and following commands in a terminal, from the root of a cloned repository*):
```sh
pipenv install # or with flag [--dev] for dev dependencies
```
or if you have [Make](https://www.gnu.org/software/make/) util
```sh
make venv # make venv-dev
```
4. Add DATABASE_URL in default section of [settings](https://github.com/swankyalex/Online-shop-django/blob/master/config/settings.yaml)


5. Run redis server:
```sh
redis-server
```
6. Run celery
```sh
celery --workdir=src -A project worker --loglevel=INFO
```
or
```sh
make celery
```
7. Run server
```sh
pipenv run python src/manage.py runserver
```
or
```sh
make run
```

## Development

The code in this repository must be tested, formatted with black.

1. Formatting with [black](https://black.readthedocs.io/en/stable/) and [isort](https://pycqa.github.io/isort/) 
```
make format
```
or
```
pipenv run [black/isort]
```
2. Make tests with with one of the following commands:
```
make test
```
```
pipenv run src/manage.py test .
```


