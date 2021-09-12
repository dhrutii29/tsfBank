from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    email = models.EmailField(max_length=254)
    accno = models.BigIntegerField()
    balance = models.IntegerField()

class Transaction(models.Model):
    debited_from = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='sender')
    received_by = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='receiver')
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    transaction_status = models.CharField(max_length=255, default="PENDING")