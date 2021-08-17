from django.db import models
from django.db.models import fields
from django.db.models.fields import Field
from django.forms import ModelForm, widgets
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class AdminForm(forms.ModelForm):
    class Meta:
        model=GlatexAdmin
        fields = ('First_Name', 'Surname_Name','Email_Address', 'Admin_Phone', 'Admin_image')

        widgets ={
            'First_Name':forms.TextInput(attrs={
                'class':'span8',
                'placeholder':'First Name',
                'id':'basicinput'

            }),
            'Surname_Name':forms.TextInput(attrs={
                'class':'span8',
                'placeholder':'Surname',
                'id':'basicinput'
            }),
            'Email_Address':forms.EmailInput(attrs={
                'class':'span8',
                'placeholder':'Email Address',
                'id':'basicinput'
            }),
            'Admin_Phone':forms.TextInput(attrs={
                'class':'span8',
                'placeholder':'Phone',
                'id':'basicinput'
            }),
           
        }

class CrreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username', 'email', 'password1', 'password2', 'first_name','last_name']

        widgets ={
            'username' : forms.TextInput(attrs={
                'class':'span8',
                'placeholder':'Username',

            }),
            'email': forms.EmailInput(attrs={
                'class':'span8',
                'placeholder':'Email Address',
            }),
            'password1':forms.TextInput(attrs={
                'class':'span8',
                'placeholder':'Id1'
            }),
            'password2':forms.TextInput(attrs={
                'class':'span8',
                'placeholder':'Id1'
            }),
            'first_name':forms.TextInput(attrs={
                'class':'span8',
                'placeholder':'First Name'
            }),
            'last_name':forms.TextInput(attrs={
                'class':'span8',
                'placeholder':'Surname'
            })
            
        }

class LargeFormatInventoryForm(forms.ModelForm):
    class Meta:
        model = LargeFormatPrinting
        fields =['Material_Name','Item_size','Item_Quantity', 'Item_Cost','Item_Date_In', 'Dealer_Phone','Dealer_Name']

        widgets ={
            'Material_Name':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'Material Name'
            }),
            'Item_size':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Material size'
            }),
            'Item_Quantity':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Material Quantity'
            }),
            'Item_Cost':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Cost'
            }),
            'Item_Date_In':forms.DateInput(attrs={
                'class':'form-control',
                'placeholder':'Date In'
            }),
            'Dealer_Phone':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Dealer Phone'
            }),
            'Dealer_Name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Dealer Name'
            }),

            
        }
class AddEmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = GlatexEmployee
        fields =['First_Name','Surname_Name','Employee_Email_Address', 'Employee_Phone','Employee_Department', 'Employee_Salary','Employee_Office', 'Nhif_Number', 'Employee_Status']

        widgets ={
            'First_Name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'First Name'
            }),
            'Surname_Name':forms.TextInput(attrs={
                'class':'form-control',
                
            }),
            'Employee_Email_Address':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Email'
            }),
            'Employee_Phone':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Phone'
            }),
            'Employee_Department':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'Department'
            }),
            'Employee_Salary':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Salary'
            }),
            'Employee_Office':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'Office'
            }),
            
            'Nhif_Number':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nhif No.'
            }),
            'Employee_Status':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'status'
            }),

            
        }

class GlatexMeetingform(forms.ModelForm):
    class Meta:
        model = GlatexMeeting
        fields =['Office_Id','Meeting_Location','Meeting_Date', 'Meeting_Purpose']

        widgets ={
            'Office_Id':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'office'
            }),
            'Meeting_Location':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'location'
                
            }),
            'Meeting_Date':forms.DateInput(attrs={
                'class':'form-control',
                'placeholder':'Date'
            }),
            'Meeting_Purpose':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Purpose'
            }),
            
            
        }

class MeetingMinutesForm(forms.ModelForm):
    class Meta:
        model = MeetingMinutes
        fields =['Meeting_Id','Meeting_Minute']

        widgets ={
            'Meeting_Id':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'Meeting'
            }),
            'Meeting_Minute':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Minutes'
            })
                
         }

class MeetingMembersForm(forms.ModelForm):
    class Meta:
        model = MeetingMembers
        fields =['meeting','members']

        widgets ={
            'meeting':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'Meeting'
            }),
            'members':forms.CheckboxInput(attrs={
                'class':'form-control',
                'placeholder':'Members'
            })
                
         }

class ClientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields =['First_Name','Last_Name','Client_Phone','Client_Email', 'Client_Location','Client_Designation']

        widgets ={
            'First_Name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'first name'
            }),
            'Last_Name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'last name'
            }),
            'Client_Phone':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Phone'
                
            }),
            'Client_Email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'email'
            }),
            'Client_Location':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'location'
            }),
            'Client_Designation':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'designation'
            }),
            
            
        }

    
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields =['Client_Name','Delivery_Number','Invoice_Total', 'Invoice_Date']

        widgets ={
            'Client_Name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'name'
            }),
            'Delivery_Number':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Number'
                
            }),
            'Invoice_Total':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Total'
            }),
            'Invoice_Date':forms.DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':'Date'
            }),
            
            
        }

class InvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetails
        fields =['Particular_Name','Particular_Size','Particular_Invoice']

        widgets ={
            'Particular_Name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'name of item'
            }),
            'Particular_Size':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'size'
                
            }),
            'Particular_Invoice':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'Total'
            }),
            'Invoice_Date':forms.DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':'Date'
            }),
            
            
        }

class SalesForm(forms.ModelForm):
    class Meta:
        model = DailySales
        fields =['Client', 'Sales_Product','Product_Size','Sales_Amount', 'Balance','Sales_Date','Payment_Method']

        widgets ={
            'Client':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Client'
            }),
            
            'Sales_Product':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'product'
                
            }),
            'Product_Size':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Product Size'
                
            }),
            
            'Sales_Quantity':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Quantity'
                
            }),
            'Sales_Amount':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'amount'
                
            }),
            'Balance':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Balance'
                
            }),
            'Sales_Date':forms.DateInput(attrs={
                'class':'form-control',
                'placeholder':'date'
            }),
            
            'Payment_Method':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'payment Method'
            }),
            
            
        }

class SalesDigitalForm(forms.ModelForm):
    class Meta:
        model = DailySalesDigital
        fields =['Client', 'Sales_Product','Product_Size','Sales_Quantity', 'Sales_Amount', 'Balance','Sales_Date','Payment_Method']

        widgets ={
            'Client':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Client'
            }),
            
            'Sales_Product':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'product'
                
            }),
            'Product_Size':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'Product Size'
                
            }),
            
            'Sales_Quantity':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Quantity'
                
            }),
            'Sales_Amount':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'amount'
                
            }),
            'Balance':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Balance'
                
            }),
            'Sales_Date':forms.DateInput(attrs={
                'class':'form-control',
                'placeholder':'date'
            }),
            
            'Payment_Method':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'payment Method'
            }),
            
            
        }


class SalesDetailsForm(forms.ModelForm):
    class Meta:
        model = SalesDetails
        fields =['Item_Name','Item_Size','sale']

        widgets ={
            'Item_Name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'item'
            }),
            'Item_Size':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'size'
                
            }),
            'sale':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'sale'
            }),
           
            
            
        }

class DesignTaskForm(forms.ModelForm):
    class Meta:
        model = DesignTasks
        fields =['Employees','Task_Name','Print_Status', 'Design_Size','Task_Date']

        widgets ={
            'Employees':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'employee'
            }),
            'Task_Name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'name'
                
            }),
            'Print_Status':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Print status'
            }),
            'Design_Size':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'size'
            }),
            'Task_Date':forms.DateInput(attrs={
                'class':'form-control',
                'placeholder':'date'
            }),
            
            
        }

class DailyExpensesForm(forms.ModelForm):
    class Meta:
        model = DailyExpenses
        fields =['Employee_Name','Expense_Description','Expense_Cost', 'Expense_Date']

        widgets ={
            'Employee_Name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'employee'
            }),
            'Expense_Description':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'How the expense was incured'
                
            }),
            'Expense_Cost':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Cost'
            }),
            
            'Expense_Date':forms.DateInput(attrs={
                'class':'form-control',
                'placeholder':'date'
            }),
            
            
        }

class MisbehaviourForm(forms.ModelForm):
    class Meta:
        model = Misbehaviour
        fields =['Misbehaviour_Nature','Employee','Misbehaviour_Date']

        widgets ={
            'Misbehaviour_Nature':forms.Select(attrs={
                'class':'form-control',
                'placeholder':''
            }),
            'Employee':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'employee'
                
            }),
            
            'Misbehaviour_Date':forms.DateInput(attrs={
                'class':'form-control',
                'placeholder':'date'
            }),
            
            
        }

class WebPostsForm(forms.ModelForm):
    class Meta:
        model = WebPost
        fields =['Post_Title','Post_Category','Post_Description', 'Post_Cost','Post_Image']

        widgets ={
            'Post_Title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'title'
            }),
            'Post_Category':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'category'
                
            }),
            'Post_Description':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'description'
            }),
            'Post_Cost':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'cost'
            }),
            'Post_Image':forms.FileInput(attrs={
                'class':'form-control',
                'placeholder':'image'
            }),
            
            
        }

class PlotterMaterialForm(forms.ModelForm):
    class Meta:
        model = PlotterMaterial
        fields =['Material_Name','Item_Quantity','Item_Color', 'Item_Cost','Dealer_Phone','Item_Date_In']

        widgets ={
            'Material_Name':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'material'
            }),
            'Item_Quantity':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Quantity'
                
            }),
            'Item_Color':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'color'
            }),
            'Item_Cost':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'cost'
            }),
            'Dealer_Phone':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'phone'
            }),
            'Item_Date_In':forms.DateInput(attrs={
                'class':'form-control',
                'placeholder':'date'
            }),
            
            
        }
class DigitalPrintingInventoryForm(forms.ModelForm):
    class Meta:
        model = DigitalPrintingInv
        fields =['Paper_Name','Paper_Size','Quantity', 'Paper_Cost','Dealer_Phone','Item_Date_In']

        widgets ={
            'Paper_Name':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'paper type'
            }),
            'Quantity':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Quantity'
                
            }),
            'Paper_Size':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'Size'
                
            }),
            'Paper_Cost':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'cost'
            }),
            'Dealer_Phone':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Phone'
            }),
            
            'Item_Date_In':forms.DateInput(attrs={
                'class':'form-control',
                'placeholder':'date'
            }),
            
            
        }

class BrandingItemsInventoryForm(forms.ModelForm):
    class Meta:
        model = BrandingItem
        fields =['Branding_Item', "Size",'Item_Quantity','Item_Color', 'Item_Cost','Item_Type','Dealer_Phone','Item_Date_In']

        widgets ={
            'Branding_Item':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'material'
            }),
            'Item_Quantity':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Quantity'
                
            }),
            'Size':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'size'
                
            }),
            'Item_Color':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'color'
            }),
            'Item_Cost':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'cost'
            }),
            'Item_Type':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'type'
                
            }),
            'Dealer_Phone':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'phone'
            }),
            'Item_Date_In':forms.DateInput(attrs={
                'class':'form-control',
                'placeholder':'date'
            }),
            
            
        }

class AccessoryInventoryForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields =['Accessory_Name','Accessory_Quantity', 'Accessory_Cost','Dealer_Phone','Item_Date_In']

        widgets ={
            'Accessory_Name':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'Name'
            }),
            'Accessory_Quantity':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Quantity'
                
            }),
            
            'Accessory_Cost':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'cost'
            }),
            'Dealer_Phone':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'phone'
            }),
            'Item_Date_In':forms.DateInput(attrs={
                'class':'form-control',
                'placeholder':'date'
            }),
            
            
        }

class SalesInventoryForm(forms.ModelForm):
    class Meta:
        model = SalesAccessoryInventory
        fields =['Client_Name','Product','Quantity', 'Cost']

        widgets ={
            'Client_Name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Name'
            }),
            'Product':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Product'
                
            }),
            
            'Quantity':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Quantity'
            }),
            'Cost':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'cost'
            }),
            
            
            
        }

class ScreenprintingSalesForm(forms.ModelForm):
    class Meta:
        model = ScreenprintingSales
        fields =['Client','Items','Quantity','Amount_Paid','Balance','Payment_Method']
        widgets ={
            'Client':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Client'
            }),
            'Items':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Item name'
            }),
            'Quantity':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Quantity'
            }),
            'Amount_Paid':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'amount paid'
            }),
            'Balance':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Balance'
            }),
            'Payment_Method':forms.Select(attrs={
                'class':'form-control',
                'placeholder':'Payment method'
            }),
        }

class ScreenprintingInvoiceForm(forms.ModelForm):
    class Meta:
        model = Screenprintinginvoice
        fields=['Client_Name','Product','Invoice_Total']
        widgets ={
            'Client_Name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Client'
            }),
            'Product':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Product'
            }),
            'Invoice_Total':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'invoice Total'
            }),
        }

class ScreenprintingExpensesForm(forms.ModelForm):
    class Meta:
        model = ScreenprintingExpenses
        fields =['Expense_Item','Quantity','Expense_Cost']
        widgets ={
            'Expense_Item':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Item Spent on'
            }),
            'Quantity':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Quantity'
            }),
            
            'Expense_Cost':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'cost'
            }),
            
        }

class MovieSalesForm(forms.ModelForm):
    class Meta:
        model=MovieSales
        fields = ['Amount']
        widgets ={
            'Amount':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Amount in a Day'
            }),
        }

class MovieExpenseForm(forms.ModelForm):
    class Meta:
        model=Movieexpenses
        fields = ['Expense_Item', 'Expense_Cost']
        widgets ={
            'Expense_Item':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Expense'
            }),
            'Expense_Cost':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Amount Spent'
            }),
        }




