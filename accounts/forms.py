from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["email", "username"]


class SignUpForm(forms.Form):
    username = forms.CharField(
        label="Nome de Usuário",
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Nome de Usuário"})
    )
    email = forms.EmailField(label="Email ", max_length=128, required=True)
    password = forms.CharField(label="Senha ", max_length=255, required=True, widget=forms.PasswordInput)
    confirmation = forms.CharField(label="Confirme a Senha ", max_length=255, required=True, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=64, required=True)
    password = forms.CharField(label="Senha", max_length=255, required=True, widget=forms.PasswordInput)
