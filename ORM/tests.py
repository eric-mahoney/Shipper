from django.test import TestCase
from datetime import datetime
from ORM.models import Customer, Address, Order, Order_Details
from nltk.tokenize import RegexpTokenizer


class CustomerTestCase(TestCase):
    def setUp(self):
        eric = Customer.objects.create(first_name='Eric',
                                       last_name='Mahoney',
                                       cell_phone='4342502573',
                                       home_phone='4342502573',
                                       e_mail='emahone5@gmu.edu')

        rakib = Customer.objects.create(first_name='Rakib',
                                        last_name='Ahamed',
                                        cell_phone='4342502573',
                                        home_phone='4342502573',
                                        e_mail='Rahmed123@gmu.edu')
        eric_address = Address.objects.create(customer=eric, street='pinecroft road',
                                              city='danville', state='va', zipcode='24540')
        eric_order = Order.objects.create(payment_method="credit card", payment_acct_number="123456",
                                          payment_acct_security_code=3321, order_total=0)
        eric_order_details = Order_Details.objects.create(
            order=eric_order, product_name='MacBook Pro', quantity=1)

    def test_model_creation(self):
        customer1 = Customer.objects.get(first_name="Eric")
        customer1_address = Address.objects.get(street='pinecroft road')
        customer1_order = Order.objects.get(payment_acct_number="123456")
        customer1_order_details = Order_Details.objects.get(
            product_name="MacBook Pro")
        print(customer1)
        print(customer1_address)
        print(customer1_order)
        print(customer1_order_details)

    def test_model_delete(self):
        Customer.objects.filter(first_name='Eric').delete()
        Address.objects.filter(street='pinecroft road').delete()
        Order.objects.filter(payment_acct_number="123456").delete()
        Order_Details.objects.filter(product_name="MacBook Pro").delete()
        print('\n\ndeleted all entries')

    def test_model_update(self):
        customer = Customer.objects.get(first_name="Eric")
        customer.first_name = 'Bob'
        print('\n\ncustomer updated:')
        print(customer)
        customer_address = Address.objects.get(street='pinecroft road')
        customer_address.street = 'Loop Road'
        print('\n\naddress updated:')
        print(customer_address)
        customer1_order = Order.objects.get(payment_acct_number="123456")
        customer1_order.payment_acct_number = '654321'
        print('\n\ncustomer order updated:')
        print(customer1_order)
        customer1_order_details = Order_Details.objects.get(
            product_name="MacBook Pro")
        customer1_order_details.product_name = '2019 MacBook Pro'
        print('\n\ncustomer order details updated:')
        print(customer1_order_details)
