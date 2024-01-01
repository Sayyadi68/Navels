from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from . import models

@admin.register(models.account)
class MenuAdmin(UserAdmin):

    list_display = ('username', 'UserID', 'email' ,'UserPass', 'Plans','UserBio','UserImg','is_verify','phone_number','is_staff','otp')

    add_fieldsets = UserAdmin.fieldsets + (
        (None,
         {'fields': (
         'username', 'UserID', 'email', 'UserPass', 'Plans', 'UserBio', 'UserImg', 'is_verify', 'phone_number',
         'is_staff', 'otp',)}),
    )

    fieldsets = (
        (None,
         {'fields': ('username', 'UserID', 'email' ,'UserPass', 'Plans','UserBio','UserImg','is_verify','phone_number','is_staff','otp',)}),
    )




@admin.register(models.ticet)
class ticketAdmin(admin.ModelAdmin):
    list_display = ('sender' ,'ticetreson','ticet_text', 'visibale','send_time')




