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
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'unit_price', 'inventory','inventory_status', 'collection', )
    list_editable = ['unit_price',]
    product = Product.objects.all()
    list_per_page = 10
    
    
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 150:
            return f"Low"
        else:
            return f"OK"
        
    def counted_inventory(self, product):
        return product.inventory
    
    # def inventory_variance(self, product):
    #     return product.inventory - self.counted_inventory
        
        
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_display', 'placed_at','payment_status', 'customer']
    list_editable = ['payment_status']
    
    order = Order.objects.all()
    
    def order_display(self, order):
        return f"StoreFront-{order.id}"
    
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured_product', 'products_count']
    
    def products_count(self, collection):
        return collection.products_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )

admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Address, AddressAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)