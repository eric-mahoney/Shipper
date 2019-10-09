from django.contrib import admin

# Register your models here.
from .models import Customer, Address, Order, Order_Details
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Order_Details)