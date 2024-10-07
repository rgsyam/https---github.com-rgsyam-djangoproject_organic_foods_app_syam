from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    CATEGORY_PRODUCTS=[
        ("fruits","Fruits"),
        ("vegetables","Vegetables"),
        ("non-veg","Non-veg"),
    ]
    img=models.ImageField(upload_to='pic',default="")
    product_name=models.CharField(max_length=100)
    description=models.TextField()
    rate= models.CharField( max_length=50)
    category=models.CharField(max_length=100,choices=CATEGORY_PRODUCTS)
    
    def __str__(self):
        return f"Products{self.product_name}"
    
class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(null=True)
    address = models.CharField(max_length=500, null=True)
    mobile = models.CharField(max_length=20, null=True)
    booking_date = models.DateField(auto_now_add=True, null=True)
    order_date = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'Booking for {self.product.product_name} x {self.quantity} on {self.booking_date}'
    
   