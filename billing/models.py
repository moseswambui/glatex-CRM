
from django.db import models
from customerportal.models import CartItem

class DeliveryDetails(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.name

PAYMENT_STATUS = (
    ("PAID", "Paid"),
    ("NOT PAID", "Not Paid")
)

class Order(models.Model):
    STATUS_PENDING, STATUS_PAID,STATUS_PARTIAL  = ("PENDING", "PAID", "PARTIAL")
    cart = models.ForeignKey(
        CartItem,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    delivery_details = models.ForeignKey(
        DeliveryDetails,
        blank=True, 
        null=True,
        on_delete=models.CASCADE
    )
    payment_status = models.CharField(
        max_length=50,
        choices=((STATUS_PAID, STATUS_PAID),(STATUS_PENDING, STATUS_PENDING), (STATUS_PARTIAL,STATUS_PARTIAL)),
        default=  STATUS_PENDING,
    )

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")


    def __str__(self):
        return str(self.delivery_details)


class Payment(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    order = models.ForeignKey(
        Order,
        blank=True, 
        null=True,
        on_delete=models.CASCADE
    )

    amount = models.IntegerField(null=True, blank=True)
    paid_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Payment")
        verbose_name_plural =("Payments")

    def __str__(self):
        return str(self.order)

class Delivery(models.Model):
    order = models.ForeignKey(
        Order,
        blank=True, 
        null=True,
        on_delete=models.CASCADE
    )
    delivery_status = models.BooleanField(default="")
