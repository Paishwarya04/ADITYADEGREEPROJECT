from django.shortcuts import render,redirect
from .forms import *
from .models import *


# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def cus_register(request):
    if request.method=='POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cus_list')
    else:
        form=CustomerForm()
    return render(request,'cus.html',{'form' : form})
 
def cus_list(request):
    customer=Customer.objects.all()
    return render(request,'cus_list.html',{'customer':customer})

