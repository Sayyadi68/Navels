from django import forms

from . import models

class LoginForm(forms.Form):
    class Meta:
        model = models.account
        fields = ['username','phone_number','email', 'UserID', 'UserPass', 'email']


class OtpForm(forms.Form):
    class Meta:
        model = models.account
        fields = ['otp']

class CustomUserInfoForm(forms.ModelForm):
    class Meta:
        model = models.account
        fields = ['username', 'UserPass' ,'Plans','UserBio','UserImg']



class Ticketform(forms.Form):
    class Meta:
        model = models.ticet
        fields = ['sender', 'recever' ,'ticetreson','ticet_text', 'visibale']


