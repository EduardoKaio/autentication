from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from autentication.models import *


class CadastroForm(UserCreationForm):
  first_name = forms.CharField(required=True)
  phone = forms.CharField(required=True)
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ('first_name', 'username', 'email', 'phone', 'password1' ,'password2' )