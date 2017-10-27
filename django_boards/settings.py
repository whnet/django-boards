"""
Django settings for django_boards project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from apps.board.settings import BOARD_THEME

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3u@gq^l@i5ji7obrnjm8x3@1f!=998++k7w-v^7md)830x@zvx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'precise_bbcode',
    'sass_processor',
    'easy_thumbnails',
    'apps.api',
    'apps.common',
    'apps.board',
]

if BOARD_THEME == 'bootstrap3':
    INSTALLED_APPS.append('crispy_forms')

# Auth Configuration
AUTH_USER_MODEL = 'api.EmailUser'
LOGIN_REDIRECT_URL = '/board/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'apps.api.authentication.NoCSRFSessionAuthentication',
    ),
    'PAGE_SIZE': 25
}

ROOT_URLCONF = 'django_boards.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.board.context_processors.settings',
                'apps.board.context_processors.base_context'
            ],
        },
    },
]

WSGI_APPLICATION = 'django_boards.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_boards',
        'USER': 'django_boards',
        'PASSWORD': 'django_boards',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'server', 'dev', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'server', 'dev', 'media')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_DIR = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    STATIC_DIR,
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # Other finders..
    'sass_processor.finders.CssFinder',
)

# Crispy forms

if BOARD_THEME == 'bootstrap3':
    CRISPY_TEMPLATE_PACK = 'bootstrap3'


# Easy thumbnails

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (200, 200), 'crop': True},
        'avatar_small': {'size': (100, 100), 'crop': True},
        'avatar_smaller': {'size': (50, 50), 'crop': True},
        'avatar_smallest': {'size': (25, 25), 'crop': True}
    },
}

CORS_ORIGIN_ALLOW_ALL = True
