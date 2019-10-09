from django.db import models
from datetime import datetime

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=25, null=False, default='')
    last_name = models.CharField(max_length=25, null=False, default='')
    customer_since = models.DateTimeField(
        auto_now=True, null=False)
    cell_phone = models.CharField(max_length=15, null=False, default='')
    home_phone = models.CharField(max_length=15, null=False, default='')
    e_mail = models.CharField(max_length=25, null=False, default='')
    created_date = models.DateTimeField(auto_now=True, null=False)
    updated_date = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return 'First name: {} \nLast name: {}'.format(self.first_name,
                                                       self.last_name)

    class Meta:
        ordering = ('first_name', )


class Address(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    street = models.CharField(max_length=50, null=False, default='')
    city = models.CharField(max_length=25, null=False, default='')
    state = models.CharField(max_length=20, null=False, default='')
    zipcode = models.CharField(max_length=11, null=False, default='')
    created_date = models.DateTimeField(auto_now=True, null=False)
    updated_date = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return 'Street: {}\nCity: {}\nState: {}\nZip: {}'.format(
            self.street, self.city, self.state, self.zipcode)

    class Meta:
        ordering = ('street', )


class Order(models.Model):
    order_number = models.AutoField(primary_key=True,
                                    max_length=10,
                                    null=False)
    Customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False, default='')
    payment_method = models.CharField(max_length=10, null=False, default='')
    payment_acct_number = models.CharField(
        max_length=20, null=False, default='')
    payment_acct_security_code = models.IntegerField(default='')
    order_total = models.FloatField(max_length=10, default='')
    created_date = models.DateTimeField(auto_now=True, null=False)
    updated_date = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return 'Order ID: {}\nCreated Date: {}'.format(self.order_number,
                                                       self.created_date)

    class Meta:
        ordering = ('Customer', )


class Order_Details(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product_name = models.CharField(max_length=20, null=False, default='')
    quantity = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True, null=False)
    updated_date = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return 'Product: {}\nQuantity: {}'.format(self.product_name,
                                                  self.quantity)

    class Meta:
        ordering = ('order', )
