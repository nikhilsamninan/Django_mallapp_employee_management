from django import forms
from .models import *

class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class Imgform(forms.ModelForm):
    class Meta:
        model = Images
        fields ='__all__'
