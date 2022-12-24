from django.db import models
from accounts.models import Account
from django.urls import reverse
class Type(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    slug = models.CharField(max_length=50, unique=True,null=True, blank=True)
    type = models.ForeignKey(Type, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('blog_by_category',args=[self.slug])
class Blog(models.Model):
    author=models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    slug = models.CharField(max_length=50, unique=True,null=True, blank=True)
    type = models.ForeignKey(Type, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    blog = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_blog_url(self):
        return reverse('blog_detail',args=[ self.category.slug, self.slug])

    def get_blog_mgt(self):
        return reverse('blogdetail',args=[ self.category.slug, self.slug])

    def get_blog_category(self):
        return reverse('blog_detail',args=[ self.category.slug, self.slug])

class BlogCommentary(models.Model):
    blog = models.ForeignKey(Blog, blank=True, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(Account, null=True, blank=True, on_delete=models.PROTECT)
    title = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    commentary = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title

class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE)
    comment = models.TextField( null=True, blank=True) 
    rating = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

class Reply(models.Model):
    pass
