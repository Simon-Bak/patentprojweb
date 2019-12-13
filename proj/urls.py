from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('main', views.main, name='main'),
    path('info', views.info, name='info'),
    path('demo', views.demo, name='demo'),
    path('testurl', views.testurl, name='testurl'),
    path('result', views.result, name='result')
]