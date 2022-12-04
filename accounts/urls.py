
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('register/', views.Register, name='register'),
    path('login/', views.Login_User, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('myorder/', views.MyOrder, name='myorder'),
    path("dashboard/",views.Dashboard, name="dashboard"),
    path("profile/",views.Profile, name="profile"),
    path("connections/",views.Connections, name="connections"),
    path("notifucations/",views.Notifications, name="notifications"),
    path("add_blog/",views.AddBlog, name="add-blog"),
    path("blog/<slug:category_slug>/<slug:blog_slug>",views.BlogDetail, name="blog_detail"),
] 
