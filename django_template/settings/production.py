import os

from decouple import config
import dj_database_url

from .base import *

DEBUG = False
ALLOWED_HOSTS = ('django_template.herokuapp.com',)
SECRET_KEY = os.environ.get('SECRET_KEY')

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_PRELOAD_METADATA = True

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_LOCATION = 'django_template/static'
STATICFILES_STORAGE = 'django_template.custom_storages.StaticStorage'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'django_template/media'
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'sf_events.custom_storages.MediaStorage'
MEDIA_ROOT = ''

DATABASES = {'default': dj_database_url.config(
    default=config('DATABASE_URL'))
}

INSTALLED_APPS += [
    'storages',
]
