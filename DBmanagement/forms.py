from django import forms
from .models import *


class BaseFrom(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class ServiceFrom(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class NewUserForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class NewCarFrom(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class NewOrderForm(forms.ModelForm):
    DateOfOrder = forms.DateInput()
    DateStart = forms.DateInput()
    DateEnd = forms.DateInput()
    class Meta:
        model = Order
        fields = '__all__'
