from django import forms
from captcha.fields import CaptchaField

from .models import User





class CheckCode(forms.Form):
    captcha = CaptchaField()

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=6, max_length=16)
    password = forms.CharField(required=True, min_length=6, max_length=16)

class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=6, max_length=16)
    password = forms.CharField(required=True, min_length=6, max_length=16)

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['media/users/avatar/']

        





# class UploadImageForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['image']


# class UserInfoForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['group', 'add_time']

