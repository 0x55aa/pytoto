# coding: utf-8
import threading
from django.conf import settings

from .cron import crontab


def autodiscover():
    for app in settings.CRON_LIST:
        crontab.register(app)

    t = threading.Thread(target=crontab.start)
    t.setDaemon(True)
    t.start()
