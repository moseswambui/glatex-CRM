from django.db import models
from django.urls import reverse

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

class ServiceType(models.Model):
    type_name = models.CharField(max_length=50,blank=True, null=True, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name = 'Service Type'
        verbose_name_plural='Service Types'

    def get_url(self):
        return reverse('product_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name




class Service(models.Model):
    service_name = models.CharField(max_length=50, blank=True)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE,blank=True,null=True)
    slug = models.SlugField(max_length=50,unique=True)
    description = models.TextField(max_length=255,blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to ='customerportal/uploaded')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_color = models.CharField(max_length=50,blank=True)
    size = models.CharField(max_length=10, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

