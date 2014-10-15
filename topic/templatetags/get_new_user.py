# coding: utf-8
from django import template
from django.contrib.auth.models import User


register = template.Library()


@register.assignment_tag
def get_new_user():
    """
    获取新注册用户
    """
    # try:
    #     return User.objects.order_by('-date_joined')[0]
    # except IndexError:
    #     return None
    return User.objects.order_by('date_joined').last()
