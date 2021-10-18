from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username,email, password=None):
        if not email:
            raise ValueError('User must have an email')

        if not username:
            raise ValueError ('User must have username')

        user = self.model(
            email = self.normalize_email(email),
            username =username,
            first_name = first_name,
            last_name = last_name,

        )
        user.is_admin = True
        user.is_active =True
        user.is_staff = True
        user.is_superadmin = True
        user.save(self._db )
        return user

class Account(AbstractBaseUser):
    pass
