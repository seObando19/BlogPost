from django import forms
from users.models import User

class LoginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        """ fields = __all__ => equivale a todos los campos """
        fields = ('email', 'password',)