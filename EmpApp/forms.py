from django import forms

from EmpApp.models import Employee

from EmpApp.models import Login
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','password','email')





class EmployeeForm(forms.ModelForm):

    class Meta:
        model=Employee
        fields="__all__"


class LoginForm(forms.ModelForm):

    class Meta:
        model=Login
        fields="__all__"
