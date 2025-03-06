from django.contrib import admin
from .models import Product, ProductCategory,ProductVariation
from ckeditor.widgets import CKEditorWidget
from django.db import models

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(ProductVariation)

class ProductAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()}  # Apply WYSIWYG editor
    }

admin.site.register(Product, ProductAdmin)