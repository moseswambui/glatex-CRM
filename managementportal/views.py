from collections import UserList
from typing import Container
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.db.models.expressions import F
from django.forms.forms import Form
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.shortcuts import redirect,render
from django.db.models import Avg,Sum
from django.contrib.auth import authenticate,login, logout
from .decorators import *
from django.contrib.auth.models import Group
import time
import datetime

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
   
    user_profile=request.user.glatexemployee
    
    print(user_profile.Employee_image)
    pic = user_profile.Employee_image
    
    
    context={'user_profile':user_profile,'pic':pic}
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
    
    mpesa_total = DailySales.objects.filter(Payment_Method= "Mpesa").aggregate(Sum('Sales_Amount'))
    mpesa=mpesa_total.get("Sales_Amount__sum")
    
    cash_total =DailySales.objects.filter(Payment_Method= "Cash").aggregate(Sum('Sales_Amount'))
    cash=cash_total.get("Sales_Amount__sum")
    
    cheque_total =DailySales.objects.filter(Payment_Method= "Cheque").aggregate(Sum('Sales_Amount'))
    cheque=cheque_total.get("Sales_Amount__sum")

    large_formattotal = cash+mpesa
    print(large_formattotal)
    

    digital_sales=DailySalesDigital.objects.all().aggregate(Sum('Sales_Amount'))
    digital_amount = digital_sales.get("Sales_Amount__sum")

    expenses = DailyExpenses.objects.all().aggregate(Sum('Expense_Cost'))
    expense_amount = expenses.get('Expense_Cost__sum')

    grand_total = int(digital_amount+ large_formattotal)
    
    profit = int(grand_total) - int(expense_amount)
    percent_profit = (expense_amount/grand_total *100)
    context ={ 'large_formattotal':large_formattotal,'expense_amount':expense_amount,'digital_amount':digital_amount,'grand_total':grand_total,'profit':profit,'percent_profit':percent_profit}
    return render(request,"employee_jobstats.html",context)

def LargeFormat(request):
    form=WebPostsForm()
    if request.method =='POST':
        form =WebPostsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,"employee_largeformat.html",context)




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
    localtime=time.asctime(time.localtime(time.time()))
    form=AccessoryInventoryForm()
    if request.method =='POST':
        form =AccessoryInventoryForm(request.POST)
        if form.is_valid():
            form.save()

    accessories = Accessory.objects.all()
    context = {'form':form,'accessories':accessories,'localtime':localtime}
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

def SalesUpdate(request, pk):
    sale=DailySales.objects.get(id=pk)
    form=SalesForm(instance=sale)
    if request.method == 'POST':
        form=SalesForm(request.POST,instance=sale)
        if form.is_valid():
            form.save()
            return redirect('sales')

    context={'form':form}
    return render(request, 'employee_sales_update.html',context)

def SalesDelete(request,pk):
    sale=DailySales.objects.get(id=pk)
    form=SalesForm(instance=sale)
    if request.method=='POST':
        sale.delete()
        
        
        return redirect('sales')

    context={'sale':sale}
    return render(request,'employee_sales_delete.html',context)

def SalesDigitalDelete(request,pk):
    digital_sale=DailySalesDigital.objects.get(id=pk)
    if request.method=='POST':
        digital_sale.delete()
        return redirect('salesdigital')

    context={'digital_sale':digital_sale}
    return render(request,'employee_sales_digital_delete.html',context)

def SalesDigitalUpdate(request,pk):
    digital_sale=DailySalesDigital.objects.get(id=pk)
    form=SalesDigitalForm(instance=digital_sale)
    if request.method=='POST':
        form=SalesDigitalForm(request.POST,instance=digital_sale)
        if form.is_valid():
            form.save()
            return redirect('salesdigital')

    context={'form':form}

    return render(request,'employee_sales_digital_update.html',context)
    
def ExpensesUpdate(request,pk):
    expense=DailyExpenses.objects.get(id=pk)
    form = DailyExpensesForm(instance=expense)
    if request.method == 'POST':
        form =DailyExpensesForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expenses')
    context = {'form':form}
    return render(request, 'employee_expense_update.html',context)

def ExpensesDelete(request,pk):
    expense=DailyExpenses.objects.get(id=pk)
    if request.method=='POST':
        expense.delete()
        return redirect("expenses")
    context={"expense":expense}
    return render(request, 'employee_expense_delete.html',context) 

def EmployeeTask(request):
    return render(request,"employee_tasks.html")

def EmployeeMisbehaviour(request):
    return render(request,"employee_misbehaviour.html")

def EmployeeBreakages(request):
    return render(request,"employee_breakages.html")

def Sales(request):
    localtime= time.asctime(time.localtime(time.time()))
    print(localtime)
    monday_date= "2021-09-20"
    form=SalesForm()
    if request.method =='POST':
        form =SalesForm(request.POST)
        if form.is_valid():
            form.save()
    digital_sales = DailySales.objects.all()
    sales = DailySales.objects.all()
    
    mpesa_sales = DailySales.objects.filter(Payment_Method= "Mpesa")
    mpesa_total = DailySales.objects.filter(Payment_Method= "Mpesa").aggregate(Sum('Sales_Amount'))
    mpesa=mpesa_total.get("Sales_Amount__sum")

    cash_sales =DailySales.objects.filter(Payment_Method= "Cash")
    cash_total =DailySales.objects.filter(Payment_Method= "Cash").aggregate(Sum('Sales_Amount'))
    cash=cash_total.get("Sales_Amount__sum")

    cheque_sales =DailySales.objects.filter(Payment_Method= "Cheque")
    cheque_total =DailySales.objects.filter(Payment_Method= "Cheque").aggregate(Sum('Sales_Amount'))
    cheque=cheque_total.get("Sales_Amount__sum")
    total=mpesa+cash

    
    context = {'form':form,'mpesa_sales':mpesa_sales, 'cash_sales':cash_sales, 'cheque_sales':cheque_sales,'total':total,'mpesa_total':mpesa_total,'cash_total':cash_total,'cheque_total':cheque_total,'localtime':localtime}
    return render(request,"employee_sales.html",context)

def SalesDigital(request):
    form=SalesDigitalForm()
    if request.method == 'POST':
        form = SalesDigitalForm(request.POST)
        if form.is_valid():
            form.save()
    digital_sales = DailySalesDigital.objects.all()
    total_digital= DailySalesDigital.objects.all().aggregate(Sum('Sales_Amount'))

    mpesa_sales = DailySalesDigital.objects.filter(Payment_Method= "Mpesa")
    mpesa_total = DailySalesDigital.objects.filter(Payment_Method= "Mpesa").aggregate(Sum('Sales_Amount'))

    cash_sales =DailySalesDigital.objects.filter(Payment_Method= "Cash")
    cash_total =DailySalesDigital.objects.filter(Payment_Method= "Cash").aggregate(Sum('Sales_Amount'))

    cheque_sales =DailySalesDigital.objects.filter(Payment_Method= "Cheque")
    cheque_total =DailySalesDigital.objects.filter(Payment_Method= "Cheque").aggregate(Sum('Sales_Amount'))

    total = DailySales.objects.all().aggregate(Sum('Sales_Amount'))

    context = {'form':form,'digital_sales':digital_sales,'cash_sales':cash_sales,'mpesa_sales':mpesa_sales, 'cheque_sales':cheque_sales,'total_digital':total_digital,'mpesa_total':mpesa_total,'cash_total':cash_total,'cheque_total':cheque_total}
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

def DesignTask(request):
    form=DesignTaskForm()
    if request.method=='POST':
        form=DesignTaskForm(request.POST)
        if form.is_valid():
            form.save()

    designtask=DesignTasks.objects.all()
    context={'form':form,'designtask':designtask}
    return render(request, 'employee_designtask.html',context)

def Fabricationtask(request):
    form=FabricationTaskForm()
    if request.method=='POST':
        form=FabricationTaskForm(request.POST)
        if form.is_valid():
            form.save()

    fabtask = FabricationTask.objects.all()
    context={'form':form,'fabtask':fabtask}
    return render(request, 'employee_fabricationtask.html',context)

def TownExpenses(request):
    localtime= time.asctime(time.localtime(time.time()))
    monday_date= "2021-09-20"
    today = datetime.date.today()
    print(today)
    form = TownClothingExpensesForm()
    if request.method =='POST':
        form = TownClothingExpensesForm(request.POST)
        if form.is_valid():
            form.save()

    clothingexpenses = Town_ClothingExpenses.objects.all()
    today_clothes = Town_ClothingExpenses.objects.filter(Purchase_Date=today)
    
    today_total =Town_ClothingExpenses.objects.filter(Purchase_Date=today).aggregate(Sum('Total_Cost'))
    total_cost = Town_ClothingExpenses.objects.all().aggregate(Sum('Total_Cost'))
  
    print(today_total)
    context={'form':form,'clothingexpenses':clothingexpenses,'total_cost':total_cost,"localtime":localtime,"today_clothes":today_clothes,"today_total":today_total}
    return render(request,"employee_townexpenses.html",context)

def Town(request):
    clothingexpenses = Town_ClothingExpenses.objects.all()
    print(clothingexpenses)
    context = {'clothingexpenses':clothingexpenses}
    return render(request, 'employee_town.html',context)
def AllInventory(request):
    inventory = LargeFormatPrinting.objects.all()
    context ={'inventory':inventory}
    return render(request, 'employee_inventory.html',context)

def AllSales(request):
    sales = DailySales.objects.all()
    context = {'sales':sales}
    return render(request, 'employee_allsales.html',context)