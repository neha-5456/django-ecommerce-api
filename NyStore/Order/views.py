from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print("Received data:", request.data)  # Debug
        print("Authenticated User:", request.user)  # Debug

        serializer = self.get_serializer(data=request.data, context={'request': request})  # Pass request context

        if not serializer.is_valid():
            print("Serializer errors:", serializer.errors)  # Debug errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

