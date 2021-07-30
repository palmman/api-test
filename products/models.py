from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name