from .base import *

ALLOWED_HOSTS = []
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'shfdhsdf'

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}