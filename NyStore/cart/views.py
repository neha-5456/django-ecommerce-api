from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from Product.models import ProductVariation
from .serializers import CartSerializer, CartItemSerializer

class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

class AddToCartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # print(request.data.get('product_variation'))
        cart, created = Cart.objects.get_or_create(user=request.user)
        variation_id = request.data.get('product_variation')
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        try:
            variation = ProductVariation.objects.get(id=variation_id)
        except ProductVariation.DoesNotExist:
            return Response({"error": "Product variation not found"}, status=status.HTTP_404_NOT_FOUND)

        cart_item, created = CartItem.objects.get_or_create(cart=cart,product_id = product_id , product_variation=variation)
        cart_item.quantity += int(quantity)
        cart_item.save()

        return Response({"message": "Product variation added to cart"}, status=status.HTTP_201_CREATED)

class RemoveFromCartView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        variation_id = kwargs.get('variation_id')
        cart_item = CartItem.objects.filter(cart=cart, product_variation_id=variation_id).first()

        if cart_item:
            cart_item.delete()
            return Response({"message": "Item removed from cart"}, status=status.HTTP_200_OK)

        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
