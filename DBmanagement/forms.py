from django import forms
from .models import *


class BaseFrom(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

class NewUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'