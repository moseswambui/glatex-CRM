from django.shortcuts import render

def Blog(request):
    return render(request, 'blog/blog.html')

def Detail_blog(request):
    return render(request,'blog/single-detail-blog.html')