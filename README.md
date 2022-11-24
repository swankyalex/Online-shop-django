## Online Shop
### https://swankyaleks-shop.onrender.com/

[![Make](https://img.shields.io/badge/Make-%23008FBA.svg?style=for-the-badge&logo=gnu&logoColor=white)](https://www.gnu.org/software/make/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)&nbsp;
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-blue?logo=postgresql&style=for-the-badge&logoColor=white)](https://postgresql.org)&nbsp;
[![Stripe](https://img.shields.io/badge/Stripe-626CD9?style=for-the-badge&logo=Stripe&logoColor=white)](https://stripe.com/)&nbsp;
[![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/)&nbsp;
[![Celery](https://img.shields.io/badge/celery-%2337814A.svg?&style=for-the-badge&logo=celery&logoColor=white)](https://docs.celeryq.dev/en/stable/)&nbsp;

[![main](https://github.com/swankyalex/Online-shop-django/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/swankyalex/Online-shop-django/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Lines of code](https://img.shields.io/tokei/lines/github/swankyalex/Online-shop-django)](https://github.com/swankyalex/Online-shop-django/tree/master)
![license](https://img.shields.io/badge/license-Apache%202-blue)
<br>
[![code size](https://img.shields.io/github/languages/code-size/swankyalex/Online-shop-django)](./)
[![repo size](https://img.shields.io/github/repo-size/swankyalex/Online-shop-django)](./)
##
[![python](https://img.shields.io/github/pipenv/locked/python-version/swankyalex/Online-shop-django)](https://www.python.org/)
[![dynaconf](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/Online-shop-django/dynaconf)](https://www.dynaconf.com/)
[![postgresql](https://img.shields.io/badge/PostgreSQL-15.1-blue)](https://postgresql.org)
<br>
[![django](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/Online-shop-django/django)](https://www.djangoproject.com/)
[![django-allauth](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/Online-shop-django/django-allauth)](https://django-allauth.readthedocs.io/en/latest/)
[![stripe](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/Online-shop-django/stripe)](https://stripe.com/)
<br>
[![celery](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/Online-shop-django/celery)](https://docs.celeryq.dev/en/stable/)
[![redis](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/Online-shop-django/django-redis)](https://redis.io/)
[![gunicorn](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/Online-shop-django/gunicorn)](https://gunicorn.org/)

### This is a web-service (online shop), written on Django and Django Templates. Functionality:
- Online shop with different categories of goods;
- User registration with confirmation email sending;
- Work with goods in cart for every user;
- Main profile page (editing personal data) for users;
- Github authorization for users;
- Tests for all applications;
- Celery with Redis for delayed tasks
- Stripe payments connected

## Usage
### Without docker (SQlite using)
1. Clone this repository to your machine.
2. Make sure Python and [Pipenv](https://pipenv.pypa.io/en/latest/) are installed on your machine.
3. Install the project dependencies (*run this and following commands in a terminal, from the root of a cloned repository*):
```sh
pipenv install # or with flag [--dev] for dev dependencies
```
4. Run redis server:
```sh
redis-server
```
5. Run celery
```sh
celery --workdir=src -A project worker --loglevel=INFO
```
6. Run server
```sh
pipenv run python src/manage.py runserver
```

## Development

The code in this repository must be tested, formatted with black.

1. Formatting with [black](https://black.readthedocs.io/en/stable/) and [isort](https://pycqa.github.io/isort/) 
```
pipenv run [black/isort]
```
2. Make tests with with one of the following commands:
```
pipenv run src/manage.py test .
```

### Docker usage (PostgreSQL using)
1. Clone this repository to your machine.
2. Run commands:
```sh
docker-compose build  
```
and
```sh
docker-compose up 
```

## Available [Make](https://www.gnu.org/software/make/) commands:

```
make venv           Сreate virtual environment (pipenv install)
make venv-dev       Сreate virtual environment with dev packages (pipenv install --dev)
make run            Run local server (python manage.py runserver)
make run-prod       Run local server via gunicorn
make format         Code formatting with black, isort.
make sh             Run django shell (python manage.py shell)
make su             Create django superuser (python manage.py createsuperuser)
make migrations     Create migrations (python manage.py makemigrations)
make migrate        Push migrations (python manage.py migrate)
make static         Static collection for production (python manage.py collectstatic)
make test           Run tests (pytest src)
make load-dump      Load initial fixtures to database (python manage.py loaddata)
make celery         Run celery (celery --workdir=$(DIR_SRC) -A project worker --loglevel=INFO)
make docker         Build docker image (docker-compose build)
make docker-run     Run docker container (docker-compose up)
make docker-clean   Clean all docker cache for project
```


