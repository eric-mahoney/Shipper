from .models import Customer, Order, Address, Order_Details
from django import forms


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name',
                  'cell_phone', 'home_phone', 'e_mail')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'id': 'firstname',
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'id': 'lastname',
                'class': 'form-control'}),
            'cell_phone': forms.NumberInput(attrs={
                'placeholder': 'Cell Phone',
                'id': 'cellphone',
                'class': 'form-control'
            }),
            'home_phone': forms.NumberInput(attrs={
                'placeholder': 'Home Phone',
                'id': 'homephone',
                'class': 'form-control'
            }),
            'e_mail': forms.EmailInput(attrs={
                'placeholder': 'E-mail',
                'id': 'email',
                'class': "form-control"
            })
        }


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('Customer', 'street', 'city', 'state', 'zipcode')
        widgets = {
            'Customer': forms.Select(attrs={
                'placeholder': 'Customer',
                'id': 'customer',
                'class': 'form-control'
            }),
            'street': forms.TextInput(attrs={
                'placeholder': 'Street',
                'id': 'street',
                'class': 'form-control'}),
            'city': forms.TextInput(attrs={
                'placeholder': 'City',
                'id': 'city',
                'class': 'form-control'
            }),
            'state': forms.TextInput(attrs={
                'placeholder': 'State',
                'id': 'state',
                'class': 'form-control'
            }),
            'zipcode': forms.NumberInput(attrs={
                'placeholder': 'Zipcode',
                'id': 'zipcode',
                'class': "form-control"
            })
        }


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('order_number', 'Customer', 'payment_method',
                  'payment_acct_number', 'payment_acct_security_code', 'order_total')
        widgets = {
            'Customer': forms.Select(attrs={
                'placeholder': 'Customer',
                'id': 'customer',
                'class': 'form-control'
            }),
            'payment_method': forms.TextInput(attrs={
                'placeholder': 'Payment Method',
                'id': 'payment_method',
                'class': 'form-control'}),
            'payment_acct_number': forms.NumberInput(attrs={
                'placeholder': 'Payment Account Number',
                'id': 'payment_acct_number',
                'class': 'form-control'
            }),
            'payment_acct_security_code': forms.NumberInput(attrs={
                'placeholder': 'Security Code',
                'id': 'payment_acct_security_code',
                'class': 'form-control'
            }),
            'order_total': forms.NumberInput(attrs={
                'placeholder': 'Order Total',
                'id': 'order_total',
                'class': "form-control"
            })
        }


class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = Order_Details
        fields = ('order', 'product_name', 'quantity')
        widgets = {
            'order': forms.Select(attrs={
                'placeholder': 'Order',
                'id': 'order',
                'class': 'form-control'
            }),
            'product_name': forms.TextInput(attrs={
                'placeholder': 'Product Name',
                'id': 'product_name',
                'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={
                'placeholder': 'Quantity',
                'id': 'quantity',
                'class': 'form-control'
            })
        }
