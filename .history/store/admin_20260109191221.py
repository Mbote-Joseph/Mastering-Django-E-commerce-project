from django.contrib import admin

from store.models import Address, Cart, CartItem, Collection, Customer, Order, OrderItem, Product, Promotion
from store.admin import AddressAdmin

# Register your models here.
class PromotionAdmin(admin.ModelAdmin):
    class Meta:
        fields = ('description', 'discount')
        
        
class AddressAdmin(admin.ModelAdmin):
    class Meta:
        fields = ('street', 'city', 'zip', 'customer')

admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address, AddressAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)