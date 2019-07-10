from django.db import models
import datetime

# Create your models here.


class Product(models.Model):  # class inherits all from class model
    name = models.CharField(
        max_length=255,  # name with datatype and a maximum length of 255 chars
        blank=True  # allows field to be empty
    )
    price = models.FloatField(
        blank=True
    )
    url = models.CharField(
        max_length=2083
    )
    date = models.DateTimeField()
