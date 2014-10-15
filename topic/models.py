# coding: utf-8
import re

from django.utils import timezone
from django.db import models
from django.core import validators
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType

from forum.models import Forum
from accounts.models import UserLog


class TopicType(models.Model):
    """
    主题类型
    """
    forum = models.ForeignKey(Forum)
    name = models.CharField("类型名", max_length=32)
    slug = models.CharField(u"别名", max_length=32, unique=True, null=True,
            validators=[
                validators.RegexValidator(re.compile('^([a-zA-Z0-9_-]*[a-zA-Z][a-zA-Z0-9_-]*)$'), u'字母,数字,下划线,不能纯数字.'),
                validators.MinLengthValidator(3),
            ])

    def __unicode__(self):
        return self.name

    def get_slug(self):
        if self.slug:
            return self.slug
        else:
            return str(self.pk)

    def get_absolute_url(self):
        slug = self.get_slug()
        return reverse('type_topic_list', args=(slug, ))

    def get_topic_count(self):
        return Topic.objects.filter(forum=self.forum, topic_type=self).count()


class Tag(models.Model):
    """
    标签
    """
    name = models.CharField("类型名", max_length=32, unique=True)
    topic_count = models.IntegerField(u"主题数", default=1)
    slug = models.CharField(u"别名", max_length=32, unique=True, null=True,
            validators=[
                validators.RegexValidator(re.compile('^([a-zA-Z0-9_-]*[a-zA-Z][a-zA-Z0-9_-]*)$'), u'字母,数字,下划线,不能纯数字.'),
                validators.MinLengthValidator(3),
            ])

    def __unicode__(self):
        return self.name


class Topic(models.Model):
    """
    主题
    """
    forum = models.ForeignKey(Forum, related_name="forum_topic")
    user = models.ForeignKey(User)
    created_on = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_user = models.ForeignKey(User, related_name='+', null=True, blank=True)
    updated_on = models.DateTimeField(u"更新时间", null=True)
    tag = models.ManyToManyField(Tag, null=True, blank=True)

    topic_type = models.ForeignKey(TopicType, verbose_name=u"类型", null=True, blank=True)
    subject = models.CharField(u"标题", max_length=100)
    # 最好根据forum唯一
    slug = models.CharField(u"别名", max_length=32, unique=True, null=True,
            validators=[
                validators.RegexValidator(re.compile('^([a-zA-Z0-9_-]*[a-zA-Z][a-zA-Z0-9_-]*)$'), u'字母,数字,下划线,不能纯数字.'),
                validators.MinLengthValidator(7),
            ])

    last_reply_on = models.DateTimeField(u"最后回复时间", null=True)
    last_reply_user = models.ForeignKey(User, related_name='+')

    #total
    sort_order = models.IntegerField(u"权重", default=0)
    reply_count = models.IntegerField(u"回复次数", default=0)
    view_count = models.IntegerField(u"浏览次数", default=0)
    spam_count = models.IntegerField(u"举报次数", default=0)
    like_count = models.IntegerField(u"喜欢次数", default=0)
    reply_user_count = models.IntegerField(u"回复人数", default=0)

    #status
    closed = models.BooleanField("关闭", default=False)
    hot = models.BooleanField("热帖", default=False)
    hidden = models.BooleanField("隐藏", default=False)
    essence = models.BooleanField("精华", default=False)
    sticky = models.BooleanField("置顶", default=False)
    homepage = models.BooleanField("首页", default=False)

    class Meta:
        ordering = ['-sticky', '-last_reply_on']

    def __unicode__(self):
        return self.subject

    def get_slug(self):
        if self.slug:
            return self.slug
        else:
            return str(self.pk)

    def get_absolute_url(self):
        slug = self.get_slug()
        return reverse('topic_detail', args=(slug, ))

    def get_topic_first_post(self):
        # id or flood
        return Post.objects.filter(topic=self).order_by('id').first()

    def get_forum_next_topic(self):
        return Topic.objects.filter(forum=self.forum, pk__gt=self.pk).order_by('id').first()
        # 不是1.6的
        # try:
        #     return Topic.objects.filter(forum=self.forum, pk__gt=self.pk).order_by('id')[0]
        # except IndexError:
        #     return None

    def get_forum_pre_topic(self):
        # try:
        #     return Topic.objects.filter(forum=self.forum, pk__lt=self.pk).order_by('-id')[0]
        # except IndexError:
        #     return None
        return Topic.objects.filter(forum=self.forum, pk__lt=self.pk).order_by('id').last()

    def user_delete(self, user,):
        self.closed = True
        self.save()
        # 保存用户操作

    def set_homepage(self, user):
        self.homepage = True
        self.save()
        UserLog(user=user, action=4, content_object=self).save()
        return True

    def view_count_add(self):
        self.view_count += 1
        self.save()

    def get_all_post(self):
        return self.post_set.filter()


class Post(models.Model):
    """
    帖子
    """
    topic = models.ForeignKey(Topic)
    parent = models.ForeignKey('self', null=True, blank=True)
    user = models.ForeignKey(User)

    created_on = models.DateTimeField(u"创建时间", auto_now_add=True)
    update_user = models.ForeignKey(User, related_name='+', null=True, blank=True)
    updated_on = models.DateTimeField(u"更新时间", null=True)

    floor = models.IntegerField(u"楼层", default=1)
    content = models.TextField(u"内容", max_length=60000)

    deleted = models.BooleanField("关闭", default=False)
    deleted_by = models.ForeignKey(User, related_name='+', null=True, blank=True)
    deleted_on = models.DateTimeField(u"删除时间", null=True)

    reply_email = models.BooleanField("有回复是否邮件通知", default=False)

    sort_order = models.IntegerField(u"权重", default=0)
    reply_count = models.IntegerField(u"回复次数", default=0)
    spam_count = models.IntegerField(u"举报次数", default=0)
    like_count = models.IntegerField(u"喜欢次数", default=0)
    reply_user_count = models.IntegerField(u"回复人数", default=0)

    def user_delete(self, user,):
        if self.deleted:
            return False
        self.deleted = True
        self.deleted_by = user
        self.deleted_on = timezone.now()
        self.save()
        if self.floor == 1:
            self.topic.user_delete(user)
        UserLog(user=user, action=2, content_object=self).save()

    def user_like(self, user,):
        # get_or_create()
        post_type = ContentType.objects.get_for_model(self)
        try:
            UserLog.objects.get(content_type__pk=post_type.pk,
                                object_id=self.pk, action=3, user=user)
            return False
        except ObjectDoesNotExist:
            UserLog(user=user, action=3, content_object=self).save()

        self.like_count += 1
        self.save()
        if self.floor == 1:
            self.topic.like_count += 1
            self.topic.save()
        return True

    def user_spam(self, user,):
        # get_or_create()
        post_type = ContentType.objects.get_for_model(self)
        try:
            UserLog.objects.get(content_type__pk=post_type.pk,
                                object_id=self.pk, action=1, user=user)
            return False
        except ObjectDoesNotExist:
            UserLog(user=user, action=1, content_object=self).save()

        self.spam_count += 1
        self.save()
        if self.floor == 1:
            self.topic.spam_count += 1
            self.topic.save()
        return True


class Attachment(models.Model):
    """
    附件
    """
    slug = models.CharField(u"唯一标识", max_length=32, blank=True)
    name = models.CharField(u"文件名", max_length=32)
    display_name = models.CharField(u"显示名", max_length=32)
    created_on = models.DateTimeField(u"创建时间", auto_now_add=True)
