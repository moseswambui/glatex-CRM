from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.MyBlog, name='blog'),
    path("home/category/<slug:category_slug>/",views.MyBlog, name="blog_by_category"),
    
]
