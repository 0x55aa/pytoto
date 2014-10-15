# coding: utf-8
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import Http404, HttpResponse
from django.conf import settings

from .models import Category

from lib.mixin import Dispatch302Mixin
from topic.management.commands.reset_total import Command


class ForumResetTotalView(View):
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        if (request.GET.get("key", '') != settings.RESET_SECRET_KEY):
            raise Http404
        Command().handle()
        return HttpResponse('success')


class ForumIndexView(ListView):
    model = Category


class ForumListView(Dispatch302Mixin, DetailView):
    model = Category
    slug_url_kwarg = 'category_slug'
