from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product_name', 'quantity', 'price']



class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)  # Keep items inside order

    class Meta:
        model = Order
        fields = ['id', 'total_price', 'created_at', 'status', 'items']  # REMOVE 'user'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        request = self.context.get('request')  # Get request from serializer context

        if not request or not request.user:
            raise serializers.ValidationError({"error": "User authentication failed."})

        order = Order.objects.create(user=request.user, **validated_data)  # Assign user
        for item in items_data:
            OrderItem.objects.create(order=order, **item)
        return order
