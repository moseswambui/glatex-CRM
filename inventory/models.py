from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

LARGEFORMATMATERIAL=[
    ('BANNER', 'Banner'),
    ('STICKER', 'Sticker'),
    ("WINDOWGRAPHICS",'Window Graphics'),
    ('CLEARSTICKER','Clear Sticker'),
    ('REFLECTIVESTICKER', 'Reflective Sticker'),
]
class LargeFormatPrinting(models.Model):
    Material_Name=models.CharField(max_length=20,choices=LARGEFORMATMATERIAL, null=True, blank=True)
    Item_size = models.DecimalField(null=True,decimal_places=1,max_digits=5, blank=True)
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
    Item_Qantity = models.IntegerField(blank=True, null=True)
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
    ('OTHERS','Others')
]
PAPERSIZE=[
    ('A4',"A4"),
    ('A3','A3'),
]
class DigitalPrinting(models.Model):
    Paper_Type=models.CharField(max_length=50,choices=PAPERTYPE, null=True, blank=True)
    Quantity =models.IntegerField(null=True, blank=True)
    Paper_Cost =models.IntegerField(null=True, blank=True)
    Paper_Size =models.CharField(max_length=5,choices=PAPERSIZE, null=True,blank=True)
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

class BrandingItem(models.Model):
    Branding_Item = models.CharField(max_length=10,choices=BRANDINGITEMS, null=True,blank=True)
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





    
    
