"""
Django settings for civiwiki project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'st9-h5vqc8&#b7k@7(_orp5ub7z^yecmj-fv+99k60-_5wy7qy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'api',
	'corsheaders',
    # 'django.contrib.messages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', TODO: uncomment and fix eventually
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
	'corsheaders.middleware.CorsMiddleware',
)
CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'civiwiki.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['frontend/templates'],
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

WSGI_APPLICATION = 'civiwiki.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DEBUG = True
if 'RDS_DB_NAME' in os.environ:
    DATABASE = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.enviorn['RDS_DB_NAME'],
            'USER': os.enviorn['RDS_USERNAME'],
            'PASSWORD': os.enviorn['RDS_PASSWORD'],
            'HOST': os.enviorn['RDS_HOSTNAME'],
            'PORT': os.enviorn['RDS_PORT']
        }
    }
else:
    DATABASES = {
        'default': {
            'HOST':'civiwiki.cwnas2j52gab.us-west-2.rds.amazonaws.com',
            'PORT': '5432',
            'NAME': 'civiwiki',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'civiwiki',
            'PASSWORD': 'changecivic2',
        },
    }



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False #Eh deal with timezones on front-end, I dislike them


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "../frontend/static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_ROOT_URL = '/media/'
