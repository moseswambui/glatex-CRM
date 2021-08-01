from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import CharField, NullBooleanField
from django.db.models.fields.related import ManyToManyField, OneToOneField

class ContactUs(models.Model):
    name = models.CharField(max_length=30 , null=True,blank=True)
    phone = models.CharField(max_length=30 , null=True,blank=True)
    email =models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=80,blank=True, null=True)
    message =models.TextField(null=True, blank=True)

class Order(models.Model):
    product_name = models.CharField(max_length=30, null=True, blank=True)
    first_name =models.CharField(max_length=34, null=True, blank=True)

