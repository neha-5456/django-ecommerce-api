from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ProductVariationViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'variation', ProductVariationViewSet, basename='variation')

urlpatterns = [
    path('', include(router.urls)),  # Include all ViewSet routes
]