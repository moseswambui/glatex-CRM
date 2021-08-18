from collections import UserList
from typing import Container
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.shortcuts import redirect,render
from django.db.models import Avg,Sum
from django.contrib.auth import authenticate,login, logout
from .decorators import *
from django.contrib.auth.models import Group

@UnoutheticatedUser
def GlatexPortal(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('employeedashboard')

        else:
            messages.success(request,'Error logging in: Please try again')
            return render(request, "glatexportal.html") 
      
    return render(request, "glatexportal.html")

def LogoutEmployee(request):
    logout(request)
    messages.success(request,('Logged out Successfully'))
    return redirect('glatex')

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
    total_largeformat = DailySales.objects.all()
    
    sales_screenprinting = DailySales.objects.all()
    total_screenprinting = DailySales.objects.all().aggregate(Sum("Sales_Amount"))
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
    saleinventory = SalesAccessoryInventory.objects.all()
    context = {'saleinventory':saleinventory}
    return render(request,"admin_message.html",context)

def EmployeeDashboard(request):
    my_groups=Group.objects.filter(user=request.user)
    
    
    context={'my_groups':my_groups}
    messages.success(request, 'logged in successfully')
    return render(request,"employee_index.html",context)

def DigitalPrinting(request):
    form=WebPostsForm()
    if request.method =='POST':
        form =WebPostsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,"employee_digitalprinting.html",context)

def JobStats(request):
    sales =  DailySales.objects.all().aggregate(Sum('Sales_Amount'))
    expenses = DailyExpenses.objects.all().aggregate(Sum('Expense_Cost'))
    exp = expenses.values()
    sal=sales.values()
    
    
    context ={'sales':sales,'expenses':expenses}
    return render(request,"employee_jobstats.html",context)

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

    employees = User.objects.all()
    context = {'form':form,'employees':employees}
    return render(request,"employee_register.html",context)

def LargeFormatInventory(request):
    form=LargeFormatInventoryForm()
    if request.method =='POST':
        form =LargeFormatInventoryForm(request.POST)
        if form.is_valid():
            form.save()

    largeformat = LargeFormatPrinting.objects.all()
    context = {'form':form,'largeformat':largeformat}
    return render(request,"employee_largeformat_inventory.html",context)

def LargeFormatUpdate(request,pk):
    largeformat=LargeFormatPrinting.objects.get(id=pk)
    form=LargeFormatInventoryForm(instance=largeformat)
    if request.method=='POST':
        form=LargeFormatInventoryForm(request.POST, instance=largeformat)
        if form.is_valid():
            form.save()
            return redirect('sales_inventory')

    context={'form':form}
    return render(request, 'employee_largeformat_inventory_update.html',context)

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

    accessories = Accessory.objects.all()
    context = {'form':form,'accessories':accessories}
    return render(request,"employee_accessory_inventory.html",context)

def AccessoryInventoryUpdate(request,pk):
    accessory=Accessory.objects.get(id=pk)
    form=AccessoryInventoryForm(instance=accessory)
    if request.method=='POST':
        form=AccessoryInventoryForm(request.POST, instance=accessory)
        if form.is_valid():
            form.save()
            return redirect('sales_inventory')

    context={'form':form}
    return render(request, 'employee_accessory_inventory_update.html',context)

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
    digital_sales = DailySales.objects.all()
    sales = DailySales.objects.all()
    print(sales)
    total = DailySales.objects.all().aggregate(Sum('Sales_Amount'))
    context = {'form':form,'sales':sales,'total':total}

    return render(request,"employee_sales.html",context)

def SalesDigital(request):
    form=SalesDigitalForm()
    if request.method == 'POST':
        form = SalesDigitalForm(request.POST)
        if form.is_valid():
            form.save()
    digital_sales = DailySalesDigital.objects.all()
    total_digital= DailySalesDigital.objects.all().aggregate(Sum('Sales_Amount'))
    context = {'form':form,'digital_sales':digital_sales,'total_digital':total_digital}
    return render(request, 'employee_sales_digital.html',context)
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
    employees= User.objects.all()
    context = {'form':form,'employees':employees}
    return render(request, 'employee_registration.html',context)

def SalesInventory(request):
    form=SalesInventoryForm()
    if request.method =='POST':
        form =SalesInventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employeedashboard')
            
    saleinv = SalesAccessoryInventory.objects.all()
    context = {'form':form,'saleinv':saleinv}
    
    return render(request,'employee_sales_inventory.html',context)

def ScreenPrintingSales(request):
    form=ScreenprintingSalesForm()
    if request.method =='POST':
        form =ScreenprintingSalesForm(request.POST)
        if form.is_valid():
            form.save()
    screensales = ScreenprintingSales.objects.all() 
    total_sales = ScreenprintingSales.objects.all().aggregate(Sum('Amount_Paid'))
  
    context ={'form':form,'screensales':screensales,'total_sales':total_sales}
    return render(request, 'employee_sales_screenprinting.html',context)

def ScreenPrintingExpenses(request):
    form=ScreenprintingExpensesForm()
    if request.method =='POST':
        form =ScreenprintingExpensesForm(request.POST)
        if form.is_valid():
            form.save()
    screenexpenses = ScreenprintingExpenses.objects.all() 
    total_expense = ScreenprintingExpenses.objects.all().aggregate(Sum('Expense_Cost'))
     
    context ={'form':form,'screenexpenses':screenexpenses,'total_expense':total_expense}
    return render(request, 'employee_expenses_screenprinting.html',context)

def ScreenPrintingInvoices(request):
    form=ScreenprintingInvoiceForm()
    if request.method =='POST':
        form =ScreenprintingInvoiceForm(request.POST)
        if form.is_valid():
            form.save()
    screeninvoice =Screenprintinginvoice.objects.all()
    invoice_total = Screenprintinginvoice.objects.all().aggregate(Sum('Invoice_Total'))

    context ={'form':form,'screeninvoices':screeninvoice,'invoice_total':invoice_total}
    return render(request, 'employee_invoices_screenprinting.html',context)

def MovieExpenses(request):
    form = MovieExpenseForm()
    if request.method == 'POST':
        form = MovieExpenseForm(request.POST)
        if form.is_valid():
            form.save()
    movieexpense = Movieexpenses.objects.all()
    total_expense = Movieexpenses.objects.all().aggregate(Sum('Expense_Cost'))
    context ={'form':form,'movieexpense':movieexpense,'total_expense':total_expense}
    return render(request, 'employee_expenses_movies.html',context)

def Moviesales(request):
    form=MovieSalesForm()
    if request.method =='POST':
        form = MovieSalesForm(request.POST)
        if form.is_valid():
            form.save()
    moviesales = MovieSales.objects.all()
    total_sales = MovieSales.objects.all().aggregate(Sum('Amount'))
    context = {'form':form,'moviesales':moviesales,'total_sales':total_sales}
    return render(request,'employee_sales_movie.html',context)