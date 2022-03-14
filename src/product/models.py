from django.db import models

# Create your models here.

# Product model. Product: name, weight, price, created_at, updated_at

class Product(models.Model):
    name            = models.CharField(max_length=50)
    weight          = models.SmallIntegerField()
    price           = models.IntegerField()
    created_at      = models.DateField(auto_now=False, auto_now_add=True)
    updated_at      = models.DateField(auto_now=True, auto_now_add=False)