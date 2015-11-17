from .settings import *

DEBUG=False
SECRET_KEY = os.environ['SECRET_KEY']
EMAIL_BACKEND = "sgbackend.SendGridBackend"
SENDGRID_USER = os.environ['SENDGRID_USER']
SENDGRID_PASSWORD = os.environ['SENDGRID_PASSWORD']


BLACKLIST = ['debug_toolbar', 'django_extensions']
INSTALLED_APPS = tuple([app for app in INSTALLED_APPS if app not in BLACKLIST])

import dj_database_url
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../fredslist/static'),
)



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': "DEBUG",
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, "logs/general_logs.log"),
            'formatter': 'verbose'
        },
        'mailer': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }

    },
    'loggers': {
        'chirp': {
            'handlers': ['file', 'console', 'mailer'],
            'level': 'DEBUG',
            'propagate': True
        },
    }

}


