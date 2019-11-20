from django import forms
from HotelApp.models import Employee,Upload
from django.contrib.auth.models import User
# Create your models here.
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        #fields=('eid','ename') ====>tuple
        #exclude=['salary'] #=======>list

class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password')
        widgets = {
            'password': forms.PasswordInput(),
        }

class UploadForm(forms.ModelForm):
    class Meta:
        model=Upload
        fields=('name','pic')



        
