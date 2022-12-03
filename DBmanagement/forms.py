from django import forms
from .models import *


class BaseFrom(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'


class ServiceFrom(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class NewUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'


class CarFrom(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'
