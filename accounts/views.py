# coding: utf-8
import json

from django.views.generic.edit import CreateView
from django.views.generic.base import View, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import get_object_or_404

from .forms import RegisterForm


class RegisterView(CreateView):
    model = User
    template_name = "accounts/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class ProfileView(TemplateView):
    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)

        if 'user_id' in self.kwargs:
            context['user'] = get_object_or_404(User, id=self.kwargs['user_id'])
        else:
            context['user'] = self.request.user

        return context
