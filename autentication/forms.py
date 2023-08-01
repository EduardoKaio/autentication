from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from autentication.models import *


class CadastroForm(UserCreationForm):
  first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Nome completo', 'class' : 'input100'}))
  phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Celular', 'class' : 'input100', 'maxlength': '15', 'onkeyup': 'handlePhone(event)'}))
  email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class' : 'input100'}))
  username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Usuário', 'class' : 'input100'}))
  password1=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class' : 'input100'}))
  password2=forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar senha', 'class' : 'input100'}))
  class Meta:
    model = User
    fields = ('first_name', 'email', 'username', 'phone', 'password1' ,'password2' )

class RecuperarForm(forms.Form):
  email = forms.EmailField(required=True)
