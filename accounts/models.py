from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.conf import settings
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username,phone_number,email, password=None):
        if not email:
            raise ValueError('User must have an email')

        if not username:
            raise ValueError ('User must have username')

        user = self.model(
            email = self.normalize_email(email),
            username =username,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,


        )
        user.is_admin = True
        user.is_active =True
        user.is_staff = True
        user.is_superadmin = True
        user.set_password(password)
        user.save(self._db )
        return user

    def create_superuser(self, first_name, last_name, email,phone_number, username, password=None, **extra_fields):
        user = self.create_user(
            email = self.normalize_email(email),
            username =username,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
        )
        user.is_admin = True
        user.is_active =True
        user.is_staff = True
        user.is_superadmin = True
        user.save(self._db )
        return user
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    email= models.EmailField(max_length=50,null=True, blank=True, unique=True)
    phone_number= models.CharField(max_length=50, null=True, blank=True)

    date_joined = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', "phone_number"]

    objects =  MyAccountManager()

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural='Accounts'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_active

    def has_module_perms(self, app_label):
        return self.is_active

class ProfileDetails(models.Model):
    user =  models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete = models.CASCADE,
    )
    user_type= models.CharField(max_length=50, null=True, blank=True)
    county = models.CharField(max_length=50, null=True, blank=True)
    sub_county = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    secondary_phone = models.CharField(max_length=50, null=True, blank=True)
   