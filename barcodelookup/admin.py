from django.contrib import admin
from .models import Product
# Register your models here.

# register Product database for admin panel
admin.site.register(Product)