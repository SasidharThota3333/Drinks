from django import forms
from django.forms import ModelForm
from .models import *

class Drinks_Forms(ModelForm):
    class Meta:
        model = Drinks
        fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'

class ToDo_Forms(ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'
        widgets = {
            'Date': DateInput(),
        }

