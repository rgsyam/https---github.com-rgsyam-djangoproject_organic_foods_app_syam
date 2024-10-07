from django.db import models

# Create your models here.

#Special_Offers

class Special_Offers(models.Model):
    CATEGORY_CHOICES=[
        ('all offers','All Offer'),
        ('fruits','Fruits'),
        ('vegatables','Vegatables'),
    ]
    
    title=models.CharField(max_length=253)
    image=models.ImageField(upload_to="pic", default="")
    description=models.TextField()
    rate=models.CharField(max_length=100)
    category=models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    
    
    def __str__(self):
        return self . title
    
    #Subscription
    
class Subscription(models.Model):
    email=models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self . email
    
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=300)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self . name
    
        
    
        
        
        
    
    
    
        
    
