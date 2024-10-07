from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForms (UserCreationForm):
    email=forms.EmailField(max_length=254,required=True,help_text="Request .Enter a valid email address.")
    
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
    
    def clean(self):
        cleaned_data =super ().clean()
        email= cleaned_data.get("email")
        username = cleaned_data.get("username")
        
        if User.objects.filter(email=email).exists():
            self.add_error("email", 'This email address is already in use.')
            
        if User.objects.filter(username=username).exists():
            self.add_error("username",'This username is already Taken')
        
        return cleaned_data