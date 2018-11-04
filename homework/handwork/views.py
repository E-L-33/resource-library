from django.shortcuts import render
# from django.contrib import auth    可以使用django的内置登录模块
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    # 注册呀
    return render(request, 'register.html')


def userlogin(request):
    # 登录呀
    return render(request, 'login.html')


def homework(request):
    # 展示页面
    return render(request, 'home.html')
