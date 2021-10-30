import django_heroku
from .base import *

DEBUG = False

WSGI_APPLICATION = 'jivana.wsgi.application'

SECRET_KEY = os.environ['SECRET_KEY']

SECURE_SSL_REDIRECT = True

django_heroku.settings(locals())

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.jivana.be', '.jivana.com', '.aws.amazon.com', '.herokuapp.com']

# AMAZON AWZS
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_STORAGE_BUCKET_NAME = 'dbsselect'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.eu-central-1.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)