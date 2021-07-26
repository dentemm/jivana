import django_heroku
from .base import *

DEBUG = False

WSGI_APPLICATION = 'jivana.wsgi.application'

SECRET_KEY = os.environ['SECRET_KEY']

SECURE_SSL_REDIRECT = True

django_heroku.settings(locals())