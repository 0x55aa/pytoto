# coding: utf-8
from django import template
from topic.models import Topic


register = template.Library()


@register.assignment_tag
def get_pic_topic():
    """
    获取图片帖子
    """
    count = 2
    topic_essence = Topic.objects.filter(essence=True)[:count]
    l = count - len(topic_essence)
    if l > 0:
        topic_list = Topic.objects.filter(essence=False).order_by('-last_reply_on')[:l]
    return topic_essence | topic_list
