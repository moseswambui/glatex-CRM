from django.shortcuts import render
from .models import Blog

def MyBlog(request):
    blogs = Blog.objects.all()
    for blog in blogs:
        print(blog.title)

    context = {
        'blogs':blogs
    }
    return render(request, 'blog/blog.html', context)