# coding:utf-8
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey

from django.contrib.auth.models import User


class Profile(models.Model):
    level_CHOICES = (
        (1, '!'),
        (2, '@'),
        (3, '#'),
        (4, '%'),
    )

    user = models.OneToOneField(User)
    level = models.IntegerField(u"等级", default=1)
    topic_count = models.IntegerField(u"主题数", default=1)
    post_count = models.IntegerField(u"贴数", default=1)
    avatar_url = models.URLField(blank=True, null=True)


class UserLog(models.Model):
    ACTION_CHOICES = (
        (1, u'举报'),
        (2, u'删除'),
        (3, u'赞'),
        (4, u'首页'),
    )
    user = models.ForeignKey(User)
    action = models.IntegerField("动作", choices=ACTION_CHOICES, default=1)
    des = models.CharField(u"des", max_length=200, blank=True)
    c_time = models.DateTimeField(u"时间", auto_now_add=True)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
