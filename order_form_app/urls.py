"""order_form_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ORM import views

urlpatterns = [
    path('', views.render_info, name="index"),
    path('admin/', admin.site.urls, name="admin"),
    path('createcustomer/', views.create_customer, name="createcustomer"),
    path('createorderdetails/', views.create_order_details,
         name='createorderdetails'),
    path('createorder/', views.create_order, name="createorder"),
    path('createaddress/', views.create_address, name="createaddress")
]
