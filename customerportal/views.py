from django.shortcuts import render

def Index(request):
    return render(request,"customerportal\index.html" )
