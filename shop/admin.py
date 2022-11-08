from django.contrib import admin
from shop.models import Product, Payments, Order, OrderItem

admin.site.register(Product)
admin.site.register(Payments)
admin.site.register(Order)
admin.site.register(OrderItem)
