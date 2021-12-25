from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import CustomCreateForm,  CustomChangeForm
from .models import CustomUser

class CustomuserAdmin(UserAdmin):
    add_form = CustomCreateForm
    form = CustomChangeForm
    model = CustomUser
    # list_display = ['email', 'username', 'age', 'is_staff', ]


admin.site.register(CustomUser, CustomuserAdmin)