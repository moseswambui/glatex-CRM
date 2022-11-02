from multiprocessing import context
from typing import ItemsView
from django.core import exceptions
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from datetime import date
from django.db.models import Q
from django.core.mail import send_mail
import json
from django.template.loader import render_to_string
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
def OnlinePayment(request):
    print("we are here")
    body = json.loads(request.body)
    #store transaction details
    print("we are here")
    payment = Payment(name = body['name'],amount_paid=body['amount_paid'],email_address=body['email_address'], area=body['area'], payment_id=body['transID'],payment_method = body['payment_method'], status = body['status'])
    payment.save()
    print("payment saved")
    return render(request, 'customer_checkout.html')

def Orders(request):
    orders = Payment.objects.all()
    context = {
        'orders':orders
    }
    return render(request, 'customer_orders.html', context)

def Index(request):
    products = Product.objects.all()
    large_format = ProductType.objects.filter(name='Large Format')
    services = Service.objects.all()
    
   
    context = {
        'products':products,
        'large_format':large_format,
        'services': services,
        }
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
    current_user = request.user
    product = Product.objects.get(id=product_id)

    if current_user.is_authenticated:
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
       
        is_cart_item_exists = CartItem.objects.filter(product=product,cart=cart, user=current_user).exists()

        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(product=product,cart=cart, user = current_user)

            ex_vars_list = []
            id = []

            for item in cart_item:
                existing_variation = item.variations.all()
                ex_vars_list.append(list(existing_variation))
                id.append(item.id)

            print(ex_vars_list)

            if product_variation in ex_vars_list:
                index = ex_vars_list.index(product_variation)
                item_id = id[index]
                item =CartItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()

            else:
                item = CartItem.objects.create(product=product, quantity=1,cart=cart, user = current_user)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)

                item.save()

        else:
            cart_item= CartItem.objects.create(
                product=product,
                quantity = 1,
                user = current_user,
                cart=cart,
            )
            if len(product_variation)  > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)

            cart_item.save()

        return redirect("cart")

    else:
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
        is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()

        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(product=product, cart=cart)

            ex_vars_list = []
            id = []

            for item in cart_item:
                existing_variation = item.variations.all()
                ex_vars_list.append(list(existing_variation))
                #id.append(item.id)

            print(ex_vars_list)

            if product_variation in ex_vars_list:
                index = ex_vars_list.index(product_variation)
                item_id = id[index]
                item =CartItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()

            else:
                item = CartItem.objects.create(product=product, quantity=1, cart=cart)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)

                item.save()

        else:
            cart_item= CartItem.objects.create(
                product=product,
                quantity = 1,
                cart = cart,
            )
            if len(product_variation)  > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)

            cart_item.save()

        return redirect("cart")

        


def Cart(request, total=0,quantity=0,cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items= CartItem.objects.filter(user=request.user)

        else:
            cart= MyCart.objects.get(cart_id = _cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart)
        #my_items = []

        """for item in cart_items:
            product_name = item.product.name
            my_items.append(product_name)
        string_items = ''.join([str(item) for item in my_items])
        print(string_items)"""

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
    """
    send_mail(
        "oder fullfillment",
        "Order Received successfully",
        "moseswambui044@gmail.com",
        ['blackuser321@gmail.com'],
        fail_silently=False,

    )
    """
    return render(request, 'customer_cart.html',context)

def remove_cart(request, product_id, cart_item_id):
    
    product = get_object_or_404(Product, id=product_id)

    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)

        else:
            cart = MyCart.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
            
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save() 
        else:
            cart_item.delete()

    except:
        pass
    
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

@login_required(login_url = 'login')
def Checkout(request, total=0, quantity=0, cart_items=None):
    try:
        total = 0
        tax = 0
        if request.user.is_authenticated:
            
            cart_items = CartItem.objects.filter(user=request.user)

        else:
            cart= MyCart.objects.get(cart_id = _cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart)
        my_items = []
        for item in cart_items:
            product_name = item.product.name
            my_items.append(product_name)
        string_items = ''.join([str(item) for item in my_items])
        print(string_items)
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
        'string_items':string_items
    }
    return render(request,"customer_checkout.html", context )

def ContactUs(request):
    return render(request,"customer_contact.html" )

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(name__icontains = keyword))

    context = {
        'products':products,
    }
    return render(request,'customer_shop.html',context)
@login_required(login_url = 'login')
def Dashboard(request):
    user = request.user
    total = 0
    tax = 0
    quantity = 0
    if user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)

    else:
        pass
    my_items = []

    for item in cart_items:
        product_name = item.product.name
        my_items.append(product_name)

    string_items = ''.join([str(item) for item in my_items])

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

    tax = (2*total)/100
    grand_total = total + tax

    context = {
        "cart_items":cart_items,
        'grand_total': grand_total,
        'my_items':my_items,
        "string_items":string_items,
        "quantity":quantity,
    }
        
    return render(request,'accounts/index.html', context)
@login_required(login_url = 'login')
def Orders(request):
    return render(request, "accounts/orders.html")