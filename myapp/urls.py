from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('main/', views.main_view, name='main'),
    path('seller/', views.seller_view, name='seller'),

]
