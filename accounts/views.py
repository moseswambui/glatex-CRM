from django.shortcuts import render

def Register(request):
    return render(request, 'customer_register.html')

def Login(request):
    return render(request, 'customer_login.html')

def Logout(request):
    return render(request, 'customer_logout.html')
