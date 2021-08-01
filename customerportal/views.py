from django.shortcuts import render

def Index(request):
    return render(request,"index.html" )

def Shop(request):
    return render(request,"customer_shop.html" )

def AboutUs(request):
    return render(request,"customer_about-us.html" )

def Checkout(request):
    return render(request,"customer_checkout.html" )

def ContactUs(request):
    return render(request,"customer_contact.html" )

