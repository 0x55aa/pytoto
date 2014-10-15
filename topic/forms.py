# coding: utf-8
import datetime
from django.utils import timezone
from django import forms

from .models import Topic, Post


class TopicUpdateForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(), max_length=60000)

    def __init__(self, *args, **kwargs):
        super(TopicUpdateForm, self).__init__(*args, **kwargs)
        if hasattr(self.instance, 'forum'):
            tt_list = list(self.instance.forum.topictype_set.all().values_list('id', 'name'))
            tt_list.insert(0, ('', '------'))
            self.fields['topic_type'].choices = tt_list
            # self.fields['content'].initial = self.instance.get_topic_first_post().content
        else:
            'err'
        self.fields['subject'].widget.attrs['class'] = 'input_text'

    class Meta:
        model = Topic
        fields = ('topic_type', 'subject', 'content')

    def save(self, user, *args, **kwargs):
        topic = super(TopicUpdateForm, self).save(commit=False, *args, **kwargs)
        topic.update_user = user
        topic.updated_on = timezone.now()
        topic.save()
        post = topic.get_topic_first_post()
        post.content = self.cleaned_data['content']
        post.update_user = user
        post.updated_on = timezone.now()
        post.save()

        return topic


class TopicCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.forum = kwargs.pop('forum', None)
        super(TopicCreateForm, self).__init__(*args, **kwargs)
        tt_list = list(self.forum.topictype_set.all().values_list('id', 'name'))
        tt_list.insert(0, ('', '------'))
        self.fields['topic_type'].choices = tt_list
        self.fields['subject'].widget.attrs['class'] = 'input_text'

    class Meta:
        model = Topic
        # 先去掉'slug',
        fields = ('tag', 'topic_type', 'subject', )
        labels = {
            'tag': '',
        }
        widgets = {
            'tag': forms.HiddenInput(),
        }

    def save(self, user, create=True, *args, **kwargs):
        topic = super(TopicCreateForm, self).save(commit=False, *args, **kwargs)
        if create:
            topic.user = user
            topic.last_reply_user = user
            topic.forum = self.forum
            topic.save()
            self.forum.topic_count += 1
            self.forum.save()
        else:
            topic.update_user = user
            topic.last_reply_on = timezone.now()
            topic.save()
        return topic


class PostCreateFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('parent', 'content', 'reply_email')
        labels = {
            'parent': '',
            'content': '',
        }
        widgets = {
            'parent': forms.HiddenInput(),
        }

    def save(self, user, topic, create=True, *args, **kwargs):
        post = super(PostCreateFrom, self).save(commit=False, *args, **kwargs)
        if create:
            post.user = user
            post.topic = topic
            post.floor = post.topic.reply_count + 1
            post.save()
            # 统计
            post.topic.reply_count += 1
            post.topic.last_reply_user = user
            post.topic.last_reply_on = timezone.now()
            post.topic.save()
            if post.parent:
                post.parent.reply_count += 1
                post.parent.save()

            topic.forum.post_count += 1
            today = datetime.date.today()
            if topic.forum.post_count_day == today:
                topic.forum.today_post_count += 1
            else:
                topic.forum.today_post_count = 1
                topic.forum.post_count_day = today
            topic.forum.save()
        else:
            post.update_user = user
            post.last_reply_on = timezone.now()
            post.save()

        return post
