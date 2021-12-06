from django.db import models
from django.urls import reverse
from django.db.models.deletion import SET_NULL
from django.db.models.fields import CharField, NullBooleanField
from django.db.models.fields.related import ManyToManyField, OneToOneField

class Category(models.Model):
    category_name = models.CharField(max_length=50,blank=True, null=True, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('product_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name

class ProductType(models.Model):
    type_name = models.CharField(max_length=50,blank=True, null=True, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name = 'Product Type'
        verbose_name_plural='Product Types'

    def get_url(self):
        return reverse('product_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name



class Product(models.Model):
    product_name = models.CharField(max_length=50, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE,blank=True,null=True)
    slug = models.SlugField(max_length=50,unique=True)
    description = models.TextField(max_length=255,blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to ='custmerportal/uploaded')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_color = models.CharField(max_length=50,blank=True)
    size = models.CharField(max_length=10, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail',args=[ self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color')

class VariationManager(models.Manager):
    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size')

class VariationManager(models.Manager):
    def services(self):
        return super(VariationManager, self).filter(variation_category='service')

variation_category_choice=(
    ('color','color'),
    ('size','size'),
    ('service','service')
)
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __unicode__(self):
        return self.product


class MyCart(models.Model):
    cart_id=models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    def __str(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(MyCart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product

class ContactUs(models.Model):
    name = models.CharField(max_length=30 , null=True,blank=True)
    phone = models.CharField(max_length=30 , null=True,blank=True)
    email =models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=80,blank=True, null=True)
    message =models.TextField(null=True, blank=True)

class Order(models.Model):
    product_name = models.CharField(max_length=30, null=True, blank=True)
    first_name =models.CharField(max_length=34, null=True, blank=True)

