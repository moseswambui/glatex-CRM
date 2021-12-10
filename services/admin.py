from django.contrib import admin
from .models import Category,ServiceType,Service

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('service_name',)}
    list_display = ('service_name', 'slug')

class ServiceCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name', 'slug')

class ServiceTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('type_name',)}
    list_display = ('type_name', 'slug')


admin.site.register(Category, ServiceCategoryAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register( ServiceType,ServiceTypeAdmin)