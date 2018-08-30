from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='groups/')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Link(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=300)
    link = models.URLField(max_length=500)
    details = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='links/', null=True, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name