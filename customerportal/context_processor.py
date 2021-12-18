from .models import *
from .views import _cart_id

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

def counter(request):
    cart_count = 0

    if 'admin' in request.path:
        return {}

    else: 
        try:
            cart = MyCart.objects.filter(cart_id = _cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity


        except MyCart.DoesNotExist:
            cart_count =0

    return dict(cart_count=cart_count)

def service_links(request):
    mylinks = ServiceCategory.objects.all()
    return dict(mylinks=mylinks)

def type_links(request):
    typelinks = ProductType.objects.all()
    return dict(typelinks=typelinks)

def tag_links(request):
    taglinks = ProductTag.objects.all()
    return dict(taglinks=taglinks)