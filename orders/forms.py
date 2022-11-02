from django import forms 
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = ['first_name', 'last_name', 'phone', 'email','address','zip_code','county', 'city', 'order_note']

        def __init__(self, *args, **kwargs):
            super(OrderForm, self).__init__(*args, **kwargs)

            self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
            self.fields['email'].widget.attrs['placeholder'] = 'email'
            self.fields['phone'].widget.attrs['placeholder'] = 'Phone Number'
            self.fields['address'].widget.attrs['placeholder'] = 'Address'
            self.fields['county'].widget.attrs['placeholder'] = 'County'
            self.fields['city'].widget.attrs['placeholder'] = 'City'
            self.fields['order_note'].widget.attrs['placeholder'] = 'Order Note'

            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'checkout-form-list'
            