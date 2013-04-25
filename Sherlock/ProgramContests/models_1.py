#models.py file to contain the different models
#Author Harish Babu Arunachalam
#Date : 29th November 2012

from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = {'username','password1','password2','first_name','last_name','email'}
        
    def save(self,commit=True):
        user = super(UserRegistrationForm,self).save(commit=False)
        print "inside save() method"
        #user.email = self.cleaned_data("email")
        if commit:
            print "inside commit statement"
            user.save()
        return user


    