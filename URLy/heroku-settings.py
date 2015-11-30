from .settings import *
import os
import dj_database_url

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

BLACKLIST = ['django_extensions']
INSTALLED_APPS = tuple([app for app in INSTALLED_APPS if app not in BLACKLIST])

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
