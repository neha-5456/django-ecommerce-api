from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
# Create your models here.
from ckeditor.fields import RichTextField


def category_image_path(instance, filename):
    return  f"product/category/icons/{instance.name}/{filename}"

def product_image_path(instance, filename):
    return  f"product/images/{instance.name}/{filename}"


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    icon =  models.ImageField( upload_to=category_image_path, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it's not set
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    class Meta:
       verbose_name = _("Product Category")
       verbose_name_plural = _("Product Categories")
      
    def __str__(self):
        return self.name   
    
def get_default_product_category():
        return ProductCategory.objects.get_or_create(name="Uncategorized")[0] 
   
class Product(models.Model):
    category = models.ForeignKey(ProductCategory,related_name="product_list",on_delete=models.SET(get_default_product_category),)
    name = models.CharField(max_length=200)
    desc = RichTextField()
    image = models.ImageField(upload_to=product_image_path, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    
    class Meta:
        ordering = ("-created_at",)

    
    def __str__(self):
        return self.name
 
class ProductVariation(models.Model):
    product = models.ForeignKey(Product, related_name="variations", on_delete=models.CASCADE)
    variation_name = models.CharField(max_length=100)  # Example: "Size", "Color"
    value = models.CharField(max_length=100)  # Example: "Red", "Blue", "Large"
    price_modifier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Optional price change

    def __str__(self):
        return f"{self.product.name} - {self.variation_name}: {self.value}"

    