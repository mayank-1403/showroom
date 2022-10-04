from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from showroom.forms import BookCustomerModelForm, BookStaffModelForm, CustomerModelForm, StaffModelForm, StockModelForm, VehicleModelForm
from showroom.models import staff, stock, vehicle
from django.contrib import messages

# Create your views here.
def staff_create(request):
    form=StaffModelForm(request.POST or None)
    if form.is_valid():
        obj=form.save()
        obj=StaffModelForm()
        messages.success(request, "Staff added successfully!")
    template_name="staff.html"
    context={"title":"Add new staff", "form":form}
    return render(request, template_name, context)

def vehicle_create(request):
    form=VehicleModelForm(request.POST or None)
    if form.is_valid():
        obj=form.save()
        obj=VehicleModelForm()
        messages.success(request, "Vehicle added successfully!")
    template_name="vehicle.html"
    context={"title":"Add new vehicle", "form":form}
    return render(request, template_name, context)

def customer_create(request):
    form=CustomerModelForm(request.POST or None)
    if form.is_valid():
        obj=form.save()
        obj=CustomerModelForm()
        messages.success(request, "Customer added successfully!")
    template_name="customer.html"
    context={"title":"Add new customer", "form":form}
    return render(request, template_name, context)
    #return redirect("/showroom/book-cust/")

def stock_create(request):
    form=StockModelForm(request.POST or None)
    if form.is_valid():
        obj=form.save()
        obj=StockModelForm()
        messages.success(request, "Stock created successfully!")
    template_name="stock.html"
    context={"title":"Add stock", "form":form}
    return render(request, template_name, context)

def book_cust(request):
    form=BookCustomerModelForm(request.POST or None)
    if form.is_valid():
        obj=form.save()
        obj=BookCustomerModelForm()
        messages.success(request, "Vehicle booked successfully!")
    template_name="book_cust.html"
    context={"title":"Book vehicle by customer", "form":form}
    return render(request, template_name, context)

def book_staff(request):
    form=BookStaffModelForm(request.POST or None)
    if form.is_valid():
        obj=form.save()
        obj=BookStaffModelForm()
        messages.success(request, "Vehicle booked successfully!")
    template_name="book_staff.html"
    context={"title":"Book vehicle by staff", "form":form}
    return render(request, template_name, context)

def view_stock(request):
    qs=stock.objects.all()
    template_name="viewstock.html"
    context={"object_list":qs}
    return render(request, template_name, context)

def view_admin_stock(request):
    qs=stock.objects.all()
    template_name="viewadminstock.html"
    context={"object_list":qs}
    return render(request, template_name, context)


def view_staff(request):
    qs=staff.objects.all()
    template_name="viewstaff.html"
    context={"object_list":qs}
    return render(request, template_name, context)

def update_stock(request, stockid):
    obj=get_object_or_404(stock, stockid=stockid)
    form=StockModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        obj=form.save()
        messages.success(request, "Stock updated successfully!")
    template_name="stockupdate.html"
    context={"form":form}
    return render(request, template_name, context)

def book_admin(request):
    form=VehicleModelForm(request.POST or None)
    if form.is_valid():
        obj=form.save()
        obj=VehicleModelForm()
        messages.success(request, "Vehicle added successfully!")
    template_name="book_admin.html"
    context={"title":"Add vehicle by admin", "form":form}
    return render(request, template_name, context)

def home(request):
    return render(request,'home.html')