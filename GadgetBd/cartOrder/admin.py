from django.contrib import admin
from. models import *






class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id','customer','total_cart_items','total_price']
    list_display_links = ['cart_id']



class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cartItem_id','cart','product','cartItem_quantity','cartItem_price']
    list_display_links = ['cartItem_id']


admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem,CartItemAdmin)


