# coding: utf-8
import time
import json
import os.path

from django.views.generic import View
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
# from django.core.urlresolvers import reverse
from django.conf import settings

from .models import Topic, Post, TopicType
from .forms import TopicCreateForm, PostCreateFrom, TopicUpdateForm

from lib.mixin import SlugMixin, DispatchLoginMixin, Dispatch302Mixin, DispatchAdminMixin
from lib.util import js_escape
from forum.models import Forum


class TopicIndexView(ListView):
    model = Topic
    context_object_name = "topics"
    paginate_by = "30"

    def get_context_data(self, **kwargs):
        context = super(TopicIndexView, self).get_context_data(**kwargs)
        context['forum_topic_total'] = Forum.objects.get_all_forum_count()
        context['is_total'] = True
        return context

    def get_queryset(self):
        return self.model.objects.filter(closed=False)


class TypeTopicListView(Dispatch302Mixin, ListView):
    template = "topic/topic_list.html"
    model = TopicType
    slug_url_kwarg = 'type_slug'
    context_object_name = "topics"
    paginate_by = "30"

    def get_object(self):
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        if slug is not None:
            slug_field = self.get_slug_field()
            self.object = get_object_or_404(self.model, **{slug_field: slug})
            return self.object

        raise AttributeError("no slug_url_kwarg")

    def get_queryset(self):
        return Topic.objects.filter(closed=False, topic_type=self.object)

    def get_context_data(self, **kwargs):
        context = super(TypeTopicListView, self).get_context_data(**kwargs)

        context['type'] = self.object
        context['forum'] = self.object.forum
        return context


class TopicCreateView(DispatchLoginMixin, Dispatch302Mixin, DetailView):
    template = "topic/topic_create.html"
    model = Forum
    slug_url_kwarg = 'forum_slug'

    def get(self, request, *args, **kwargs):
        topic_form = TopicCreateForm(forum=self.object)
        post_form = PostCreateFrom()
        context = {'topic_form': topic_form, 'post_form': post_form, }
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        topic_form = TopicCreateForm(request.POST, forum=self.object)
        post_form = PostCreateFrom(request.POST)
        if topic_form.is_valid() and post_form.is_valid():
            user = request.user
            topic = topic_form.save(user=user)
            post_form.save(user=user, topic=topic)
            return HttpResponseRedirect(topic.get_absolute_url())

        context = {'topic_form': topic_form, 'post_form': post_form, }
        return render(request, self.template, context)


class TopicDetailView(Dispatch302Mixin, DetailView):
    model = Topic
    slug_url_kwarg = 'topic_slug'

    def get_context_data(self, **kwargs):
        self.object.view_count_add()
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['post_form'] = PostCreateFrom()
        return context


class TopicListView(Dispatch302Mixin, ListView):
    model = Forum
    context_object_name = "topics"
    slug_url_kwarg = 'forum_slug'
    paginate_by = "30"

    def get_object(self):
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        if slug is not None:
            slug_field = self.get_slug_field()
            self.object = get_object_or_404(self.model, **{slug_field: slug})
            return self.object

        raise AttributeError("no slug_url_kwarg")

    def get_queryset(self):
        self.forum = self.object
        return Topic.objects.filter(closed=False, forum=self.forum)

    def get_context_data(self, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)

        context['forum'] = self.forum
        return context


class TopicUpdateView(DispatchLoginMixin, SlugMixin, DetailView):
    template = "topic/topic_update.html"
    model = Topic
    slug_url_kwarg = 'topic_slug'
    http_method_names = ['post', 'get', ]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = TopicUpdateForm(instance=self.object)
        content = self.object.get_topic_first_post().content
        content = js_escape(content)
        context = {'form': form, 'content': content}
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = TopicUpdateForm(request.POST, instance=self.object)
        if form.is_valid():
            user = request.user
            topic = form.save(user=user)
            return HttpResponseRedirect(topic.get_absolute_url())

        context = {'form': form}
        return render(request, self.template, context)


class PostSpamView(DispatchLoginMixin, SlugMixin, DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        status = self.object.user_spam(request.user)
        if status:
            r = {'status': True, 'msg': u'举报成功'}
        else:
            r = {'status': False, 'msg': u'已经举报过了'}
        return HttpResponse(json.dumps(r), content_type="application/json")


class TopicHomepageDetailView(DispatchAdminMixin, SlugMixin, DetailView):
    model = Topic
    slug_url_kwarg = 'topic_slug'
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        status = self.object.set_homepage(request.user)
        if status:
            r = {'status': True, 'msg': u'操作成功'}
        else:
            r = {'status': False, 'msg': u'操作失败'}
        return HttpResponse(json.dumps(r), content_type="application/json")


class PostLikeView(DispatchLoginMixin, SlugMixin, DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        status = self.object.user_like(request.user)
        if status:
            r = {'status': True, 'msg': u'赞成功'}
        else:
            r = {'status': False, 'msg': u'已经赞过了'}
        return HttpResponse(json.dumps(r), content_type="application/json")


class PostCreateView(DispatchLoginMixin, SlugMixin, SingleObjectMixin, FormView):
    model = Topic
    form_class = PostCreateFrom
    slug_url_kwarg = 'topic_slug'
    http_method_names = ['post', ]

    def get_success_url(self):
        pass

    def form_invalid(self, form):
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/'))

    def form_valid(self, form):
        topic = self.get_object()
        form.save(user=self.request.user, topic=topic)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/'))


class PostDeleteView(DispatchAdminMixin, SlugMixin, DeleteView):
    model = Post
    slug_url_kwarg = 'post_slug'
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.user_delete(request.user)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/'))
        r = {'status': True, 'msg': u'删除成功'}
        return HttpResponse(json.dumps(r), content_type="application/json")


MAX_FILE_SIZE = 2 * 2 ** 20  # 2 Mb
MIX_FILE_SIZE = 3 * 2 ** 10	 # 3 Kb
ACCEPTED_FORMATS = (
    "image/pjpeg",
    "image/jpeg",
    "image/png",
    "image/gif",
)
ACCEPTED_EXT = ('jpeg', 'jpg', 'png', 'gif')


class UploadImgView(DispatchLoginMixin, View):
    http_method_names = ['post', ]

    def post(self, request, *args, **kwargs):
        f = request.FILES['upload_file']
        ext = f.name.split('.')[-1]
        if f.size > MAX_FILE_SIZE or f.size < MIX_FILE_SIZE:
            r = {'success': False, 'msg': '文件大小要在2M-1K之间'}
            return HttpResponse(json.dumps(r), content_type="application/json")
        if f.content_type not in ACCEPTED_FORMATS or ext not in ACCEPTED_EXT:
            r = {'success': False, 'msg': '图片类型错误'}
            return HttpResponse(json.dumps(r), content_type="application/json")

        userid = hex(request.user.pk)[2:]
        second_time = hex(int(time.time()))[2:]
        file_name = "%s%s.%s" % (second_time, userid, ext)
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        with open(file_path, 'wb') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        r = {'success': True, 'file_path': settings.MEDIA_URL_ + file_name}
        return HttpResponse(json.dumps(r), content_type="application/json")
