from django.contrib import admin
from .models import Product  # from models in current folder, import Product (class)

# Register your models here.

admin.site.register(Product)  # manage Product class in admin area
