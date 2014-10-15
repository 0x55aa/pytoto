# coding: utf-8
import re
from django import template


register = template.Library()


@register.filter()
def get_text(context, num=160):
    """
    获取单纯的文本，并截取字数
    """
    return re.sub('<[^>]+>', '', context)[:num]
