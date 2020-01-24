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
    

    def clean_name(self):
        value = self.cleaned_data['name']
        if value.isupper():
            raise forms.ValidationError("please dont use uppercase")
        return value
    
    def clean_confirmPassword(self):
       password = self.cleaned_data['password']
       confirm_Password = self.cleaned_data['confirm_Password']
       if not password == confirm_Password:
            raise forms.ValidationError("Password and Confirm Password not match")
       return confirm_Password