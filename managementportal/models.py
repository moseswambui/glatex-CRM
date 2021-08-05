from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import NullBooleanField
from django.db.models.fields.related import ManyToManyField, OneToOneField
from django.utils import tree


DEPARTMENTS = [
    ("DESIGN",'Design'),
    ("T_shirt_Printing",'Tshirt_Printing'),
    ('FABRICATION','Fabrication'),
    ("RECEPTION",'Reception'),
    ("PRINTING",'Printing'),
]
EMPLOYEE_STATUS=[
    ("ACTIVE","Active"),
    ("DISCONTINUED","Discontinued"),
]
class GlatexAdmin(models.Model):
    First_Name = models.CharField(max_length=30,null=True, blank=True)
    Surname_Name = models.CharField(max_length=30,null=True, blank=True)
    
    Email_Address = models.EmailField(null=True, blank=True)
    Admin_Phone =models.CharField(max_length=13,blank=True,null=True)
    Admin_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.First_Name

    
    

class GlatexOffice(models.Model):
    Office_Id = models.CharField(primary_key=True,max_length=20)
    Office_Location=models.CharField(max_length=20,blank=True, null=True)
    Office_Admin =models.ForeignKey(GlatexAdmin,on_delete=SET_NULL,blank=True,null=True)
    Office_Cell =models.CharField(max_length=13,blank=True,null=True)
    Office_Email= models.EmailField(blank=True, null=True)
    def __str__(self):
        return self.Office_Location

class GlatexManager(models.Model):
    First_Name = models.CharField(max_length=30,null=True, blank=True)
    Surname_Name = models.CharField(max_length=30,null=True, blank=True)
    Manager_Id=models.CharField(primary_key=True,max_length=12)
    Manager_Email_Address = models.EmailField(null=True, blank=True)
    Manager_Phone =models.CharField(max_length=13,blank=True,null=True)
    Manager_Salary=models.CharField(max_length=5, blank=True, null=True)
    Manager_Office=models.ForeignKey(GlatexOffice,on_delete=models.CASCADE)
    def __str__(self):
        return self.First_Name


class GlatexEmployee(models.Model):

    First_Name = models.CharField(max_length=30,null=True, blank=True)
    Surname_Name = models.CharField(max_length=30,null=True, blank=True)
    
    Employee_Email_Address = models.EmailField(null=True, blank=True)
    Employee_Phone=models.CharField(max_length=13,blank=True,null=True)
    Employee_Department=models.CharField(max_length=30,choices=DEPARTMENTS,null=True,blank=True)
    Employee_Salary= models.CharField(max_length=5,null=True, blank=True)
    Employee_Office = models.ForeignKey(GlatexOffice,on_delete=SET_NULL,blank=True, null=True)
    
    Nhif_Number =models.CharField(max_length=10,default="None")
    Employee_Status = models.CharField(max_length=20,choices=EMPLOYEE_STATUS, null=True)

    def __str__(self):
        return self.First_Name

class GlatexMeeting(models.Model):
    Office_Id = models.ForeignKey(GlatexOffice,on_delete=SET_NULL,null=True,blank=True)
    Meeting_Location =models.CharField(max_length=25, null=True, blank=True)
    Meeting_Date = models.DateField(null=True, blank=True)
    Meeting_Purpose =models.CharField(max_length=50, blank=True, null=True)

class MeetingMinutes(models.Model):
    Meeting_Id = models.ForeignKey(GlatexMeeting, on_delete=SET_NULL, blank=True, null=True)
    Meeting_Minute = models.TextField(null=True, blank=True)
    
class MeetingMembers(models.Model):
    meeting=models.OneToOneField(GlatexMeeting, on_delete=models.CASCADE,null=True)
    members = models.ManyToManyField(GlatexEmployee, blank=True)

CLIENTDESIGNATION = [
    ("BROKER", 'Broker'),
    ("REGULAR", "Regular")
]
class Client(models.Model):
    First_Name = models.CharField(max_length=45, null=True,blank=True)
    Last_Name = models.CharField(max_length=45, null=True,blank=True)
    Client_Phone = models.CharField(max_length=45, null=True,blank=True)
    Client_Email = models.EmailField( null=True,blank=True)
    Client_Location = models.CharField(max_length=45, null=True,blank=True)
    
    Client_Designation= models.CharField(max_length=10,choices=CLIENTDESIGNATION,null=True,blank=True)
LARGEFORMATMATERIAL=[
    ('BANNER', 'Banner'),
    ('STICKER', 'Sticker'),
    ("WINDOWGRAPHICS",'Window Graphics'),
    ('CLEARSTICKER','Clear Sticker'),
    ('REFLECTIVESTICKER', 'Reflective Sticker'),
    ('BACKLIT','Backlit')
]

class Invoice(models.Model):
    Client_Name = models.CharField(max_length=45, null=True, blank=True)
    Delivery_Number = models.CharField(max_length=20,null=True, blank=True)
    Invoice_Total = models.IntegerField(null=True, blank=True)
    Invoice_Date = models.DateField(null=True, blank=True)
    invoice_number = models.CharField(max_length=10,blank=True, null=True)

class InvoiceDetails(models.Model):
    Particular_Name = models.CharField(max_length=20,null=True, blank=True)
    Particular_Size= models.CharField(max_length=10,null=True, blank=True)
    Particular_Amount=models.IntegerField(null=True,blank=True)
    Particular_Invoice = models.ForeignKey(Invoice,on_delete=SET_NULL, blank=True,null=True)

PAYMENTMETHOD = [
    ('MPESA','M-pesa'),
    ('CASH','Cash')
]
class DailySales(models.Model):
    Client = models.CharField(max_length=45, null=True, blank=True)
    Client_id = models.CharField(max_length=45, null=True, blank=True)
    Sales_Product = models.CharField(max_length=34,null=True,blank=True)
    Sales_Quantity = models.CharField(max_length=34,null=True,blank=True)
    Sales_Amount = models.IntegerField(null=True, blank=True)
    Sales_Date =models.DateField(null=True, blank=True)
    Sales_Department = models.CharField(max_length=34,null=True,blank=True, choices=DEPARTMENTS)
    Payment_Method = models.CharField(max_length=20,blank=True, null=True,choices=PAYMENTMETHOD)

class SalesDetails(models.Model):
    Item_Name = models.CharField(max_length=56,null=True, blank=True)
    Item_Size =models.CharField(max_length=10,null=True, blank=True)
    sale = models.ForeignKey(DailySales,on_delete=models.CASCADE, null=True,blank=True)

class DesignTasks(models.Model):
    Employees = models.ForeignKey(GlatexEmployee, on_delete=SET_NULL, null=True,blank=True)
    Task_Name = models.CharField(max_length=25, null=True, blank=True)
    Task_Amount = models.IntegerField(null=True, blank=True)
    Payment_Status =models.CharField(max_length=20,blank=True, null=True)
    Print_Status =models.CharField(max_length=25, null=True)
    Design_Size =models.CharField(max_length=25, null=True)
    Task_Date = models.DateField(null=True)

class FabricationTask(models.Model):
    Employees = models.ManyToManyField(GlatexEmployee,blank=True)
    Task_Name = models.CharField(max_length=25, null=True, blank=True)
    Task_Amount = models.IntegerField(null=True, blank=True)
    Payment_Status =models.CharField(max_length=20,blank=True, null=True)
    Task_Location = models.CharField(max_length=30,null=True)
    Task_Date = models.DateField(null=True)

class DailyExpenses(models.Model):
    Employee = models.ForeignKey(GlatexEmployee, on_delete=SET_NULL, null=True)
    Employee_Name = models.CharField(max_length=56, null=True , blank=True)
    Item_Name =models.CharField(max_length=50,null=True,blank=True)
    Expense_Cost = models.IntegerField(null=True, blank=True)
    Expense_Date=models.DateField(null=True, blank=True)

MISBEHAVIOURS = [
    ('LATENETESS', 'Lateness'),
    ('Rudeness', 'Rudeness'),
    ('UNNCESARY DELAYS', 'Unnecessary Delays')
]
class Misbehaviour(models.Model):
    Misbehaviour_Nature =models.CharField(max_length=50,null=True,choices=MISBEHAVIOURS)
    Employee =models.ForeignKey(GlatexEmployee, on_delete=SET_NULL,null=True)
    Misbehaviour_Date = models.DateField(null=True)
POSTCATEGORY=[
    ('LARGEFORMAT', "Large Format"),
    ('SCREENPRINTING','Screen Printing'),
    ('DIGITALPRINTING', 'Digital Printing')
]
class WebPost(models.Model):
    Post_Title = models.CharField(max_length=50, null=True, blank=True)
    Post_Category=models.CharField(max_length=20,null=True, choices=POSTCATEGORY)
    Post_Description = models.CharField(max_length=50, null=True, blank=True)
    Post_Cost = models.IntegerField(null=True, blank=True)
    Post_Image = models.ImageField(null=True)
    Employee = models.ForeignKey(GlatexEmployee, blank=True,null=True, on_delete=SET_NULL)

LARGEFORMATMATERIAL=[
    ('BANNER', 'Banner'),
    ('STICKER', 'Sticker'),
    ("WINDOWGRAPHICS",'Window Graphics'),
    ('CLEARSTICKER','Clear Sticker'),
    ('REFLECTIVESTICKER', 'Reflective Sticker'),
]
class LargeFormatPrinting(models.Model):
    Material_Name=models.CharField(max_length=20,choices=LARGEFORMATMATERIAL, null=True, blank=True)
    Item_size = models.CharField(null=True,max_length=4, blank=True)
    Item_Quantity= models.IntegerField(null=True,blank=True)
    Item_Cost = models.IntegerField(null=True, blank=True)
    Item_Date_In = models.DateField(null=True, blank=True)
    Dealer_Phone = models.CharField(max_length=15, blank=True,null=True)
    Dealer_Name = models.CharField(max_length=15, blank=True,null=True)
    Manufacturer_Name=models.CharField(max_length=30,blank=True, null=True)
    
PLOTTERMATERIAL=[
    ('VINYL','Vinyl'),
    ('MANILLA', 'Manilla'),
]
COLORS =[
    ('RED','Red'),
    ('WHITE','White'),
    ('YELLOW','Yellow'),
    ('BLACK',"Black")
]
class PlotterMaterial(models.Model):
    Material_Name =models.CharField(max_length=20,choices=PLOTTERMATERIAL,null=True,blank=True)
    Item_Quantity = models.IntegerField(blank=True, null=True)
    Item_Color = models.CharField(max_length=20,choices=COLORS,null=True,blank=True)
    Item_Cost =models.IntegerField( blank=True, null=True)
    Dealer_Phone = models.CharField(max_length=15, blank=True,null=True)
    Dealer_Name = models.CharField(max_length=15, blank=True,null=True)
    Item_Date_In = models.DateField(null=True, blank=True)


PAPERTYPE=[
    ('PHOTOCOPY','Photocopy Rim'),
    ('GLOSSY','Glossy Rim'),
    ('TICTAC','TicTac'),
    ('PHOTOPAPER','PhotoPaper rim'),
    ('IVORY','Ivory'),
    ('PLAINPAPER','Plain Paper'),
    ('PHOTOPAPER','Photo Paper'),
    ('SUBLIMATION', 'Sublimation'),
    ('EMBOSED','Embossed'),
]
PAPERSIZE=[
    ('A4',"A4"),
    ('A3','A3'),
]
class DigitalPrintingInv(models.Model):
    Paper_Name=models.CharField(max_length=50,choices=PAPERTYPE, null=True, blank=True)
    Quantity =models.IntegerField(null=True, blank=True)
    Paper_Cost =models.IntegerField(null=True, blank=True)
    Paper_Size = models.CharField(max_length=5,choices=PAPERSIZE, null=True,blank=True)
    Item_Date_In = models.DateField(null=True, blank=True)
    Dealer_Phone = models.CharField(max_length=15, blank=True,null=True)
    Dealer_Name = models.CharField(max_length=15, blank=True,null=True)

BRANDINGITEMS=[
    ('TSHIRTS','Tshirt'),
    ("Cap",'Cap'),
    ('HOODIES','Hoodies'),
    ('SHIRT','Shirt'),
    ('MUG','Mug'),
    ('REFLECTOR','Reflector'),
    ("OTHER",'Other'),
]
SIZES=[
    ("S",'S'),
    ("M",'M'),
    ('L','L'),
    ("XL",'XL'),
    ("XXL",'XXL'),
    ("XXXL",'XXXL'),
]

class BrandingItem(models.Model):
    Branding_Item = models.CharField(max_length=10,choices=BRANDINGITEMS, null=True,blank=True)
    Size = models.CharField(max_length=10,choices=SIZES, null=True,blank=True)
    Item_Quantity = models.IntegerField(null=True,blank=True)
    Item_Color = models.CharField(max_length=20,choices=COLORS,null=True,blank=True)
    Item_Cost = models.IntegerField(blank=True,null=True)
    Item_Type =models.CharField(max_length=20,null=True,blank=True)
    Item_Date_In = models.DateField(null=True, blank=True)
    Dealer_Phone = models.CharField(max_length=15, blank=True,null=True)
    Dealer_Name = models.CharField(max_length=15, blank=True,null=True)

ACCESSORIES=[
    ('ALUMINIUM','Aluminium'),
    ("BROADBASE STAND",'Broadbase Stand'),
    ('BULB','Bulb'),
    ('NAMETAGS','Name Tags')
]
class Accessory(models.Model):
    Accessory_Name=models.CharField(max_length=25,choices=ACCESSORIES,blank=True, null=True)
    Accessory_Quantity = models.IntegerField(null=True,blank=True)
    Accessory_Cost = models.IntegerField(blank=True, null=True)
    Item_Date_In = models.DateField(null=True, blank=True)
    Dealer_Phone = models.CharField(max_length=15, blank=True,null=True)
    Dealer_Name = models.CharField(max_length=15, blank=True,null=True)
INKPRINTERS =[
    ('LARGEFORMAT', 'Large Format'),
    ('DIGITALPRINTER','Digital Printer')

]
class PrintInk(models.Model):
    Ink_Name =models.CharField(max_length=25,null=True, blank=True)
    Ink_Size = models.CharField(max_length=3, null=True, blank=True)
    Ink_Gadget = models.CharField(max_length=30,null=True, blank=True,choices=INKPRINTERS)
    Ink_Color =models.CharField(max_length=20,null=True, blank=True)
    Ink_Quantity = models.IntegerField(blank=True,null=True)
    Ink_Cost = models.IntegerField(null=True, blank=True)
    Ink_Date_In = models.DateField(null=True, blank=True)
    Dealer_Phone = models.CharField(max_length=15, blank=True,null=True)
    Dealer_Name = models.CharField(max_length=15, blank=True,null=True)

CONTRACTS = [
    ('LARGEFORMAT','Large Format'),
    ('Electricity','Electrician')
]
class GlatexContractor(models.Model):
    Phone_Number = models.CharField(max_length=16,null=True, blank=True)
    Contractor_Responsibilities =models.CharField(max_length=30,null=True, blank=True,choices=CONTRACTS)
    Contractor_bio = models.CharField(max_length=60,null=True, blank=True)

class PromotionalItem(models.Model):
    Item_Name = models.CharField(max_length=45, null=True, blank=True)
    Item_Discount =models.IntegerField(null=True, blank=True)
    Item_cost =models.IntegerField(null=True, blank=True)
    item_description = models.TextField(null=True, blank=True)
    Item_banner_photo = models.ImageField(null=True,blank=True)




class Ad(models.Model):
    Company_Name = models.CharField(max_length=45, null=True, blank=True)
    Company_Location =models.CharField(max_length=45, null=True)
    Ad_Description = models.TextField(null=True, blank=True)
    Ad_Charges = models.IntegerField(null=True,blank=True)
    Ad_Image = models.ImageField(null=True, blank=True)

class PendingJob(models.Model):
    client_name = models.CharField(max_length=50, null=True,blank=True)
    client_phone =models.CharField(max_length=19, null=True, blank=True)
    job_description = models.TextField(max_length=56, null=True, blank=True)
    date_in = models.DateField(null=True, blank=True)
    fullfilment_date = models.DateField(null=True, blank=True)

class ParcelDelivery(models.Model):
    item_name = models.CharField(max_length=40,null=True, blank=True)
    receiver_name = models.CharField(max_length=40,null=True, blank=True)
    delivery_location =models.CharField(max_length=40, null=True, blank=True)
    delivery_phone = models.CharField(max_length=20, null=True, blank=True)
    send_date = models.DateField(null=True, blank=True)
    sender = models.OneToOneField(GlatexEmployee,on_delete=models.SET_NULL, null=True, blank=True)
    number_plate = models.CharField(max_length=10,null=True, blank=True)
    driver_cell = models.CharField(max_length=20,null=True, blank=True)





