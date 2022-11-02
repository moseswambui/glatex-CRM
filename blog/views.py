from django.shortcuts import render

def Blog(request):
    return render(request, 'blog/blog.html')