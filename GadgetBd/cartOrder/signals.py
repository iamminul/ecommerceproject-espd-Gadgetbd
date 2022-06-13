from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *



@receiver(post_save, sender= CartItem)
def update_cart(sender,**kwargs):
    print('Cart Update signal is called')
    print('Cart Item Instance',kwargs['instance'])
    cartItemInstance = kwargs['instance']
    print('Cart Item ID:',cartItemInstance.cartItem_id)

    cartID = cartItemInstance.cart.cart_id
    cartItem_quantity = cartItemInstance.cartItem_quantity
    cartItem_price = cartItemInstance.cartItem_price

    print('Cart Item Quantity:', cartItem_quantity)
    print('Cart Item Price:', cartItem_price)

    cart = Cart.objects.get(cart_id=cartID)

    cart.total_price += cartItem_price
    cart.total_cart_items += cartItem_quantity
    cart.save()

    print('Actual Cart:',cart)




