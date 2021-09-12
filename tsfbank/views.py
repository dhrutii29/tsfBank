from django.shortcuts import render
from .models import Customers, Transaction

# Create your views here.

def index(request):
    return render(request, 'index.html')

def customers(request):
    customer = Customers.objects.all()
    return render(request, 'customers.html', {'customer': customer})

def transfer(request):
    if request.method == 'POST':
        sender_email = request.POST["s_email"]
        receiver_email = request.POST["r_email"]
        amt = request.POST["amount"]
        try:
            sender = Customers.objects.get(email=sender_email)
            receiver = Customers.objects.get(email=receiver_email)
            amt = int(amt)
            if amt <= sender.balance:
                print(sender.balance, receiver.balance)
                sender.balance-=amt
                receiver.balance+=amt
                print(sender.balance, receiver.balance)
                sender.save()
                receiver.save()
                new_txn = Transaction(debited_from=sender, received_by=receiver, amount=amt, transaction_status="SUCCESS")
                new_txn.save()
                return render(request, 'transfer.html', {'message': "Transaction Successful!"})
            else:
                return render(request, 'transfer.html', {'error': "You do not have sufficient balance!"})
        
        except Customers.DoesNotExist:
            return render(request, 'transfer.html', {'error': "This customer does not exists."})
    else: 
        return render(request, 'transfer.html')

def transactions(request):
    transaction = Transaction.objects.all()
    return render(request, 'transactions.html', {'transaction': transaction})

def customer_details(request, pk):
    customer = Customers.objects.get(id = pk)
    context={'customer':customer}
    return render(request, 'customer_details.html', context)