from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView,DetailView,ListView
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy 
from . import forms
from django.shortcuts import render, get_object_or_404
from users.models import User
from .models import Message, Stock
from django.contrib.auth.decorators import login_required
import random

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


class HomeView(TemplateView):
    template_name = "umeo_site/home.html"
#ログインしてない時の処理を書かなきゃ（もしかしてこの処理，全部のページでいるのでは？）

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

class MessageIndexView(ListView):
    model = Message
    #templateにはmessage_list.htmlが自動的に選ばれる

class CreateMessageView(CreateView):
    model = Message
    form_class = forms.MessageForm
    success_url = reverse_lazy('umeo_site:message')

    def form_valid(self, form):
        form.instance.writer = self.request.user
        self.request.user.umeop += 1000
        self.request.user.save()
        return super(CreateMessageView, self).form_valid(form)

class RankView(ListView):
    #https://www.nblog09.com/w/2019/05/06/django-listview/
    #DjangoのListViewで順番を入れ替えたり絞込をする
    model = User
    template_name = "umeo_site/rank.html"
    
    def get_queryset(self):
        return User.objects.order_by('-umeop')

def StockView(request):
    return render(request, 'umeo_site/stock.html', {'now': Stock.objects.all().order_by('-created_at')[0],
                                                    'stock': Stock.objects.all().order_by('-created_at')[0:11]})
    #stock = Stock()
    #stock_before = Stock.objects.all().order_by('-created_at')[0]
    #stock.value = stock_before.value + random.randint(-100, 100)
    #stock.save()

def StockBuyView(request):
    user = request.user
    stock_now = Stock.objects.all().order_by('-created_at')[0]
    if user.umeop >= stock_now.value:
        user.umeop -= stock_now.value
        user.stock += 1
        user.save()
    return render(request, 'umeo_site/stock.html', {'now': Stock.objects.all().order_by('-created_at')[0],
                                                    'stock': Stock.objects.all().order_by('-created_at')[0:11]})

def StockSellView(request):
    user = request.user
    stock_now = Stock.objects.all().order_by('-created_at')[0]
    if user.stock > 0:
        user.umeop += stock_now.value
        user.stock -= 1
        user.save()
        #https://qiita.com/maisuto/items/eece9d880d94fd241a0d
        #renderの使い方
    return render(request, 'umeo_site/stock.html', {'now': Stock.objects.all().order_by('-created_at')[0],
                                                    'stock': Stock.objects.all().order_by('-created_at')[0:11]})



