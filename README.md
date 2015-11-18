http://evening-falls-6344.herokuapp.com/loc/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(modules)s %(messages)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/general_logs.log'),
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
        'peteslist': {
            'handlers': ['file', 'console', 'mailer'],
            'level': 'DEBUG',
            'propagate': True
        }
    },
}
