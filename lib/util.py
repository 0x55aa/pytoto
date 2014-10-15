# coding: utf-8
import urllib
import hashlib

from django.conf import settings


def get_avatar(email, host, size=48):
    default_url = "http://" + host + settings.STATIC_URL + 'image/user_normal.jpg'
    url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    url += urllib.urlencode({'d': default_url, 's': str(size)})

    return url


def js_escape(string):
    double = (("\\", r"\\"), ("'", "\\'"), ('"', '\\"'), ("\r", r"\r"),
              ("\n", r"\n"), ("&", "\\&"), ("\t", r"\t"), ("\b", r"\b"),
              ("\f", r"\f"))
    for k, v in double:
        string = string.replace(k, v)
    return string
