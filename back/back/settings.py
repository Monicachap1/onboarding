"""
Django settings for back project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys

import environ
from django.utils.translation import gettext_lazy as _

env = environ.Env()
environ.Env.read_env(env.str("ENV_PATH", "back/.env"))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

if env("ALLOWED_HOSTS", default="") != "":
    ALLOWED_HOSTS = [host for host in env.list("ALLOWED_HOSTS")]
else:
    # Fallback for old environment variable to avoid breaking change
    ALLOWED_HOSTS = [
        env("ALLOWED_HOST", default="0.0.0.0"),
    ]

if DEBUG:
    ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "users",
    "organization",
    "user_auth",
    "misc",
    "back",
    # admin
    "admin.templates",
    "admin.notes",
    "admin.to_do",
    "admin.resources",
    "admin.introductions",
    "admin.admin_tasks",
    "admin.badges",
    "admin.integrations",
    "admin.preboarding",
    "admin.appointments",
    "admin.sequences",
    "admin.people",
    "admin.settings",
    # new hires
    "new_hire",
    # slack
    "slack_bot",
    # ldap
    "ldap",
    # external
    "rest_framework",
    "axes",
    "anymail",
    "django_q",
    "crispy_forms",
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Login Defaults
LOGIN_REDIRECT_URL = "logged_in_user_redirect"
LOGOUT_REDIRECT_URL = "login"
LOGIN_URL = "login"

RUNNING_TESTS = "pytest" in sys.modules
FAKE_SLACK_API = False
SLACK_USE_SOCKET = env.bool("SLACK_USE_SOCKET", default=False)
SLACK_APP_TOKEN = env("SLACK_APP_TOKEN", default="")
SLACK_BOT_TOKEN = env("SLACK_BOT_TOKEN", default="")

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "organization.middleware.HealthCheckMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "users.middleware.language_middleware",
    "axes.middleware.AxesMiddleware",
]

# Django Debug Bar
if DEBUG:
    import socket

    INSTALLED_APPS += [
        "debug_toolbar",
    ]
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
    hostname, _dummy, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]


ROOT_URLCONF = "back.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "organization.context_processor.org_include",
            ],
        },
    },
]
TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"),)

WSGI_APPLICATION = "back.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {"default": env.db()}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        ),
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

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


AUTH_USER_MODEL = "users.User"

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    origin for origin in env.list("CORS_ALLOWED_ORIGINS", default="")
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "api.permissions.AdminPermission",
    ],
}


# API
API_ACCESS = env.bool("API_ACCESS", default=DEBUG or RUNNING_TESTS)
if API_ACCESS:
    INSTALLED_APPS += ["rest_framework.authtoken", "api"]

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

if env("MAILGUN_API_KEY", default="") != "":
    ANYMAIL = {
        "MAILGUN_API_KEY": env("MAILGUN_KEY", default=""),
        "MAILGUN_SENDER_DOMAIN": env("MAILGUN_DOMAIN", default=""),
    }
    EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"

if env("MAILJET_API_KEY", default="") != "":
    ANYMAIL = {
        "MAILJET_API_KEY": env("MAILJET_API_KEY", default=""),
        "MAILJET_SECRET_KEY": env("MAILJET_SECRET_KEY", default=""),
    }
    EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"

if env("MANDRILL_KEY", default="") != "":
    ANYMAIL = {"MANDRILL_API_KEY": env("MANDRILL_KEY", default="")}
    EMAIL_BACKEND = "anymail.backends.mandrill.EmailBackend"

if env("POSTMARK_KEY", default="") != "":
    ANYMAIL = {"POSTMARK_SERVER_TOKEN": env("POSTMARK_KEY", default="")}
    EMAIL_BACKEND = "anymail.backends.postmark.EmailBackend"

if env("SENDGRID_KEY", default="") != "":
    ANYMAIL = {"SENDGRID_API_KEY": env("SENDGRID_KEY", default="")}
    EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"

if env("SENDINBLUE_KEY", default="") != "":
    ANYMAIL = {"SENDINBLUE_API_KEY": env("SENDINBLUE_KEY", default="")}
    EMAIL_BACKEND = "anymail.backends.sendinblue.EmailBackend"

if env("EMAIL_HOST", default="") != "":
    EMAIL_HOST = env("EMAIL_HOST", default="localhost")
    EMAIL_PORT = env.int("EMAIL_PORT", default=25)
    EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
    EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=False)
    EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL", default=False)
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="example@example.com")

OLD_PASSWORD_FIELD_ENABLED = True

# Caching
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cached_items",
    }
}

Q_CLUSTER = {
    "name": "DjangORM",
    "workers": 1,
    "timeout": 90,
    "retry": 1800,
    "queue_limit": 50,
    "bulk": 10,
    "orm": "default",
    "catch_up": False,
    "max_attempts": 2,
}

if DEBUG and RUNNING_TESTS:
    Q_CLUSTER["sync"] = True

# AWS
AWS_S3_ENDPOINT_URL = env(
    "AWS_S3_ENDPOINT_URL", default="https://s3.eu-west-1.amazonaws.com"
)
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default="")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", default="")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME", default="")
AWS_REGION = env("AWS_REGION", default="eu-west-1")

if env.str("BASE_URL", "") == "":
    BASE_URL = "https://" + ALLOWED_HOSTS[0]
else:
    BASE_URL = env("BASE_URL")

# Twilio
TWILIO_FROM_NUMBER = env("TWILIO_FROM_NUMBER", default="")
TWILIO_ACCOUNT_SID = env("TWILIO_ACCOUNT_SID", default="")
TWILIO_AUTH_TOKEN = env("TWILIO_AUTH_TOKEN", default="")

# Django-Axes
AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    "axes.backends.AxesBackend",
    # Django ModelBackend is the default authentication backend.
    "django.contrib.auth.backends.ModelBackend",
]
AXES_ENABLED = env.bool("AXES_ENABLED", default=True)
AXES_FAILURE_LIMIT = env.int("AXES_FAILURE_LIMIT", default=10)
AXES_COOLOFF_TIME = env.int("AXES_COOLOFF_TIME", default=24)

if env.bool("AXES_USE_FORWARDED_FOR", True):
    AXES_META_PRECEDENCE_ORDER = [
        "HTTP_X_FORWARDED_FOR",
        "REMOTE_ADDR",
    ]

# Error tracking
if env("SENTRY_URL", default="") != "":
    import logging

    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration
    from sentry_sdk.integrations.logging import LoggingIntegration

    sentry_logging = LoggingIntegration(
        level=logging.INFO,  # Capture info and above as breadcrumbs
        event_level=logging.ERROR,  # Send errors as events
    )

    sentry_sdk.init(
        dsn=env("SENTRY_URL", default=""),
        integrations=[DjangoIntegration(), sentry_logging],
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=False,
    )

if not env.bool("DEBUG", default=False) and not env.bool(
    "HTTP_INSECURE", default=False
):
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

FIXTURE_DIRS = ["fixtures"]

# Forcing SSL from Django - preferably done a few levels before,
# but this is a last resort in the case of Heroku
if env.bool("SSL_REDIRECT", default=False):
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True

# Storing static files compressed
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Languages
LANGUAGES = [
    ("en", _("English")),
    ("nl", _("Dutch")),
    ("fr", _("French")),
    ("de", _("German")),
    ("tr", _("Turkish")),
    ("pt", _("Portuguese")),
    ("jp", _("Japanese")),
    ("es", _("Spanish")),
]
LANGUAGE_SESSION_KEY = "chief-language"
SITE_ROOT = os.path.dirname(os.path.realpath(__name__))
LOCALE_PATHS = (os.path.join(SITE_ROOT, "locale"),)

if env.bool("DEBUG_LOGGING", default=False):
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {"format": "%(levelname)s %(message)s"},
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "simple",
            },
        },
        "loggers": {
            "django.request": {
                "handlers": ["console"],
                "propagate": False,
                "level": "DEBUG",
            },
            "root": {"level": "DEBUG", "handlers": ["console"]},
        },
    }


# OIDC
OIDC_LOGIN_DISPLAY = env("OIDC_LOGIN_DISPLAY", default="Custom-OIDC")
OIDC_ENABLED = env.bool("OIDC_ENABLED", default=False)
OIDC_CLIENT_ID = env("OIDC_CLIENT_ID", default="")
OIDC_CLIENT_SECRET = env("OIDC_CLIENT_SECRET", default="")
OIDC_AUTHORIZATION_URL = env("OIDC_AUTHORIZATION_URL", default="")
OIDC_TOKEN_URL = env("OIDC_TOKEN_URL", default="")
OIDC_USERINFO_URL = env("OIDC_USERINFO_URL", default="")
OIDC_SCOPES = env("OIDC_SCOPES", default="openid email profile")
OIDC_LOGOUT_URL = env("OIDC_LOGOUT_URL", default="")
OIDC_FORCE_AUTHN = env.bool("OIDC_FORCE_AUTHN", default=False)
OIDC_ROLE_ADMIN_PATTEREN = env(
    "OIDC_ROLE_ADMIN_PATTEREN", default="^cn=Administrators.*"
)
OIDC_ROLE_MANAGE_PATTEREN = env("OIDC_ROLE_MANAGE_PATTEREN", default="^cn=Manage.*")
OIDC_ROLE_DEFAULT = env.int("OIDC_DEFAULT_ROLE", "3")
OIDC_ROLE_PATH_IN_RETURN = env('OIDC_ROLE_PATH_IN_RETURN',default="zoneinfo").split(",")
OIDC_USERINFO_SYNC = env.bool("OIDC_USERINFO_SYNC", default=False)

# LDAP
LDAP_SYNC=env.bool("LDAP_SYNC", default=False)
LDAP_HOST=env("LDAP_HOST", default="openldap")
LDAP_PORT=env.int("LDAP_PORT", default=389)
LDAP_TLS=env.bool("LDAP_TLS", default=False)
LDAP_BIND_DN=env("LDAP_BIND_DN", default="cn=admin,dc=example,dc=org")
LDAP_BIND_PW=env("LDAP_BIND_PW", default="admin")
LDAP_BASE_DN=env("LDAP_BASE_DN", default="dc=example,dc=org")
LDAP_USER_BASE_RDN=env("LDAP_USER_BASE_RDN", default="ou=User")
LDAP_GROUP_BASE_RDN=env("LDAP_GROUP_BASE_RDN", default="ou=Group")
LDAP_USER_FILTER=env("LDAP_USER_FILTER", default="(cn=*)")
LDAP_GROUP_FILTER=env("LDAP_GROUP_FILTER", default="(cn=*)")
# Account type for LDAP, posixAccount or inetOrgPerson
LDAP_ACCOUNT_TYPE=env("LDAP_ACCOUNT_TYPE", default="posixAccount")
LDAP_USER_TMP_OU=env("LDAP_USER_TMP_OU", default="ou=Inactive")
LDAP_DEFAULT_GROUPS = env("LDAP_DEFAULT_GROUPS", default="")
LDAP_POSIX_GROUP_RDN = env("LDAP_POSIX_GROUP_RDN", default="")
LDAP_DEFAULT_GROUPS_FILENAME=env("LDAP_DEFAULT_GROUPS_FILENAME", default="/department.yaml")
LDAP_LOG=env.bool("LDAP_LOG", default=False)
LDAP_USER_HOME_DIRECTORY=env("LDAP_USER_HOME_DIRECTORY", default="/home")

# USER_CREDENTIALS
USER_CREDENTIALS_SEND_IMMEADIATELY= env.bool("USER_CREDENTIALS_SEND_IMMEADIATELY", default=False)

if env.str("WELCOME_URL", "") == "":
    WELCOME_URL = BASE_URL
else:
    WELCOME_URL = env("WELCOME_URL")

PREBOARDING_URL = None
if env.str("PREBOARDING_URL","")=="":    
    PREBOARDING_URL = None
else:
    PREBOARDING_URL = env("PREBOARDING_URL")