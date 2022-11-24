from django import forms
from django.core.exceptions import ValidationError
from app_curd import models

#登录框
class login_form(forms.Form):
    username = forms.CharField(max_length=20)  # 用户名
    password = forms.CharField(max_length=32)  # sha1(密码)
    keeped = forms.BooleanField(required=False) #记住密码


