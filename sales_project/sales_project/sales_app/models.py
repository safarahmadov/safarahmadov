from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class sales(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    image=models.ImageField(upload_to="product_image/")
    
    
def __str__(self):
        return f"{self.name} by {self.brand} ({self.size}, {self.color}"
    
class Payment(models.Model):
    name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('Product', through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)