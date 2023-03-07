from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models import *
from app1.forms import CustomerForm
from django.contrib import messages

def create_cust_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Saved Successfully..!")
    context = {'form': CustomerForm()}
    return render(request, 'customer_form.html', context)


def show_customer(request):
    customers = Customer.objects.all()
    context = {'customers':customers}
    return render(request, 'show_customer.html', context)


def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    messages.info(request, "Data Deleted successfully..!", extra_tags='alert-danger')
    return redirect('show_customer')

def update_customer(request, pk):
    if request.method == 'POST':
        # print(request.POST)
        cust = Customer.objects.get(id=pk)
        form = CustomerForm(data=request.POST, instance=cust)
        if form.is_valid:
            form.save()
            return redirect('show_customer')
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    return render(request, 'customer_form.html', {'form':form})
    


