from django.db import models

# Create your models here.
class Product(models.Model):
    """product details for barcode"""

    barcode = models.CharField(max_length=48, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default="")

    def __str__(self):
        return self.name


# class Book(models.Model):
#     product = models.OneToOneField(Product)
