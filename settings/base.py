"""
Django settings for adbro project.

Generated by 'django-admin startproject' using Django 1.11.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS_DIR = BASE_DIR + '/src'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', cast=str)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['*']

# Application definition

BUILDIN_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

APPS = [
    'src.advertisement',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters'
]

INSTALLED_APPS = BUILDIN_APPS + APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'settings.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'settings.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    f'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'adbro',
        'USER': 'fitshopuser',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': '5432'
        # 'NAME': config('DB_NAME', cast=str),
        # 'USER': config('DB_USER', cast=str),
        # 'PASSWORD': config('DB_PASSWORD', cast=str),
        # 'HOST': config('DB_HOST', cast=str),
        # 'PORT': config('DB_PORT', cast=int),
        # 'ATOMIC_REQUESTS': False,
        # 'CONN_MAX_AGE': 600,
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Etc/GMT+7'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(APPS_DIR, 'static')]


# HASHID
HASHID_FIELD_SALT = "yQP72ht2wPBQhRV2tnvTbQuOLbV9Fo643ha0Zu2hC0FFhGvaXin1lOztBeIYFhYuBE7p0pqne3w5H6wJMj6W_g"

#
# Django REST Framework
#
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
#     'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
# }
