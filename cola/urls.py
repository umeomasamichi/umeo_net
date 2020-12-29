from django.urls import path

from . import views

app_name = 'cola'
urlpatterns = [
    #ex: /cola/
    path('', views.index, name='index'),
    #ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
]
