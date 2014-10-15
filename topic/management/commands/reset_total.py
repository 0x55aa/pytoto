# coding: utf-8
import datetime
from django.core.management.base import BaseCommand

from forum.models import Forum


class Command(BaseCommand):
    help = u'forum: today_post_count, post_count_day reset'

    def handle(self, *args, **options):
        now = datetime.datetime.now()
        Forum.objects.all().update(today_post_count=0, post_count_day=now)
        print "success: %s" % now
