from django.contrib import admin
from .models import Category, Link, Item
from ckeditor.widgets import CKEditorWidget
from django import forms

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
    exclude = ['added_by',]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'added_by', None) is None:
            obj.added_by = request.user
            obj.active = True
        super(LinkAdmin, self).save_model(request, obj, form, change)


class ItemAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), required=False)
    class Meta:
        model = Item
        fields = '__all__'


class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminForm
    exclude = ['about_photo', 'about_title', 'about_version', 'about_sub_title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Item, ItemAdmin)
