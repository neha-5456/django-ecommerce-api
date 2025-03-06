from rest_framework import serializers
from .models import Cart, CartItem
from Product.serializers import ProductVariationSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product_variation = ProductVariationSerializer(read_only=True)
    subtotal = serializers.ReadOnlyField()

    class Meta:
        model = CartItem
        fields = ['id', 'product_variation', 'quantity', 'subtotal']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']
