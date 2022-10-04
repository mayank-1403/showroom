"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import book_admin, book_cust, book_staff, customer_create, home, staff_create, stock_create, update_stock, view_admin_stock, view_staff, view_stock

urlpatterns = [
    path('staff/', staff_create),
    # path('vehicle-reg/', vehicle_create),
    path('customer/', customer_create),
    path('stock/', stock_create),
    path('book-cust/', book_cust),
    path('book-staff/', book_staff),
    path('view-stock/', view_stock),
    path('view-admin-stock/', view_admin_stock),
    path('view-staff/', view_staff),
    path('<int:stockid>/update-stock/', update_stock),
    path('admin/', book_admin),
    path('home/', home),
]
