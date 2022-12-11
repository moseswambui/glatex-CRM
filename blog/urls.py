from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.MyBlog, name='blog'),
    path("home/category/<slug:category_slug>/",views.MyBlog, name="blog_by_category"),
    path("home/category/<slug:category_slug>/<slug:blog_slug>",views.BlogDetail, name="blog_detail"),
    path('search/', views.search, name='search'),
]
