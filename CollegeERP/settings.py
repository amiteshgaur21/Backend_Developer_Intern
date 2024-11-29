"""
Django settings for erptest project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jy8c-n9y=pf##!2^jae-l_5iafq6q%wfq8gdb6c0r5d52su+9y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set to False in production to disable debug mode

ALLOWED_HOSTS = ['*']  # Update with specific domains or IPs in production

# Custom user model
AUTH_USER_MODEL = 'info.User'  # Specify custom user model located in 'info' app

# Application definition
INSTALLED_APPS = [
    'info.apps.InfoConfig',  # Custom app for user-related functionality
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Django REST framework for APIs
    'djoser',  # For authentication and user management APIs
    'rest_framework.authtoken',  # Token-based authentication
    'apis',  # Custom APIs app
]

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security enhancements
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manage user sessions
    'django.middleware.common.CommonMiddleware',  # Handle common middleware functionality
    'django.middleware.csrf.CsrfViewMiddleware',  # Protect against CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Handle user authentication
    'django.contrib.messages.middleware.MessageMiddleware',  # Handle flash messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Prevent clickjacking
]

# Project's main URLs configuration
ROOT_URLCONF = 'CollegeERP.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Look for templates in this folder
        'APP_DIRS': True,  # Enable searching app-level template directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Include request object in templates
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application for deploying the project
WSGI_APPLICATION = 'CollegeERP.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # SQLite database (lightweight, not for production)
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation for user accounts
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'  # Default language
TIME_ZONE = 'UTC'  # Default timezone
USE_I18N = True  # Enable internationalization
USE_L10N = True  # Enable localization
USE_TZ = True  # Enable timezone support

# Static files configuration
STATIC_URL = '/static/'  # URL for serving static files (CSS, JS, images)

# Redirect after login
LOGIN_REDIRECT_URL = '/'

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # Enforce authentication globally
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',  # Token-based authentication
        'rest_framework.authentication.SessionAuthentication',  # Session-based authentication
    ),
}