from django import forms
from django.contrib.auth.forms import UserCreationForm
from roadapp.models import User,Violation

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2","phone","email"]
        widget={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"})
        }

class SignInForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

class ViolationForm(forms.ModelForm):
    class Meta:
        model=Violation
        fields="__all__"