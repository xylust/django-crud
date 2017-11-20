from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(decimal_places=0, max_digits=100)

    def __str__(self):
        return self.name