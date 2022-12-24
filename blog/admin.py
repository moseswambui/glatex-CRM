from django.contrib import admin

from .models import Type, Category,Blog,BlogCommentary,BlogComment

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

class BlogCommentAdmin(admin.ModelAdmin):
    model = BlogComment
    list_display = ('blog','user', 'comment', 'rating', 'created_at')
class BlogCommentaryAdmin(admin.ModelAdmin):
    model = BlogCommentary
    list_display = ('title', 'commentary','author', 'blog')
admin.site.register(Type)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(BlogCommentary,BlogCommentaryAdmin)