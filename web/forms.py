from authentication.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    """ Form for user sign in"""
    remember_me = forms.BooleanField(required=False)


class RegisterForm(forms.Form):
    """ Form for user registration """
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
