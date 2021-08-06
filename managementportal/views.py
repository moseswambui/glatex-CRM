from typing import Container
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import *
from .models import *
from django.db.models import Avg,Sum

def GlatexPortal(request):
    return render(request, "glatexportal.html")

def Index(request):
    employees = GlatexEmployee.objects.all()
    context = {'employees':employees}
    return render(request,"admin_index.html",context)

def Employees(request):
    employees = GlatexEmployee.objects.all()
    print(employees)
    return render(request,"admin_employee.html")

def AdminSales(request):
    sales = DailySales.objects.filter(Sales_Department='Printing')
    total_largeformat = DailySales.objects.filter(Sales_Department='Printing').aggregate(Sum("Sales_Amount"))
    
    sales_screenprinting = DailySales.objects.filter(Sales_Department='T_shirt_Printing')
    total_screenprinting = DailySales.objects.filter(Sales_Department='T_shirt_Printing').aggregate(Sum("Sales_Amount"))
    context ={'sales':sales,'total_largeformat':total_largeformat,'sales_screenprinting':sales_screenprinting,'total_screenprinting':total_screenprinting}
    return render(request, 'admin_sales.html',context)

def AdminExpenses(request):
    expense = DailyExpenses.objects.all()
    total_expense = DailyExpenses.objects.all().aggregate(Sum('Expense_Cost'))
    context ={'expense':expense,'total_expense':total_expense}
    return render(request, 'admin_expenses.html',context)

def AdminBreakages(request):
    misbehaviours = Misbehaviour.objects.all()
    context ={'misbehaviours':misbehaviours}
    return render(request, 'admin_breakages.html',context)
def Advert(request):
    return render(request,"admin_advert.html")

def Clients(request):
    
    return render(request,"admin_clients.html")

def AdminInvoices(request):
    invoice = Invoice.objects.all()
    print(invoice)
    context ={'invoice':invoice}
    return render(request,"admin_invoices.html",context)

def Inventory(request):
    digital = DigitalPrintingInv.objects.all()
    largeformat = LargeFormatPrinting.objects.all()
    accessory =Accessory.objects.all()
    brandingitems =BrandingItem.objects.all()
    
    context = {'largeformat':largeformat,'accessory':accessory,'brandingitems':brandingitems,'digital':digital}
    return render(request,"admin_inventory.html",context)

def Meeting(request):
    return render(request,"admin_meeting.html")

def Messages(request):
    return render(request,"admin_message.html")

def EmployeeDashboard(request):
    return render(request,"employee_index.html")

def DigitalPrinting(request):
    form=WebPostsForm()
    if request.method =='POST':
        form =WebPostsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,"employee_digitalprinting.html",context)

def JobStats(request):
    return render(request,"employee_jobstats.html")

def LargeFormat(request):
    form=WebPostsForm()
    if request.method =='POST':
        form =WebPostsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,"employee_largeformat.html",context)

def EmployeeProfile(request):
    return render(request,"employee_profile.html")


def ScreenPrinting(request):
    form=WebPostsForm()
    if request.method =='POST':
        form =WebPostsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,"employee_screenprinting.html",context)

def RegisterEmployee(request):
    form=AddEmployeeProfileForm()
    if request.method =='POST':
        form =AddEmployeeProfileForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,"employee_register.html",context)

def LargeFormatInventory(request):
    form=LargeFormatInventoryForm()
    if request.method =='POST':
        form =LargeFormatInventoryForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,"employee_largeformat_inventory.html",context)

def VinylInventory(request):
    form=PlotterMaterialForm()
    if request.method =='POST':
        form =PlotterMaterialForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,"employee_vinyl_inventory.html",context)

def DigitalPrintingInventory(request):
    form=DigitalPrintingInventoryForm()
    if request.method =='POST':
        form =DigitalPrintingInventoryForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,"employee_digitalprinting_inventory.html",context)

def ScreenPrintingInventory(request):
    form=BrandingItemsInventoryForm()
    if request.method =='POST':
        form =BrandingItemsInventoryForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,"employee_screenprinting_inventory.html",context)

def AccessoryInventory(request):
    form=AccessoryInventoryForm()
    if request.method =='POST':
        form =AccessoryInventoryForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,"employee_accessory_inventory.html",context)

def EmployeeTask(request):
    return render(request,"employee_tasks.html")

def EmployeeMisbehaviour(request):
    return render(request,"employee_misbehaviour.html")

def EmployeeBreakages(request):
    return render(request,"employee_breakages.html")

def Sales(request):
    form=SalesForm()
    if request.method =='POST':
        form =SalesForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}

    sales = DailySales.objects.all()
    total = DailySales.objects.all().aggregate(Sum('Sales_Amount'))
    context = {'form':form,'sales':sales,'total':total}

    return render(request,"employee_sales.html",context)

def Invoices(request):
    form=InvoiceForm()
    if request.method =='POST':
        form =InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,"employee_invoices.html",context)

def Expenses(request):
    form=DailyExpensesForm()
    if request.method =='POST':
        form =DailyExpensesForm(request.POST)
        if form.is_valid():
            form.save()
    expenses = DailyExpenses.objects.all()
    total_expenses = DailyExpenses.objects.all().aggregate(Sum('Expense_Cost'))
    context = {'form':form,'expenses':expenses,'total_expenses':total_expenses}
    return render(request,"employee_expenses.html",context)

def ClientRegister(request):
    form=ClientRegistrationForm()
    if request.method =='POST':
        form =ClientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'client_register.html',context)

def RegisterAdmin(request):
    form=AdminForm()
    if request.method =='POST':
        form =AdminForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'admin_admin.html',context)

def RegisterOffice(request):
    
    return render(request, 'admin_office.html')

def RegisterUser(request):
    form = CrreateUserForm()
    if request.method == 'POST':
        form = CrreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'employee_registration.html',context)