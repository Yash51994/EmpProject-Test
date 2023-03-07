"""EmpProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include

from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('home/', homepage, name='home'),
    path('show-emp/', show_employee, name='show_emp'),
    path('active-emp/', active_emp, name='active_emp'),
    path('edit-emp/<int:pk>/', edit_emp, name='edit_emp'),
    path('customer-form/', create_cust_view, name='cust_form'),
    path('show-customer/', show_customer, name='show_customer'),
    path('delete-customer/<int:pk>/', delete_customer, name='delete_customer'),
    path('update-customer/<int:pk>/', update_customer, name='update_customer'),

    path('', include('app1.rest_urls')),

    path('__debug__/', include('debug_toolbar.urls')),
]
