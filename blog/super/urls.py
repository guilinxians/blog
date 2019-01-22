from django.conf.urls import url
from django.urls import path

from super import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('article/', views.article, name='article'),
    path('add_article/', views.add_article, name='add_article'),
    path('category/', views.category, name='category'),
    path('update_category/', views.update_category, name='update_category'),
    path('del_category/', views.del_category, name='del_category'),
    path('del_article/', views.del_article, name='del_article'),
    path('update_article/', views.update_article, name='update_article'),
]