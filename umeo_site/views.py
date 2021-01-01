from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView,DetailView
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy 
from . import forms
from django.shortcuts import render, get_object_or_404
from users.models import User
from django.contrib.auth.decorators import login_required

#hombre-nuevo.com/python/python0048/
#Userのモデルを継承して改造(umeopを持つように変更)
#https://hodalog.com/how-to-reset-migrations/

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "umeo_site/login.html"

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "umeo_site/logout.html"

class IndexView(TemplateView):
    template_name = "umeo_site/index.html"

class UserCreateView(CreateView):
    form_class = forms.UserCreationForm
    template_name = "umeo_site/create.html"
    success_url = reverse_lazy("umeo_site:login")

#login中のユーザの情報をどうにかする
#https://awesome-linus.com/2019/04/05/django-get-login-user/
@login_required
def UmeoButtonView(request):
    user = request.user
    if request.method == 'POST':
        user.umeop += user.bairitsu
        user.save()
    return render(request, 'umeo_site/button.html')

#https://codelab.website/django-templatetags/
#テンプレートタグに，掛け算をおこなうものがないので，上のurlを参考に作成
def Bairitsu_Change(request):
    user = request.user
    bai = user.bairitsu
    if user.umeop >= (bai*bai*10):
        user.umeop -= (bai*bai*10)
        user.bairitsu += 1
        user.save()
    return render(request, 'umeo_site/button.html')

class BaseView(TemplateView):
    template_name = "umeo_site/base.html"

class ExtendsView(TemplateView):
    template_name = "umeo_site/extends.html"
