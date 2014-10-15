# coding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserCreationForm,
    AuthenticationForm,
)


class PasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'input-block-level'
            field.widget.attrs['placeholder'] = field.label


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'enter-item'
            field.widget.attrs['placeholder'] = field.label


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'input_kuang item val_m errortip'
            field.widget.attrs['placeholder'] = field.label

    class Meta:
        model = User
        fields = ('email', 'username', )

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError(u'email必填项')
        return email

    def clean_username(self):
        forbidden_name = ['admin', 'xxx']
        username = self.cleaned_data['username']
        for name in forbidden_name:
            if name in username:
                raise forms.ValidationError(u'改名字已被注册')
        return username
