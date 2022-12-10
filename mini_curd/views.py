from django.shortcuts import render, redirect
from hashlib import md5

#登陆权限管理
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User

#登录窗体表单
from django import forms
from app_curd import forms as curd_forms

#timedelta
from datetime import timedelta

def test(request):
    if request.method == 'GET':
        User.objects.create_superuser(username='admin',password=md5(b'joe1sn').hexdigest(),email="joe1sn@foxmail.com")
        print("created")
    return redirect("/login/")

# 登陆页面 默认
def login(request):
    if request.method == 'GET':
        #已经登陆则重定向到index
        if request.session.get("is_login") == True:
            return redirect("/index/")
        form = curd_forms.login_form()
        return render(request, "login.html", {"form": form, "name":"Mini_CURD",})
    else :
        form = curd_forms.login_form(request.POST)
        if form.is_valid():  # 进行数据校验
            data = form.cleaned_data
            user = auth.authenticate(username=data["username"],password=md5(bytes(data["password"],encoding='utf-8')).hexdigest())
            if not user:
                return redirect("/login/")
            else:
                # 校验成功，进入管理页面
                auth.login(request, user)
                request.session["is_login"]=True
                path = request.GET.get("next") or "/index/"
                if data["keeped"] == True: #延长过期时间
                    request.session.set_expiry(timedelta(days=3)) 
                return redirect(path)
    return render(request, "login.html", {"form": form, "name":"Mini_CURD",})

def logout(request):
    auth.logout(request)
    return redirect("/login/")