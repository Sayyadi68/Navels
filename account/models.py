from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User
from django.utils.translation import gettext as _


import datetime
from phonenumber_field.modelfields import PhoneNumberField
import pytz


class Plan(models.Model):
    pass

class account(AbstractUser):
    username = models.CharField(unique=True,null=True,max_length=500,verbose_name=_("User Name"))
    UserID = models.CharField(max_length=10)
    UserPass = models.CharField(max_length=20, verbose_name=_("User Password"))
    email = models.EmailField(verbose_name=_("User Email"))
    Plans = models.ForeignKey(Plan, null=True,blank=True, on_delete=models.CASCADE, verbose_name=_("User Plan"))
    UserBio = models.TextField(blank=True, null=True ,verbose_name=_("My bio"), default="سلام این بیوگرافی من است")
    UserImg = models.ImageField(blank=True, null=True , verbose_name=_("My Image"), default='Wallpaper_4K3D_2573.jpg' )
    is_staff = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=False)
    expire_time = models.DateTimeField(auto_now=True, verbose_name=_("Expire Time"))
    phone_number = PhoneNumberField(unique=True, null=True, verbose_name=_("Phone Number"))
    otp = models.PositiveIntegerField(blank=True, null=True, verbose_name=_("Verification Code"))


    def otp_valid(self, otp):
        if int(otp) == self.otp:
            if (datetime.datetime.now().astimezone(pytz.utc).minute - self.expire_time.minute) <= 1:
                if (datetime.datetime.now().astimezone(pytz.utc).second - self.expire_time.second) <= 45:
                    self.is_verify = True
                    self.save()
                    return True
        return False

    def __str__(self):
        return f'{self.username}'


class ticet(models.Model):
    sender = models.ForeignKey(account,null=True, on_delete=models.CASCADE ,verbose_name=_("User Name"))
    ticetreson = models.TextField()
    ticet_text =  models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)
    visibale = models.BooleanField(default=True)




