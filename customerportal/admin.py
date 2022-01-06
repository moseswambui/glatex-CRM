from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ('product_name', 'slug')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name', 'slug')

class ProductTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('type_name',)}
    list_display = ('type_name', 'slug')

class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('service_name',)}
    list_display = ('service_name', 'slug')

class ServiceCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name', 'slug')

class ServiceTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('type_name',)}
    list_display = ('type_name', 'slug')

class ProductTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'slug')

class VavirationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value')
class MyCartAdmin(admin.ModelAdmin):
    list_display = ('cart_id','date_added')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product','cart','quantity')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register( ServiceType,ServiceTypeAdmin)
admin.site.register(MyCart,MyCartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Variation,VavirationAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(ProductTag, ProductTagAdmin)
admin.site.register(ProductImages)
admin.site.register(Payment)