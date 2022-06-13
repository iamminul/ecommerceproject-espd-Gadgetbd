from django.db import models
from django.contrib.auth.models import User
from home.models import Product
import random, string




#custom id generate

def random_string_generator(size=20, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars)for _ in range(size))


class Cart(models.Model):
    cart_id = models.CharField(max_length=100, blank=True)
    total_cart_items = models.PositiveIntegerField(default=0)
    total_price = models.FloatField(default=0)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = 'Cart'


    #save method
    def save(self,*args,**kwargs):
        #if no cart_id isn't passed while creating an order.
        if not len(self.cart_id):
            self.cart_id = random_string_generator()
        super(Cart,self).save(*args,**kwargs)

class CartItem(models.Model):
    cartItem_id = models.CharField(max_length=100, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cartItem_quantity = models.PositiveBigIntegerField(default=0)
    cartItem_price = models.FloatField(default=0)

    class Meta():
        verbose_name_plural = 'Cart Item'


    def save(self,*args,**kwargs):
        #if no cart_id isn't passed while creating an order.
        if not len(self.cartItem_id):
            self.cartItem_id = random_string_generator()


        self.cartItem_price = self.cartItem_quantity * self.product.prod_price
        super(CartItem, self).save(*args, **kwargs)