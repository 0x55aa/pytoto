# coding: utf-8
from django.conf.urls import patterns, url

from .views import ForumIndexView, ForumListView, ForumResetTotalView


urlpatterns = patterns('',

    url(r'^forum/$', ForumIndexView.as_view(), name='forum_index'),
    url(r'^category/(?P<category_slug>[-_\w]+)/$', ForumListView.as_view(), name='forum_list'),
    #
    url(r'^reset_total/$', ForumResetTotalView.as_view(), name='reset_total'),
)
