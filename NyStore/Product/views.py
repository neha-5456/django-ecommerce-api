from django.shortcuts import render
from .serializers import ProductCategoryReadSerializer , ProductReadSerializer ,ProductVariationSerializer
from .models import Product , ProductCategory, ProductVariation
from rest_framework import permissions, viewsets
from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer
    # permission_classes = [permissions.AllowAny]
    permission_classes = [IsAdminOrReadOnly] 
 
class ProductVariationViewSet(viewsets.ModelViewSet):
    # queryset = ProductVariation.objects.all()
    serializer_class = ProductVariationSerializer
    permission_classes = [IsAdminOrReadOnly] 
    def get_queryset(self):
        product_id = self.request.query_params.get('product_id')
        if product_id:
            return ProductVariation.objects.filter(product_id=product_id)
        return ProductVariation.objects.all()
    @action(detail=True, methods=['get'])
    def variations(self, request, pk=None):
        variations = ProductVariation.objects.filter(product_id=pk)
        serializer = self.get_serializer(variations, many=True)
        return Response(serializer.data)
        
    
    
        
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryReadSerializer
    permission_classes = [IsAdminOrReadOnly]   