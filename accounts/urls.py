
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    
    
]
