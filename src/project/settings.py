import os
import sys
from pathlib import Path

import dj_database_url
from dynaconf import settings as _ds

_this_file = Path(__file__).resolve()
DIR_PROJECT = _this_file.parent.resolve()
DIR_SRC = DIR_PROJECT.parent.resolve()
DIR_REPO = DIR_SRC.parent.resolve()
sys.path.append(os.path.join(DIR_SRC, "applications"))

SECRET_KEY = _ds.SECRET_KEY

DEBUG = _ds.MODE_DEBUG

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    _ds.HOST,
]

DOMAIN_NAME = _ds.DOMAIN_NAME

PROJECT_APPS = ["products", "users", "orders"]

THIRD_PARTY_APPS = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "debug_toolbar",
    "cloudinary_storage",
    "cloudinary",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",
    *PROJECT_APPS,
    *THIRD_PARTY_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [DIR_PROJECT / "templates", DIR_SRC / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "utils.context_processors.baskets",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
    "0.0.0.0",
    _ds.HOST,
]

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": _ds.REDIS,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

DATABASE_URL = os.getenv("DATABASE_URL", _ds.DATABASE_URL)

DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    DIR_SRC / "static",
]

STATIC_ROOT = DIR_REPO / ".static"

if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")

if not DEBUG:
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = DIR_SRC / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"
LOGIN_URL = "/users/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

EMAIL_HOST = "smtp.yandex.com"
EMAIL_PORT = 465
EMAIL_HOST_USER = "django-study-server@yandex.ru"
EMAIL_HOST_PASSWORD = _ds.EMAIL_HOST_PASSWORD
EMAIL_USE_SSL = True

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    "github": {
        "SCOPE": [
            "user",
        ],
    }
}

CELERY_BROKER_URL = _ds.CELERY_BROKER
CELERY_RESULT_BACKEND = _ds.CELERY_BROKER

STRIPE_PUBLIC_KEY = _ds.STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY = _ds.STRIPE_SECRET_KEY
STRIPE_WEBHOOK_SECRET = _ds.STRIPE_WEBHOOK_SECRET
