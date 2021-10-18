from django.core import exceptions
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def Index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,"index.html",context )

def Shop(request,category_slug=None):
    categories=None
    products = None

    if category_slug !=None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories)
        paginator = Paginator(products,3)
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
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request),product=single_product).exists()
    except Exception as e:
        raise e

    context = {'single_product':single_product, 'in_cart':in_cart}
    return render(request, 'customer_single-product.html',context)

def  _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    print("added")
    product = Product.objects.get(id=product_id)
    
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

def AboutUs(request):
    return render(request,"customer_about-us.html" )

def Checkout(request):
    return render(request,"customer_checkout.html" )

def ContactUs(request):
    return render(request,"customer_contact.html" )

