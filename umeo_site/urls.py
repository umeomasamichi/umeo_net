from django.urls import path

from . import views

app_name = 'umeo_site'
urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('index/',views.IndexView.as_view(), name="index"),
    path('create/', views.UserCreateView.as_view(),name="create"),
    path('button/', views.UmeoButtonView,name="button"),
    path('bairitsu_change/', views.Bairitsu_Change, name="change"),
    path('base/', views.BaseView.as_view(), name="base"),
    path('extends/', views.ExtendsView.as_view(), name="extends"),
]