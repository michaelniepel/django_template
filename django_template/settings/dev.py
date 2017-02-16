from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '123456789!9vfk=157gykq8a*9gq^%d#z5yw+^p8o6$cqn0-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_template_dev',
        'USER': 'work',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS += [
    'debug_toolbar',
]

INTERNAL_IPS = '127.0.0.1'

try:
    from .local import *
except ImportError:
    pass