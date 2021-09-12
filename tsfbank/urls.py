from django.urls import path
from . import views

urlpatterns = [
    path('customer_details/<str:pk>/',views.customer_details, name='customer_details'),
    path('transactions.html/', views.transactions, name="transactions"),
    path('transfer.html/', views.transfer, name='transfer'),
    path('customers.html/', views.customers, name="customers"),
    path('', views.index, name="index")
]
