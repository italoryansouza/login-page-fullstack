from django import forms
from django.contrib.auth.models import User, AuthenticationForm

class RegisterForm(forms.ModelForm):
    password= forms.CharField(widget= forms.PasswordInput)
    password_confirm = forms.CharField(widget= forms.PasswordInput, label= 'Confirmar senha')

    class Meta:
        model= User
        fields= ['username', 'email', 'password']

    def Clean(self):
        cleaned_data = super().clean()
        password= cleaned_data.get('password')
        password_confirm= cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "passwords dont match")

class LoginForm(AuthenticationForm):
    pass
