# coding: utf-8
from django.views.generic.base import TemplateView

from topic.models import Topic


class HomeView(TemplateView):
    template_name = "home.html"
    display_count = 5

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.filter(homepage=True).order_by('created_on')[:5]
        return context
