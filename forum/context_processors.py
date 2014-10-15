# coding:utf-8
from django.conf import settings

from forum.models import Site


def settings_var(request):
    """
    在template里加上settings一些变量
    """
    r = {}
    s = Site.objects.all()
    for i in s:
        r[i.name] = i.value

    r.update({'language': settings.LANGUAGE_CODE,
              })
    return r
