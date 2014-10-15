# coding: utf-8
from django import template

from lib import util


register = template.Library()


@register.simple_tag(takes_context=True)
def get_avatar(context, email, size):
    """
    获取头像
    """
    host = context['request'].get_host()
    url = util.get_avatar(email, host, size)

    return url
