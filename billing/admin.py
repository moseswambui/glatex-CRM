from django.contrib import admin
from .models import *
from customerportal.models import CartItem

class DeliveryAdminInline(admin.TabularInline):
    model = DeliveryDetails
    field = ("email", 'name', 'address')

class CartAdminInline(admin.TabularInline):
    model =  CartItem
    fields = ('product','cart',)

class PaymentInlines(admin.TabularInline):
    model = Payment
    fields = ('created_at', 'amount',)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ("cart", 'delivery_details', 'payment_status')
    inlines = [PaymentInlines]


class DeliveryDetailsAdmin(admin.ModelAdmin):
    model = DeliveryDetails
    list_display = ("email", 'name', 'address')

class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ('order', 'paid_at','amount')

admin.site.register(Order, OrderAdmin)
admin.site.register(DeliveryDetails, DeliveryDetailsAdmin)
admin.site.register(Payment, PaymentAdmin)