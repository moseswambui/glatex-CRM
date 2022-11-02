from django.db.models.signals import post_delete, post_save,pre_save
from django.dispatch import receiver

from billing.models import Order, Payment

@receiver(pre_save, sender=Payment)
def update_order_status(sender, instance, using, **kwargs):
    if instance:
        order = instance.order
        order.payment_status = Payment.STATUS_PAID
        order.save()