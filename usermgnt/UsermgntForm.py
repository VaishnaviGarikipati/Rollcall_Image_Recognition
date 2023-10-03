
from django import forms
#from captcha.fields import CaptchaField

class UsermgntForm(forms.Form):
    username=forms.CharField(label='username',max_length=50,required=True)
    userpwd=forms.CharField(label='password',max_length=50,required=True, widget=forms.PasswordInput)
    captcha=CaptchaField()