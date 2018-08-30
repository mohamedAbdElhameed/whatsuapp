from django.contrib import admin
from .models import Category, Link
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'created', 'modified']
    search_fields = ['name']
    list_filter = ['created', 'modified']


class LinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'image', 'category', 'details']
    search_fields = ['name', 'link', 'details']
    autocomplete_fields = ['category']
    list_filter = ['category', 'created', 'modified']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Link, LinkAdmin)
