from django import forms

from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control' ,'id':'nameid','autocomplete':'name'}),
            'email': forms.EmailInput(attrs={'class':'form-control' ,'id':'emailid','autocomplete':'email'}),
            'password': forms.PasswordInput(render_value=True,attrs={'class':'form-control','id':'passwordid'}),
            
        }
        
