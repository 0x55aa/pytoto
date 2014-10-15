# coding: utf-8
import datetime

from django.utils import timezone
from django import template
from topic.models import Topic


register = template.Library()


@register.assignment_tag
def get_essence_topic():
    """
    获取精华帖子
    """
    count = 8
    #time = datetime.date.today() + datetime.timedelta(days=-5)
    time = timezone.now() + datetime.timedelta(days=-5)
    topic_essence = list(Topic.objects.filter(essence=True, created_on__gt=time)[:count])
    l = count - len(topic_essence)
    if l > 0:
        topic_list = list(Topic.objects.filter(essence=False).order_by('-last_reply_on')[:l])
    return topic_essence + topic_list
