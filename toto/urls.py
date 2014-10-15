# coding: utf-8
from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

if settings.CRON:
    from lib import cron
    cron.autodiscover()

from .views import HomeView


urlpatterns = patterns('',
    # Examples:
    url(r'^admin____/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('forum.urls')),
    url(r'^', include('topic.urls')),

)
