# coding: utf-8
from django.contrib import admin
from .models import Site, Forum, Category


admin.site.register(Site)
admin.site.register(Forum)
admin.site.register(Category)
