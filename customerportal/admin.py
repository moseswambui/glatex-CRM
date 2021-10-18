from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}


admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(MyCart)
admin.site.register(CartItem)
admin.site.register(Variation)