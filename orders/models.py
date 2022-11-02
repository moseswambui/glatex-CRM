
from email.policy import default
from random import choices
from tabnanny import verbose
from django.db import models

from django.conf import settings

from accounts.models import Account
from customerportal.models import Product, Variation

from base import fields as custom_fields

class Payment(models.Model):
    user =  models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null = True,
        blank = True,
        on_delete = models.CASCADE,
        
    )

    payment_id = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    amount_paid = models.CharField(max_length=100, null=True, blank=True)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.payment_id

class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    user =  models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null = True,
        blank = True,
        on_delete = models.CASCADE,
        
    )
    payment = models.ForeignKey(
        Payment,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    order_number = models.CharField(max_length=100, null=True, blank=True)
    order_serial = custom_fields.UniqueCodeField(
        verbose_name = 'order_serial',
        max_length = 10,
        prefix="ORD-",
        null = True,
        blank = True,
    )
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    order_note = models.CharField(max_length=100, null=True, blank=True)
    order_total = models.FloatField()
    tax = models.FloatField()
    status = models.CharField(max_length=100, choices=STATUS, default='New')
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def full_address(self):
        return f'{self.address}, {self.zip_code}'

    def full_contact(self):
        return f'{self.phone}, {self.email}'

    def __str__(self):
        return self.first_name

class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    payment = models.ForeignKey(
        Payment,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    variation = models.ForeignKey(
        Variation,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    color = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.FloatField()
    product_price = models.FloatField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name