from django.urls import path

from . import views

app_name = 'umeo_site2022'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('index/',views.IndexView.as_view(), name="index"),
    path('home/', views.HomeView.as_view(), name="home"),
    path('create/', views.UserCreateView.as_view(),name="create"),
    path('base/', views.BaseView.as_view(), name="base"),
    path('button/', views.UmeoButtonView,name="button"),
    path('button/ajax/', views.UmeoButtonAjax,name="button_ajax"),
    path('bairitsu_change/', views.Bairitsu_Change, name="change"),
    path('rank/', views.RankView.as_view(), name="rank"),
]

'''
    
    path('message/', views.MessageIndexView.as_view(), name="message"),
    path('message_form/', views.CreateMessageView.as_view(), name="message_form"),
    path('stock/', views.StockView, name="stock"),
    #path('stock_buy/', views.StockBuyView, name="stock_buy"),
    #path('stock_sell/', views.StockSellView, name="stock_sell"),
    path('upload/', views.UploadView, name='upload'),
    path('upload2/', views.Upload2View.as_view(), name='upload2'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('type/', views.TypeView.as_view(), name='type'),
    path('skrollr/', views.SkrollrView.as_view(), name='skrollr'),
    path('greet/', views.GreetView.as_view(), name='greet'),
    path('typing/', views.TypingView.as_view(), name='typing'),
    path('typing/ajax/', views.TypingAjax, name="typing_ajax"),
    path('good100/', views.GoodListView.as_view(), name="good"),
    path('good100_form/', views.GoodCreateView.as_view(), name="good_form"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    '''