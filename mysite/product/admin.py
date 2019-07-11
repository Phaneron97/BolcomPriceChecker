from django.contrib import admin
from .models import Product  # from models in current folder, import Product (class)

# Register your models here.


# lists name and price in admin product list
class ProductAdmin(admin.ModelAdmin):  # Admin class of class Product, inherits from ModelAdmin (built in)
    list_display = ('name', 'price')  # lists name and price from Product in a tuple


admin.site.register(Product, ProductAdmin)  # manage Product class in admin area
