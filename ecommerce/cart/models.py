from django.db import models

# Create your models here.
from shop.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    date_added=models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.product.price*self.quantity


class Order_details(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_item=models.IntegerField()
    address=models.TextField()
    phoneno=models.BigIntegerField()
    pin=models.IntegerField()

    order_id=models.CharField(blank=True,max_length=30)
    order_date=models.DateTimeField(auto_now_add=True)

    payment_status=models.CharField(default="pending",max_length=30)
    delivery_status=models.CharField(default="pending",max_length=30)


class Payment(models.Model):
    name=models.CharField(max_length=100)
    amount=models.IntegerField()
    order_id=models.CharField(max_length=30,blank=True)
    razorpay_payment_id=models.CharField(max_length=30,blank=True)
    paid=models.BooleanField(default=False)