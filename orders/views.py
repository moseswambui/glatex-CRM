from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime

from customerportal.models import CartItem
from orders.forms import OrderForm
from orders.models import Order

def payments(request):
    return render(request,"order/payments.html")

def place_order(request, total = 0, quantity=0):
    current_user = request.user
    print(current_user)

    cart_items = CartItem.objects.filter(user = current_user)
    cart_count = cart_items.count()

    if cart_count <= 0:
        return redirect('shop')

    grand_total = 0
    tax = 0

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity) 
        quantity += cart_item.quantity

    tax = (2 * total)/100
    grand_total = total + tax
    if request.method == "POST":
        
        form = OrderForm(request.POST)

        if form.is_valid():
            data = Order()
            
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address = form.cleaned_data['address']
            data.zip_code = form.cleaned_data['zip_code']
            data.county = form.cleaned_data['county']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note'] 

            data.order_total = grand_total
            data.tax = tax

            data.save()
            print("Data saved ==>>",current_user)
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))

            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user = current_user, is_ordered=False, order_number=order_number)

            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total
            }
            return render(request, 'order/payments.html', context)
    else:
        return redirect('checkout')

