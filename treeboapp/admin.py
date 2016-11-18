from django.contrib import admin

# Register your models here.
from .models import Product, UserSubscription

admin.site.register(Product)
admin.site.register(UserSubscription)