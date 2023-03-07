from django.contrib import admin
from app1.models import *
# Register your models here.

admin.site.register([Employee, Company, Manager, Product, Customer, Profile])

