from django.contrib import admin

from .models import Type, Category,Blog

class BlogAdmin(admin.ModelAdmin):
    model = Blog
    prepopulated_fields = {'slug':('title',)}
    list_display = (
        'author',
        'category',
        'title',
        'image',
        'slug',
    )
    list_editable = ('image','slug')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'slug')
    list_editable = ('slug',)

admin.site.register(Type)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog, BlogAdmin)