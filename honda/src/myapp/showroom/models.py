from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class staff(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    pan=models.CharField(max_length=10)
    adhaar=models.CharField(max_length=12,unique=True)
    id=models.IntegerField(primary_key=True)
    phone=models.CharField(max_length=20)

class vehicle(models.Model):
    V_CHOICES=(
        ('2', 'Two-wheeler'),
        ('4', 'Four-wheeler'),
    )
    vtype=models.CharField(max_length=20, choices=V_CHOICES)
    tempno=models.IntegerField(primary_key=True)
    company=models.CharField(max_length=20)

class stock(models.Model):
    stock=models.IntegerField()
    #vno=models.IntegerField()
    stockid=models.IntegerField(primary_key=True)
    VehicleNum=models.ForeignKey(vehicle,null=True, on_delete=None)

class booking_by_staff(models.Model):
    bookingid=models.IntegerField(primary_key=True)
    stockid=models.ForeignKey(stock,on_delete=None)
    staffid=models.ForeignKey(staff,on_delete=None)

class customer(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    pan=models.CharField(max_length=10)
    adhaar=models.CharField(max_length=12,unique=True)
    id=models.IntegerField(primary_key=True)
    phone=models.IntegerField()

class booking_by_customer(models.Model):
    custid=models.IntegerField(primary_key=True)
    stockid=models.ForeignKey(stock,on_delete=None)
    staffid=models.ForeignKey(staff,on_delete=None)

# class booking_by_admin(models.Model):
#     bookingid=models.IntegerField(primary_key=True)
#     stockid=models.ForeignKey(stock,on_delete=None)
#     adminid=models.ForeignKey(staff,on_delete=None)