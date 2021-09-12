from django.contrib import admin
from .models import Customers, Transaction

# Register your models here.

admin.site.register(Customers)
admin.site.register(Transaction)