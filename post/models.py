from django.db import models

# Create your models here.

class Catalogue(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.title)
    
class CustomerEntry(models.Model):
    entry = models.ForeignKey(Catalogue, on_delete=models.CASCADE,related_name="entries")
    def __str__(self):
        return str(self.entry)
    
class Product(models.Model):
    CATEGORY_OPTIONS = [
        ('Product','Product'),
        ('Service','Service'),
        ('Other','Other'),
    ]
    category = models.CharField(choices=CATEGORY_OPTIONS,max_length=255, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    comment = models.TextField()
    
    def __str__(self):
        return str(self.category)
    

