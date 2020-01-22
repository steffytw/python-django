from django import forms
from . models import student
class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name','age','address']