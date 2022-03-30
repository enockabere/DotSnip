from django.db import models
from cloudinary.models import CloudinaryField
from authentication .models import MyUser

# Create your models here.

class Catalogue(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.title)
        
class Product(models.Model):
    STATUS = [
        ('Available','Available'),
        ('Sold','Sold'),
    ]
    image = CloudinaryField('image',blank=True)
    price = models.IntegerField(blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(choices=STATUS,max_length=255, blank=True)
    category = models.ForeignKey(Catalogue, on_delete=models.CASCADE,related_name="entries")
    
    def __str__(self):
        return str(self.title)
    
class Cart(models.Model):
    user = models.CharField(max_length=200)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="pros")
    quantity = models.IntegerField(blank=True)
    unit_price = models.IntegerField(blank=True)
    total = models.IntegerField(blank=True)
    
    def __str__(self):
        return str(self.product)
    

