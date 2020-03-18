from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=40)
    quantity = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.quantity
