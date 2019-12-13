from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('main', views.main, name='main'),
    path('info', views.info, name='info'),
    path('demourl', views.demourl, name='demourl'),
    path('demo', views.demo, name='demo'),
]