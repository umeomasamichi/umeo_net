from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView,DetailView,ListView, FormView
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy 
from . import forms
from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from .models import Message, Stock, Music, Good
from django.contrib.auth.decorators import login_required
import random
from datetime import date, datetime, timedelta
from django.http import HttpResponse

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


today = datetime.today()
birth_day = datetime(2021, 10, 1)
dt = birth_day - today

class HomeView(TemplateView):
    template_name = "umeo_site/home.html"
    def get(self, request, *args, **kwargs):
        user = self.request.user
        #https://blog.qs-grct.com/2018/10/30/010054/post-1307/
        if user.is_anonymous:
            return render(request, "umeo_site/index.html")
        #まず日付を持ってくる．このとき，9時間進めないと，dayの情報がちゃんと取れないので注意（日本時間が9時間ずれていることに由来）
        last_login = today
        tmp_date_mylogin = user.date_mylogin + timedelta(hours=9)
        date_mylogin = datetime(tmp_date_mylogin.year, tmp_date_mylogin.month, tmp_date_mylogin.day)

        deltadays = (last_login - date_mylogin)

        user.date_mylogin = today
        #flagはログインボーナス表示をするどうか
        if deltadays.days == 1:
            #1日ぶりにログインしたら，継続日数をプラス１して，保存して，投げる．
            user.running_days += 1
            user.stock += user.running_days
            user.save()
            r_days = user.running_days
            ''' これやるとしたら，saveの前にstockの処理やらなあかんのと，日数と株の表示を分けなきゃいけない
            if r_days % 10 == 0:
                r_days *= 10
            '''
            return render(request, "umeo_site/home.html", {'r_days': r_days, 'flag': 1, "remain":dt.days})
        elif deltadays.days > 1:
            #2日以上空けてログインしたら，継続日数を１にして，保存して，投げる
            user.running_days = 1
            user.stock += 1
            user.save()
            r_days = user.running_days
            return render(request, "umeo_site/home.html", {'r_days': r_days, 'flag': 1, "remain":dt.days})
        else:
            #その日にログインしてたら，ボーナス表示を出さない
            user.save()
            return render(request, "umeo_site/home.html", {'r_days': user.running_days, 'flag': 0, "remain":dt.days})
#ログインしてない時の処理を書かなきゃ（もしかしてこの処理，全部のページでいるのでは？）

class UserCreateView(CreateView):
    form_class = forms.UserCreationForm
    template_name = "umeo_site/create.html"
    success_url = reverse_lazy("umeo_site:login")

#login中のユーザの情報をどうにかする
#https://awesome-linus.com/2019/04/05/django-get-login-user/
@login_required
def UmeoButtonView(request):
    #if request.method == 'POST':
    #    user.umeop += user.bairitsu
    #    user.save()
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


#https://blog.narito.ninja/detail/61
#二つ以上のボタンを認識する方法
def UmeoButtonAjax(request):
    user = request.user
    bai = user.bairitsu
    if request.method == 'GET':
        #クエリを使っている
        id = request.GET.get("id")
        #idはstringであることに注意
        if id == '100':
            user.umeop += user.bairitsu
            user.save()
        elif request.GET["id"] == '200':
            if user.umeop >= (bai*bai*10):
                user.umeop -= (bai*bai*10)
                user.bairitsu += 1
                user.save()
        return HttpResponse("<h3>"+ str(user.username) +"さんの梅尾ポイントは" + str(user.umeop) + "Pです</h3>" +
                            "<h3>"+ str(user.username) +"さんのレベルは" + str(user.bairitsu) +"です</h3>" +
                            "<h3 class='mb-5'>次のレベルに進むためのポイントは" + str(user.bairitsu*user.bairitsu*10) +"Pです</h3>")
    else:
        return HttpResponse("failed")




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
        return User.objects.exclude(username='admin').order_by('-bairitsu')

def StockView(request):
    user = request.user
    f = forms.StockForm()
    id = request.GET.get("id")
    stock_now = Stock.objects.all().order_by('-created_at')[0]
    if "number" in request.POST:
        number = int(request.POST["number"])
        if id == '100':
            #できれば，無理な時の処理もelseで書きたい
            if user.umeop >= (stock_now.value * number):
                user.umeop -= stock_now.value * number
                user.stock += number
                user.save()
        elif id=='200':
            if user.stock - number >= 0:
                user.umeop += stock_now.value * number
                user.stock -= number
                user.save()
    return render(request, 'umeo_site/stock.html', {'now': Stock.objects.all().order_by('-created_at')[0],
                                                    'stock': Stock.objects.all().order_by('-created_at')[0:100],
                                                    'form':f})

#class StockView(TemplateView):
#   template_name = 'umeo_site/stock.html'
    
'''
def StockBuyView(request):
    user = request.user
    stock_now = Stock.objects.all().order_by('-created_at')[0]
    if user.umeop >= stock_now.value:
        user.umeop -= stock_now.value
        user.stock += 1
        user.save()
    return render(request, 'umeo_site/stock.html', {'now': Stock.objects.all().order_by('-created_at')[0],
                                                    'stock': Stock.objects.all().order_by('-created_at')[0:30]})

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
                                                    'stock': Stock.objects.all().order_by('-created_at')[0:30]})
'''

def UploadView(request):
    if request.method == 'POST':
        form = forms.MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('umeo_site:home')
    else:
        form = forms.MusicForm()
    return render(request, 'umeo_site/model_form_upload.html', {
        'form': form
    })

class Upload2View(TemplateView):
    template_name = "umeo_site/upload2.html"

class GalleryView(TemplateView):
    template_name = "umeo_site/gallery.html"

class TypeView(TemplateView):
    template_name = "umeo_site/type.html"

    '''
    def get(self, request, *args, **kwargs):
        user = self.request.user
        #まず日付を持ってくる．このとき，9時間進めないと，dayの情報がちゃんと取れないので注意（日本時間が9時間ずれていることに由来）
        tmp_last_login = user.last_login + timedelta(hours=9)
        tmp_date_mylogin = user.date_mylogin + timedelta(hours=9)

        last_login = datetime(tmp_last_login.year, tmp_last_login.month, tmp_last_login.day)
        date_mylogin = datetime(tmp_date_mylogin.year, tmp_date_mylogin.month, tmp_date_mylogin.day)

        deltadays = (last_login - date_mylogin)

        user.date_mylogin = user.last_login
        #flagはログインボーナス表示をするどうか
        if deltadays.days == 1:
            #1日ぶりにログインしたら，継続日数をプラス１して，保存して，投げる．
            user.running_days += 1
            user.stock += user.running_days
            user.save()
            r_days = user.running_days
            return render(request, "umeo_site/type.html", {'r_days': r_days, 'flag': 1})
        elif deltadays.days > 1:
            #2日以上空けてログインしたら，継続日数を１にして，保存して，投げる
            user.running_days = 1
            user.stock += 1
            user.save()
            r_days = user.running_days
            return render(request, "umeo_site/type.html", {'r_days': r_days, 'flag': 1})
        else:
            #その日にログインしてたら，ボーナス表示を出さない
            user.save()
            return render(request, "umeo_site/type.html", {'r_days': user.running_days, 'flag': 0})
    '''


class SkrollrView(TemplateView):
    template_name = "umeo_site/skrollr.html"



class GreetView(FormView):
    template_name = 'umeo_site/index2.html'  # テンプレート名(htmlファイル名)
    form_class = forms.GreetForm
    success_url = '/greet'

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        if form.is_valid():
            if request.is_ajax():
                """Ajax 処理を別メソッドに切り離す"""
                print('### Ajax request')
                return self.ajax_response(form)
            # Ajax 以外のPOSTメソッドの処理
            return super().form_valid(form)
        # フォームデータが正しくない場合の処理
        return super().form_invalid(form)

    def ajax_response(self, form):
        """jQuery に対してレスポンスを返すメソッド"""
        name = form.cleaned_data.get('name')
        return HttpResponse(f'こんにちは、{name}さん！')

class TypingView(ListView):
    model = User
    template_name = "umeo_site/typing.html"
    def get_queryset(self):
        return User.objects.exclude(username='admin').order_by('-type_score')


def TypingAjax(request):
    user = request.user
    if request.method == 'GET':
        #クエリを使っている
        score = int(request.GET.get("score"))
        if user.type_score <= score:
            user.type_score = score 
        user.umeop += score       
        user.save()
        return HttpResponse("succesed")
    else:
        return HttpResponse("failed")


class GoodListView(ListView):
    model = Good
    template_name = "umeo_site/good_list.html"
    #templateにはmessage_list.htmlが自動的に選ばれるので，
    #template_nameで上書き．

class GoodCreateView(CreateView):
    model = Good
    template_name = "umeo_site/message_form.html"
    form_class = forms.GoodForm
    success_url = reverse_lazy('umeo_site:good')

    def form_valid(self, form):
        form.instance.writer = self.request.user
        self.request.user.umeop += 1000
        self.request.user.save()
        return super(GoodCreateView, self).form_valid(form)