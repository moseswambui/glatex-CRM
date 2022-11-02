from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Type(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

class Blog(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    type = models.ForeignKey(Type, null=True, blank=True, on_delete=models.CASCADE)
    blog = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Comment(models.Model):
    pass

class Reply(models.Model):
    pass
