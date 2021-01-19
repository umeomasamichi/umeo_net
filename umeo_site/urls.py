from django.urls import path

from . import views

app_name = 'umeo_site'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('index/',views.IndexView.as_view(), name="index"),
    path('create/', views.UserCreateView.as_view(),name="create"),
    path('button/', views.UmeoButtonView,name="button"),
    path('bairitsu_change/', views.Bairitsu_Change, name="change"),
    path('base/', views.BaseView.as_view(), name="base"),
    path('home/', views.HomeView.as_view(), name="home"),
    path('message/', views.MessageIndexView.as_view(), name="message"),
    path('message_form/', views.CreateMessageView.as_view(), name="message_form"),
    path('rank/', views.RankView.as_view(), name="rank"),
    path('stock/', views.StockView, name="stock"),
    path('stock_buy/', views.StockBuyView, name="stock_buy"),
    path('stock_sell/', views.StockSellView, name="stock_sell"),
    path('upload/', views.UploadView, name='upload'),
    path('upload2/', views.Upload2View.as_view(), name='upload2'),
]