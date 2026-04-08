"""
settings.py — The brain of your Django project.
Every Django project has one. It controls:
  - Which apps are active
  - Database configuration
  - Where uploaded files go
  - Template (HTML) locations
"""

from pathlib import Path
import os

# BASE_DIR = the root folder of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key — keep this private in real projects!
SECRET_KEY = 'django-insecure-change-this-in-production-abc123xyz'

# Debug=True shows detailed errors during development
DEBUG = True

ALLOWED_HOSTS = ['*']  # In production, put your domain here

# INSTALLED_APPS = tells Django which "apps" to use.
# We added 'speech_app' — our custom app.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'speech_app',  # ← Our custom app goes here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ai_speech_dashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Django looks for HTML files in each app's 'templates' folder
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

WSGI_APPLICATION = 'ai_speech_dashboard.wsgi.application'

# DATABASE — SQLite is a simple file-based database, great for beginners.
# Django automatically creates db.sqlite3 when you run migrations.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

CSRF-TRUSTED_ORIGINS = ['https://ai-speech-dashboard.onrender.com']

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# STATIC FILES — CSS, JavaScript, images your app uses
STATIC_URL = 'static/'
STATICFILES_DIRS=[]
# MEDIA FILES — User-uploaded files (audio files in our case)
# When a user uploads audio, Django saves it in MEDIA_ROOT
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
