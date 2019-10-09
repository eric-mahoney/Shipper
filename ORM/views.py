from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from ORM.models import Customer, Order, Order_Details, Address
from . import forms

# Create your views here.


def render_info(request):
    # return HttpResponse('info')

    db = []

    def get_data():
        customers = Customer.objects.all()
        for customer in customers:
            user = {
                'customer_id': customer.id,
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                'addresses': [],
                'orders': []
            }

            addresses = Address.objects.filter(Customer=customer.id)

            if(len(addresses) > 0):
                for address in addresses:
                    item = {
                        'street': address.street,
                        'city': address.city,
                        'state': address.state,
                        'zipcode': address.zipcode
                    }
                    user['addresses'].append(item)

            orders = Order.objects.filter(Customer=customer.id)

            if(len(orders) > 0):
                for order in orders:
                    item = {
                        'order_number': order.order_number,
                        'payment_method': order.payment_method,
                        'acct_number': order.payment_acct_number,
                        'security_code': order.payment_acct_security_code,
                        'order_total': order.order_total,
                        'date': order.created_date
                    }
                    try:
                        order_details = Order_Details.objects.filter(
                            order=order)
                        order_detail_list = []
                        for single_order in order_details:
                            order_dict = {}
                            order_dict['product_name'] = single_order.product_name
                            order_dict['quantity'] = single_order.quantity
                            order_detail_list.append(order_dict)
                        item['order_details'] = order_detail_list
                    except:
                        item['product_name'] = "click 'create order details' to add order id: {}".format(
                            order.order_number)
                        item['quantity'] = "click 'create order details' to add order id: {}".format(
                            order.order_number)

                    user['orders'].append(item)

            db.append(user)

    get_data()
    return render(request, 'index.html', {'db': db})


def create_customer(request):
    form = forms.CustomerForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'index.html')
    else:
        form = forms.CustomerForm()
    return render(request, 'createcustomer.html', {'form': form})


def create_address(request):
    form = forms.AddressForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'index.html')
    else:
        form = forms.AddressForm()
    return render(request, 'createaddress.html', {'form': form})


def create_order_details(request):
    form = forms.OrderDetailsForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'index.html')
    else:
        form = forms.OrderDetailsForm()
    return render(request, 'createorderdetails.html', {'form': form})


def create_order(request):
    form = forms.OrderForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'index.html')
    else:
        form = forms.OrderForm()
    return render(request, 'createorder.html', {'form': form})
