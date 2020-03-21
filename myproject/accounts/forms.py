from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'input100'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'class':'input100'}))
    class Meta:
        model = User
        fields=['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username', 'class':'input100'}),
            'email': forms.TextInput(attrs={'placeholder':'Email', 'class':'input100'}),
        }
        
