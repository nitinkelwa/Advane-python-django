from django.urls import path, include
from . import views

urlpatterns = [
    path('hi/', views.text_ors),
    path('', views.welcome),
    path('welcome/', views.welcome),
    path('login/', views.login),
    path('registration/', views.registration),
]
