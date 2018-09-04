from django.contrib import admin
from .models import Category, Link
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'created', 'modified']
    search_fields = ['name']
    list_filter = ['created', 'modified']


class LinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'category', 'active', 'added_by']
    search_fields = ['name', 'link', 'details']
    autocomplete_fields = ['category']
    list_filter = ['category', 'created', 'modified', 'added_by', 'active']
    exclude = ('added_by')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'added_by', None) is None:
            obj.added_by = request.user
            obj.active = True
        super(LinkAdmin, self).save_model(request, obj, form, change)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Link, LinkAdmin)
