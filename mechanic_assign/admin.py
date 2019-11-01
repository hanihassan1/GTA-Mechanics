from django.contrib import admin
from mechanic_assign.models import *
from mechanic_assign.models import customers, CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from mechanic_assign.forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display= ['username', 'email', 'password']
    


admin.site.register(CustomUser,CustomUserAdmin)


admin.site.register(car)

admin.site.register(customers)

admin.site.register(employee)

admin.site.register(services)

admin.site.register(booking)