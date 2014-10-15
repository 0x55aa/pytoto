# coding: utf-8
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required


class SlugMixin(object):
    def get_slug_field(self):
        slug = self.kwargs[self.slug_url_kwarg]
        if slug.isdigit():
            return 'pk'
        else:
            return 'slug'


class DispatchLoginMixin(object):
    """
    登陆验证
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DispatchLoginMixin, self).dispatch(request, *args, **kwargs)


class DispatchAdminMixin(object):
    """
    admin登陆验证
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DispatchAdminMixin, self).dispatch(request, *args, **kwargs)


class Dispatch302Mixin(SlugMixin):
    """
    slug后边设置 ，302跳转
    """
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.get_slug_field() == 'pk' and self.object.slug:
            self.kwargs[self.slug_url_kwarg] = self.object.slug
            return HttpResponseRedirect(reverse(request.resolver_match.url_name, kwargs=self.kwargs))
        return super(Dispatch302Mixin, self).dispatch(request, *args, **kwargs)
