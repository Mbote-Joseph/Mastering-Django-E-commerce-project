from django.contrib import admin

from store.models import Address, Cart, CartItem, Collection, Customer, Order, OrderItem, Product, Promotion

# Register your models here.

admin.site.register(Promotion)
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(CartItem)