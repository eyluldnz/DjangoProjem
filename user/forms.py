from  django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, FileInput

from home.models import UserProfil


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields= ('username', 'email', 'first_name','last_name')
        widgets = {
            'username': TextInput(attrs={'class':'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'firts_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfil
        fields = ('phone', 'adress', 'city','country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'adress': TextInput(attrs={'class': 'input', 'placeholder': 'adress'}),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'country'}),
            'city': TextInput(attrs={'class': 'input', 'placeholder': 'city'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
        }



