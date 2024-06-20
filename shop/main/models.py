from django.db import models

class Brand(models.Model):
    image = models.ImageField(upload_to='brands/')
    
    def __str__(self):
        return str(self.id)

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.title