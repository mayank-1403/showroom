import imp
from django import forms
from django.core.exceptions import ValidationError

from .models import  booking_by_customer, booking_by_staff, staff, stock, vehicle, customer

# class staff_form(forms.Form):
#     name=forms.CharField(max_length=20)
#     address=forms.CharField(max_length=20)
#     pan=forms.CharField(max_length=10)
#     adhaar=forms.CharField(max_length=12)
#     id=forms.IntegerField(widget=forms.TextInput)
#     phone=forms.IntegerField(widget=forms.TextInput)

class StaffModelForm(forms.ModelForm):
    class Meta:
        model=staff
        fields=['name','address','pan','adhaar','id','phone']

    def clean_phone(self,*args,**kwargs):
        phone=self.cleaned_data.get('phone')
        qs=staff.objects.filter(phone=phone)
        if qs.exists():
            raise ValidationError("This phone number already exits!")
        return phone

class VehicleModelForm(forms.ModelForm):
    class Meta:
        model=vehicle
        fields=['vtype','tempno','company']

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model=customer
        fields=['name','address','pan','adhaar','id','phone']

class StockModelForm(forms.ModelForm):
    class Meta:
        model=stock
        fields=['stock','stockid','VehicleNum']

class BookStaffModelForm(forms.ModelForm):
    class Meta:
        model=booking_by_staff
        fields=['bookingid','stockid','staffid']

class BookCustomerModelForm(forms.ModelForm):
    class Meta:
        model=booking_by_customer
        fields=['custid','stockid','staffid']

# class BookAdminModelForm(forms.ModelForm):
#     class Meta:
#         model=booking_by_admin
#         fields=['bookingid','stockid','adminid']


