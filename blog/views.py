from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog,Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def MyBlog(request, category_slug=None):

    categories = None
    blogs = None

    if category_slug !=None:
        categories = get_object_or_404(Category, slug=category_slug)
        blogs = Blog.objects.filter(category=categories)
        blog_count = blogs.count()
        paginator = Paginator(blogs, 4)
        page = request.GET.get('page')
        paged_blogs = paginator.get_page(page)
       

    else:
        blogs = Blog.objects.all()
        blog_count = blogs.count()
        paginator = Paginator(blogs, 4)
        page = request.GET.get('page')
        paged_blogs = paginator.get_page(page)

       
    context = {
        'blogs':paged_blogs,
        'blog_count':blog_count,
    }
    return render(request, 'blog/blog.html', context)

def BlogDetail(request,blog_slug, category_slug):
    try:
        single_blog = Blog.objects.get(category__slug=category_slug, slug=blog_slug)
        all_blogs = Blog.objects.all()

    except Exception as e:
        raise e

    context = {
        "single_blog":single_blog,
    }

    return render(request, 'blog/blog_detail.html', context)