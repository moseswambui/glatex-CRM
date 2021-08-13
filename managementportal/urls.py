"""GlatexManagementSoftware URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path("",views.GlatexPortal, name="glatex"),
    path("admindashboard",views.Index, name="index"),
    path("employees/",views.Employees, name="employees"),
    path("advert/",views.Advert, name="advert"),
    path("clients/",views.Clients, name="clients"),
    path("admininvoices/",views.AdminInvoices, name="admininvoices"),
    path("adminsales/",views.AdminSales, name="adminsales"),
    path("adminexpenses/",views.AdminExpenses, name="adminexpenses"),
    path("adminbreakages/",views.AdminBreakages, name="adminbreakages"),
    path("inventory/",views.Inventory, name="inventory"),
    path("meeting/",views.Meeting, name="meetings"),
    path("salesinventory/",views.Messages, name="messages"),
    path("addadmin/",views.RegisterAdmin, name="addadmin"),
    path("addoffice/",views.RegisterOffice, name="addoffice"),

    path("employeedashboard",views.EmployeeDashboard, name="employeedashboard"),
    path("digitalprinting/",views.DigitalPrinting, name="digitalprinting"),
    path("jobstats/",views.JobStats, name="jobstats"),
    path("largeformat/",views.LargeFormat, name="largeformat"),
    path("profile/",views.EmployeeProfile, name="employeeprofile"),
    path("screenprinting/",views.ScreenPrinting, name="screenprinting"),
    path("registeremployee/",views.RegisterEmployee, name="registeremployee"),

    path("large-format-inventory/",views.LargeFormatInventory, name="largeformat_inventory"),
    path("largeformat_update/<str:pk>",views.LargeFormatUpdate, name="largeformat_update"),

    path("vinyl-inventory/",views.VinylInventory, name="vinyl_inventory"),
    path("digital-printing-inventory/",views.DigitalPrintingInventory, name="digitalprinting_inventory"),
    path("screen-printing-inventory/",views.ScreenPrintingInventory, name="screenprinting_inventory"),

    path("accessories-inventory/",views.AccessoryInventory, name="accessories_inventory"),
    path("sales-inventory/",views.SalesInventory, name="sales_inventory"),
    path("accessories-update/<str:pk>/",views.AccessoryInventoryUpdate, name="accessories_update"),

    path("Employee-tasks/",views.EmployeeTask, name="employee-tasks"),
    path("employee-misbehaviours/",views.EmployeeMisbehaviour, name="misbehaviours"),
    path("Employee-breakages/",views.EmployeeBreakages, name="breakages"),
    path("sales/",views.Sales, name="sales"),
    path("invoices/",views.Invoices, name="invoices"),
    path("expenses/",views.Expenses, name="expenses"),
    path("register-client/",views.ClientRegister, name="register-client"),
    path("register-user/",views.RegisterUser, name="register-user"),

    


]
