from django.db import models

# Create your models here.


class Product(models.model):  # class inherits all from class model
    name = models.CharField(max_length=255)  # name with datatype and a maximum length of 255 chars
    price = models.FloatField()
    url = models.Charfield()