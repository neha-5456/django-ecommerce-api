from django.urls import include, path
from rest_framework.routers import DefaultRouter

from orders.views import OrderItemViewSet, OrderViewSet

app_name = "orders"

router = DefaultRouter()
router.register(r"orders", OrderViewSet, basename="order")
router.register(r"orders/(?P<order_id>\d+)/items", OrderItemViewSet, basename="order-item")


urlpatterns = [
    path("", include(router.urls)),
]