
from django.urls import path

from myblog import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('gbook/', views.gbook, name='gbook'),
    path('index/', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('infopic/', views.infopic, name='infopic'),
    path('list/', views.list, name='list'),
    path('column', views.column, name='column'),

]