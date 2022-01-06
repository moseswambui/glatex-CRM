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
        return reverse('product_by_type',args=[self.slug])

    def __str__(self):
        return self.type_name

class ProductTag(models.Model):
    name = models.CharField(max_length=50,blank=True,null=True)
    slug = models.CharField(max_length=50, unique=True)

    def get_url(self):
        return reverse('product_by_tag',args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=50, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE,blank=True,null=True)
    slug = models.SlugField(max_length=50,unique=True)
    description = models.TextField(max_length=455,blank=True)
    price = models.IntegerField()
    tag = models.ForeignKey(ProductTag, on_delete=models.CASCADE,blank=True, null=True)
    image = models.ImageField(upload_to ='customerportal/uploaded/products')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_color = models.CharField(max_length=50,blank=True)
    size = models.CharField(max_length=10, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail',args=[ self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

class ProductImages(models.Model):
    tag_identifier = models.CharField(max_length=15,blank=True, null=True)
    product_image = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to ='customerportal/uploaded/products')

    def __str__(self):
        return self.tag_identifier

class VariationManager(models.Manager):
    def color(self):
        return super(VariationManager, self).filter(variation_category='color')
    def size(self):
        return super(VariationManager, self).filter(variation_category='size')

    def service(self):
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

    def __str__(self):
        return self.variation_category


class ServiceCategory(models.Model):
    category_name = models.CharField(max_length=50,blank=True, null=True, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'servicecategory'
        verbose_name_plural='servicecategories'

    def get_url(self):
        return reverse('service_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name

class ServiceType(models.Model):
    type_name = models.CharField(max_length=50,blank=True, null=True, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name = 'Service Type'
        verbose_name_plural='Service Types'

    def get_url(self):
        return reverse('product_by_category',args=[self.slug])

    def __str__(self):
        return self.type_name




class Service(models.Model):
    service_name = models.CharField(max_length=50, blank=True)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE,blank=True,null=True)
    slug = models.SlugField(max_length=50,unique=True)
    description = models.TextField(max_length=500,blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to ='customerportal/uploaded')
    category=models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)
    product_color = models.CharField(max_length=50,blank=True)
    size = models.CharField(max_length=10, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class MyCart(models.Model):
    cart_id=models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    def __str(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    cart = models.ForeignKey(MyCart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
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

class Payment(models.Model):
    name = models.CharField(max_length=30 , null=True,blank=True)
    payment_id = models.CharField(max_length=30 , null=True,blank=True)
    amount_paid =models.CharField(max_length=50, null=True, blank=True)
    payment_method = models.CharField(max_length=30 , null=True,blank=True)
    status = models.CharField(max_length=80,blank=True, null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    email_address = models.EmailField(blank=True, null=True)
    area = models.CharField(max_length=80,blank=True, null=True)
    item = models.CharField(max_length=200,blank=True, null=True)

