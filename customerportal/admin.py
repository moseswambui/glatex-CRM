from django.contrib import admin
from .models import *
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.html import format_html, urlencode
# Register your models here.
class ProductTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'slug')

class ProductTypeModelAdmin(admin.TabularInline):
    model = ProductType
    fields = ('type_name', "slug",)

class ProductTypesAdminInline(admin.TabularInline):
    model = ProductType
    list_display = ("name", 'category',)
class CategoryModelAdmin(admin.TabularInline):
    model = Category
    
    fields = ('category', "description",)

class TagModelAdmin(admin.TabularInline):
    model = ProductTag
    fields = ('name', "slug",)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'slug')
    inlines = [ProductTypesAdminInline]

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != "":
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" />')

        return ""

class VariationAdminInlines(admin.TabularInline):
    model = Variation
    list_display = ('product', 'variation_category', 'variation_value',)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    inlines = [ProductImagesInline, VariationAdminInlines]
    list_display = (
        'name',
        'type',
        'tag',
        'category',
        'price'
        )
    search_fields = (
        "name",
        "type",
        "category",
    )

    list_filter = (
        'type',
        'category',
        'tag',
        'size',
    )

    readonly_fields = (
        "created_date",
       
        
    )

    class Media:
        css = {
            "all":['products/styles.css']
        }

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
    list_per_page = 10



class CartItemAdmin(admin.ModelAdmin):
    model = CartItem
    list_display = ('product','cart','quantity', 'sub_total')
    list_per_page = 10

        



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