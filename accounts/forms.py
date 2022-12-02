
from django import forms
from .models import Account,ProfileDetails
from blog.models import Blog

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':"Confirm Password"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':"Password"
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email','password']

        """widgets = {
            'first_name':forms.TextInput(attrs={
                "class":"mb-0",
                "placeholder": "First Name",
                
            }),

            'last_name':forms.TextInput(attrs={
                "class":"mb-0",
                "placeholder": "Last Name",
                
            }),

            'email':forms.EmailInput(attrs={
                "class":"mb-0",
                "placeholder": "Email Address",
                
            }),
            'phone_number':forms.TextInput(attrs={
                "class":"mb-0",
                "placeholder": "Phone Number",
                
            }),

            'password':forms.PasswordInput(attrs={
                "class":"mb-0",
                "placeholder": "Password",
                
            }),

          
        }"""

    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"
        self.fields["phone_number"].widget.attrs["placeholder"] = "Phone Number"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["password"].widget.attrs["placeholder"] = "Password"

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "mb-0"

    def clean(self):
        cleaned_data = super(RegistrationForm,  self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password Doesnt Match"
            )

class ProfileDetailForms(forms.ModelForm):
    class Meta:
        model = ProfileDetails
        fields = ['user_type', 'city', 'county', 'sub_county', 'address', 'zip_code', 'gender', 'secondary_phone']
    
    def __init__(self, *args, **kwargs):
        super(ProfileDetailForms, self).__init__(*args, **kwargs)

        self.fields["user_type"].widget.attrs["placeholder"] = "User Type"
        self.fields["city"].widget.attrs["placeholder"] = "City"
        self.fields["county"].widget.attrs["placeholder"] = "County"
        self.fields["sub_county"].widget.attrs["placeholder"] = "Sub County"
        self.fields["address"].widget.attrs["placeholder"] = "Address"
        self.fields["zip_code"].widget.attrs["placeholder"] = "Zip Code"
        self.fields["gender"].widget.attrs["placeholder"] = "Gender"
        self.fields["secondary_phone"].widget.attrs["placeholder"] = "Secondary Phone"

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'category', 'image', 'blog', 'author')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'type':'text',

            'placeholder':'Blog Title',
            'aria-label':'Recipients username',
            'aria-describedby':'basic-addon13',

        })
        self.fields['category'].widget.attrs.update({
            'type':'select',
            'name':'category',
         

        })
        self.fields['blog'].widget.attrs.update({
            'type':'textarea',
            'name':'category',
            'id':'exampleFormControlTextarea1',
            'rows':'3',
            'class':'form-control',
         

        })
        self.fields['image'].widget.attrs.update({
            'type':'file',
            'name':'image',
            'id':'inputGroupFile04',
            'class':'form-control',
            'aria-label':'Upload',
            'aria-describedby':'inputGroupFileAddon04',
         

        })