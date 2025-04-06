from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
class CustomUser(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password","address")}),
        
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password",'address'),
            },
        ),
    )

admin.site.register(User,CustomUser)