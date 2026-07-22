from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('welcome/', views.welcome),
    path('', views.welcome),
    path('signup/', views.user_signup),
    path('signin/', views.user_signin),
    path('logout/', views.user_logout),
    path('list/', views.user_list),
    path('delete/<int:id>/', views.delete_user),
    path('save/', views.user_save),
    path('save/<int:id>/', views.user_save),

]
