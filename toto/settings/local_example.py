# coding: utf-8
from base import *


DEBUG = False
ALLOWED_HOSTS = ['*', ]

# 是否开启cron
CRON = False
CRON_LIST = ['topic.management.commands.reset_total', ]
# url reset
RESET_SECRET_KEY = "asdfasdfasdfsd"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
SECRET_KEY = ''
