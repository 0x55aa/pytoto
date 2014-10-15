# coding: utf-8
from django import template
from django.contrib.auth.models import User

from forum.models import Forum


register = template.Library()


@register.assignment_tag
def get_total():
    """
    获取相关统计信息
    今日帖子，总帖子，总主题，总会员
    """
    r = {
        'today_total_post': Forum.objects.get_today_total_post(),
        'total_post': Forum.objects.get_total_post(),
        'total_topic': Forum.objects.get_total_topic(),
        'total_user': User.objects.count(),
    }
    return r
