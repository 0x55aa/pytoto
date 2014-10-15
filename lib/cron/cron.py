# coding: utf-8
import sched
import time
import datetime

from django.utils.importlib import import_module
# from django.conf import settings

cmd = []


class CronTab(object):
    """
    现在只在凌晨执行, 没有参数
    """
    def __init__(self):
        self.s = sched.scheduler(time.time, time.sleep)

    def register(self, command_modul):
        module = import_module(command_modul)
        cmd.append(module.Command())
        # print cmd

    def add_job(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        now = datetime.datetime.now()
        delta_second = (tomorrow - now).seconds + 1
        # delta_second = 20
        self.s.enter(delta_second, 0, self.add_job, ())
        for c in cmd:
            self.s.enter(delta_second, 1, c.handle, ())

    def start(self):
        self.add_job()
        self.s.run()

crontab = CronTab()
