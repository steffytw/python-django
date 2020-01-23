from django import forms
from . models import student
class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name','age','address']

class signupForm(forms.Form):
    name = forms.CharField()
    username = forms.CharField()
    screen_name =forms.CharField()
    address = forms.CharField(widget = forms.Textarea(attrs={'class':'style','pattern':'[a-zA-Z0-9]+'}))
    password = forms.CharField(widget =forms.PasswordInput)
    confirm_Password = forms.CharField(widget = forms.PasswordInput)
    terms_accepted = forms.BooleanField()