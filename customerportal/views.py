from typing import ItemsView
from django.core import exceptions
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from datetime import date
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def Index(request):
    products = Product.objects.all()
    large_format = Product.objects.all()
    context = {'products':products}
    return render(request,"index.html",context )

def Shop(request,category_slug=None):
    categories=None
    products = None

    if category_slug !=None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories)
        paginator = Paginator(products,6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count=products.count()

    else:
        products = Product.objects.all()
        paginator = Paginator(products,9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
    context = {'products':paged_products,'products_count':products_count}
    return render(request,"customer_shop.html",context )

def ProductDetail(request,product_slug,category_slug):
    today = date.today()
    
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request),product=single_product).exists()
        product_images = single_product.productimages_set.all()
        
        
        all_products = Product.objects.all().order_by('-id')[:10]
    except Exception as e:
        raise e

    context = {
        'single_product':single_product,
        'in_cart':in_cart,
        'all_products':all_products,
        'today':today,
        'product_images':product_images,
    }
    return render(request, 'customer_single-product.html',context)

def  _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    product_variation = []
    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]
            print(key, value)

            try:
                variation = Variation.objects.get(product=product,variation_category__iexact=key, variation_value__iexact=value)
                product_variation.append(variation)

            except:
                pass

    try:
        cart = MyCart.objects.get(cart_id = _cart_id(request))
    except MyCart.DoesNotExist:
        cart = MyCart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
    return redirect('cart')


def Cart(request, total=0,quantity=0,cart_items=None):
    try:
        cart= MyCart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

        tax = (2*total)/100
        grand_total = total + tax
    except exceptions.ObjectDoesNotExist:
        pass
    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total,
    } 
    return render(request, 'customer_cart.html',context)

def remove_cart(request, product_id):
    cart = MyCart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    
    cart_item.delete()

    return redirect('cart')

def Services(request, servicecategory_slug = None):
    servicecategories =None
    services = None

    if servicecategory_slug != None:
        servicecategories = get_object_or_404(ServiceCategory, slug = servicecategory_slug)
        services = Service.objects.filter(category=servicecategories)
        paginator = Paginator(services, 1)
        page = request.GET.get('page')
        paged_services = paginator.get_page(page)
        service_count =  services.count()

    else:
        services = Service.objects.all()
        paginator = Paginator(services, 3)
        page = request.GET.get('page')
        paged_services = paginator.get_page(page)
        service_count =  services.count()
    context = {
        'services':paged_services,
        'service_count':service_count,
    }
    return render(request,"customer_services.html",context )

def AboutUs(request):
    return render(request,"customer_about-us.html" )

def Checkout(request):
    return render(request,"customer_checkout.html" )

def ContactUs(request):
    return render(request,"customer_contact.html" )

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains = keyword))

    context = {
        'products':products,
    }
    return render(request,'customer_shop.html',context)