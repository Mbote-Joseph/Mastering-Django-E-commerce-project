from django.contrib import admin

from store.models import Address, Cart, CartItem, Collection, Customer, Order, OrderItem, Product, Promotion

# Register your models here.
class PromotionAdmin(admin.ModelAdmin):
    fields = ('description', 'discount')
        
        
class AddressAdmin(admin.ModelAdmin):
    fields = ('street', 'city', 'zip', 'customer')
    list_display = ('street', 'city', 'zip', 'customer')
        
    def __str__(self):
        return super().__str__()
    
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'birth_date', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 25
        

admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address, AddressAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)