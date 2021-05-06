from django import forms
from users.models import User

class UserForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        """ fields = __all__ => equivale a todos los campos """
        fields = [
            'name',
            'lastname',
            'email',
            'username',
            'password',
        ]
        labels = {
            'name': 'Name',
            'lastname': 'Lastname',
            'email': 'Email',
            'username': 'Username',
            'password': 'Password',
        }
