from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Blog, name='blog'),
    path('single', views.Detail_blog, name='detail-blog'),
    
]
