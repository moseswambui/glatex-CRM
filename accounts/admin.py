from django.contrib import admin

from .models import Account, ProfileDetails
class AccountAdmin(admin.ModelAdmin):
    model = Account
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'is_active',
        )

    search_fields = (
        'first_name',
        'email',
        'phone_number'
    )

    list_filter = (
        'is_active',
        "is_admin",
    )

class ProfileDetailAdmin(admin.ModelAdmin):
    model = ProfileDetails
    list_display = (
        'user',
        'gender',
        'user_type',
        'county',
        'sub_county',
        'city',
        'address',
        'zip_code',
        )

    search_fields = (
        'user',
        'county',
    )

    list_filter = (
        'user_type',
        "city",
    )

admin.site.register(Account, AccountAdmin)
admin.site.register(ProfileDetails, ProfileDetailAdmin)