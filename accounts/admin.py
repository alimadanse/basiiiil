from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CusomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CusomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':("phone_number",)}),
        # (None, {'fields':("age","nat_id")}),
        )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':("phone_number")}),
    )    

admin.site.register(CustomUser, CustomUserAdmin)

