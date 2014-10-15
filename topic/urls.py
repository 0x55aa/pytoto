# coding: utf-8
from django.conf.urls import patterns, url

from .views import (
    TopicDetailView,
    TopicListView,
    TopicCreateView,
    TopicIndexView,
    PostSpamView,
    PostLikeView,
    PostCreateView,
    PostDeleteView,
    UploadImgView,
    TopicUpdateView,
    TypeTopicListView,
    TopicHomepageDetailView,
)


urlpatterns = patterns('',
    url(r'^upload_img/$', UploadImgView.as_view(), name='upload_img'),
    url(r'^topic/$', TopicIndexView.as_view(), name='topic_index'),
    url(r'^topic/(?P<forum_slug>[-_\w]+)/new/$', TopicCreateView.as_view(), name='topic_create'),
    url(r'^topic/(?P<topic_slug>[-_\w]+)/edit/$', TopicUpdateView.as_view(), name='topic_update'),
    url(r'^topic/(?P<topic_slug>[-_\w]+)/$', TopicDetailView.as_view(), name='topic_detail'),
    url(r'^forum/(?P<forum_slug>[-_\w]+)/$', TopicListView.as_view(), name='topic_list'),
    url(r'^type/(?P<type_slug>[-_\w]+)/$', TypeTopicListView.as_view(), name='type_topic_list'),
    url(r'^topic_homepage/(?P<topic_slug>[-_\w]+)/$', TopicHomepageDetailView.as_view(), name='topic_homepage'),

    url(r'^post/spam/(?P<post_slug>[-_\w]+)/$', PostSpamView.as_view(), name='post_spam'),
    url(r'^post/like/(?P<post_slug>[-_\w]+)/$', PostLikeView.as_view(), name='post_like'),
    url(r'^post/new/(?P<topic_slug>[-_\w]+)/$', PostCreateView.as_view(), name='post_create'),
    url(r'^post/delete/(?P<post_slug>[-_\w]+)/$', PostDeleteView.as_view(), name='post_delete'),
)
