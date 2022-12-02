from django.contrib import admin

from .models import Type, Category,Blog

class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = (
        'author',
        'category',
        'title',
        'image'
    )
    list_editable = ('image',)

admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)