import django_heroku
from .base import *

DEBUG = False

WSGI_APPLICATION = 'jivana.wsgi.application'

SECRET_KEY = os.environ['SECRET_KEY']


django_heroku.settings(locals())