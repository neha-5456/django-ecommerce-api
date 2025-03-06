from django.contrib import admin
from .models import Product, ProductCategory,ProductVariation
from ckeditor.widgets import CKEditorWidget
from django.db import models
from .utils import display_image
# Register your models here.

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','show_image' ,'created_at']
    search_fields = ['id']
    def show_image(self, obj):
         return display_image(obj, 'icon')  # Uses the common function

    show_image.short_description = "Profile Picture"
    
admin.site.register(ProductCategory, ProductCategoryAdmin)




class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','show_image', 'price' ,'created_at']
    search_fields = ['id']
    ordering = ['created_at']
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()} , # Apply WYSIWYG editor
        
    }
    
    def show_image(self, obj):
         return display_image(obj, 'image')  # Uses the common function

    show_image.short_description = "Profile Picture"
admin.site.register(Product, ProductAdmin)



class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'variation_name','value', 'price_modifier']
    search_fields = ['id']
    
admin.site.register(ProductVariation , ProductVariationAdmin)    