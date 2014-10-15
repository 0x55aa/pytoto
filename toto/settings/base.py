# coding: utf-8
from settings import *
from os.path import join, abspath, dirname


here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..", "..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

# 是否开启cron
CRON = False
CRON_LIST = ['topic.management.commands.reset_total', ]

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-cn'

STATICFILES_DIRS = (
    root('static'),
    root('media'),
)

TEMPLATE_DIRS = (
    root('templates'),
)

MEDIA_ROOT = root('media')
MEDIA_URL = '/media/'
MEDIA_URL_ = '/static/'

INSTALLED_APPS += (
    'django.contrib.humanize',

    'accounts',
    'forum',
    'topic',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "forum.context_processors.settings_var",
)
