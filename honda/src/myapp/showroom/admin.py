from django.contrib import admin

from .models import staff, vehicle, stock, customer, booking_by_customer, booking_by_staff

# Register your models here.
admin.site.register(staff)
admin.site.register(vehicle)
admin.site.register(customer)
admin.site.register(booking_by_customer)
admin.site.register(stock)
admin.site.register(booking_by_staff)
# admin.site.register(booking_by_admin)