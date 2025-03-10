from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_price','created_at', 'status']
    search_fields = ['id']
    
admin.site.register(Order , OrderAdmin)   

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product_name','quantity', 'price']
    search_fields = ['id']
admin.site.register(OrderItem, OrderItemAdmin)
# Register your models here.
