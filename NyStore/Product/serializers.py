from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import ProductCategory , Product , ProductVariation

class ProductCategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
        
        
      
class ProductReadSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Product
        fields = "__all__"  
      
class ProductVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariation
        fields = "__all__"       