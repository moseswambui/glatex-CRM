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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(MyCart)
admin.site.register(CartItem)
admin.site.register(Variation)
admin.site.register(ProductType, ProductTypeAdmin)