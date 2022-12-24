
from django import forms
from .models import Account,ProfileDetails
from blog.models import Blog, BlogCommentary

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
        fields = ('title', 'category','type', 'image', 'blog', 'author')

    def __init__(self, *args, **kwargs):
        super(AddBlogForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['id'] = 'title'
        self.fields['category'].widget.attrs['id'] = 'category'
        self.fields['type'].widget.attrs['id'] = 'type'
        self.fields['image'].widget.attrs['id'] = 'image'
        self.fields['blog'].widget.attrs['id'] = 'blog'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

        self.fields['category'].queryset = Blog.objects.none()

        if "type" in self.data:
            try:
                type_id = int(self.data.get('type'))
                print(type_id)
                self.fields['category'].queryset = Blog.objects.filter(type_id=type_id).order_by('name')
            except(ValueError, TypeError):
                pass

        elif self.instance.id:
            self.fields['category'].queryset = self.instance.type.category_set.order_by('name')

class BlogCommentaryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs = {
        'class':'form-control',
        'id':"title",
        }))
    commentary = forms.CharField(widget=forms.Textarea(attrs = {
        'class':'form-control',
        "id":"commentary",
        }))
    class Meta:
        model = BlogCommentary
        fields = ('title', 'commentary', 'blog','author')