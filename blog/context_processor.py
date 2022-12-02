from .models import *
from .views import MyBlog

def blog_categories_list(request):
    blog_catogories = Category.objects.all()
    return dict(blog_categories = blog_catogories)