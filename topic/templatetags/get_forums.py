# coding: utf-8
from django import template
from forum.models import Forum


register = template.Library()


@register.assignment_tag
def get_forums():
    """
    获取排名forums
    """
    return Forum.objects.all().order_by('-post_count')[:12]
