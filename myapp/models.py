from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Product(models.Model):
    def __str__(self):
        return self.name #return name of product instead of product1 product2
    
    def get_absolute_url(self):
        return reverse('myapp:products')
    seller_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to='images')
    
class OrderDetail(models.Model):
    customer_username = models.CharField(max_length=200)
    product = models.ForeignKey(to='Product',on_delete=models.PROTECT)
    amount = models.IntegerField()
    stripe_payment_intent =  models.CharField(max_length=200)
    has_paid = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)