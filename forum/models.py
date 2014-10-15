# coding: utf-8
import re

from django.db import models
from django.db.models import Count, Sum
from django.core import validators
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Site(models.Model):
    """
    site

    site_name:
    description:
    keyword:
    """
    name = models.CharField(u"名", max_length=32)
    value = models.CharField(u"值", max_length=100)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    """
    分类
    """
    name = models.CharField(u"分类名", max_length=32, unique=True)
    slug = models.CharField(u"别名", max_length=32, unique=True, null=True,
            validators=[
                validators.RegexValidator(re.compile('^([a-zA-Z0-9_-]*[a-zA-Z][a-zA-Z0-9_-]*)$'), u'字母,数字,下划线,不能纯数字.'),
                validators.MinLengthValidator(3),
            ])

    ordering = models.IntegerField(u"排序", default=1)
    created_on = models.DateTimeField(u"创建时间", auto_now_add=True)

    def __unicode__(self):
        return self.name

    def get_slug(self):
        if self.slug:
            return self.slug
        else:
            return str(self.pk)

    def get_absolute_url(self):
        slug = self.get_slug()

        return reverse('forum_list', args=(slug, ))


class ForumManager(models.Manager):
    def get_today_total_post(self):
        r = self.aggregate(Sum('today_post_count'))
        return r['today_post_count__sum']

    def get_total_post(self):
        r = self.aggregate(Sum('post_count'))
        return r['post_count__sum']

    def get_total_topic(self):
        r = self.aggregate(Sum('topic_count'))
        return r['topic_count__sum']

    def get_all_type_count(self):
        """
        获得所有topictype的帖子数统计
        """
        pass

    def get_all_forum_count(self):
        """
        获得所有forum帖子数
        """
        return self.only('name', 'topic_count')


class Forum(models.Model):
    """
    板块
    """
    category = models.ForeignKey(Category, related_name="category_forum")
    name = models.CharField(u"板块名", max_length=32, unique=True)
    slug = models.CharField(u"别名", max_length=32, unique=True, null=True,
            validators=[
                validators.RegexValidator(re.compile('^([a-zA-Z0-9_-]*[a-zA-Z][a-zA-Z0-9_-]*)$'), u'字母,数字,下划线,不能纯数字.'),
                validators.MinLengthValidator(3),
            ])

    ordering = models.IntegerField(u"排序", default=1)
    description = models.CharField(u"描述", max_length=100)
    created_on = models.DateTimeField(u"创建时间", auto_now_add=True)

    topic_count = models.IntegerField(u"主题数", default=0)
    post_count = models.IntegerField(u"帖子数", default=0)
    today_post_count = models.IntegerField(u"今日帖子数", default=0)
    post_count_day = models.DateField(u"今日发帖统计时间", auto_now_add=True)

    last_replay_on = models.DateTimeField(u"创建时间", null=True)
    last_post_user = models.ForeignKey(User, related_name='+', null=True, blank=True)
    last_post = models.ForeignKey("topic.Post", related_name='+', null=True, blank=True)

    objects = ForumManager()

    def __unicode__(self):
        return self.name

    def get_slug(self):
        if self.slug:
            return self.slug
        else:
            return str(self.pk)

    def get_absolute_url(self):
        slug = self.get_slug()
        # c_slug = self.category.get_slug()

        # return reverse('topic_list', args=(c_slug, slug, ))
        return reverse('topic_list', args=(slug, ))

    def get_all_topic(self):
        return self.forum_topic.filter(closed=False)

    def get_all_topictype(self):
        """
        获取这个forum的说有topictype，并计算每个的发帖量
        """
        tt = self.topictype_set.all()
        return tt

    def get_notype_topic_count(self):
        """
        没设置type的帖子数量
        """
        return self.forum_topic.filter(topic_type=None).count()
