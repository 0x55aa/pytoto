# coding: utf-8
from django.contrib import admin
from .models import TopicType, Tag, Topic, Post, Attachment


admin.site.register(Topic)
admin.site.register(TopicType)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Attachment)
