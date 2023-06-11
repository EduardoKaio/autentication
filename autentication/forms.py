from django import forms
from autentication.models import *


class LoginForm(forms.Form): 
  email = forms.EmailField(max_length=100, label='E-mail', widget=forms.TextInput(attrs={'class' : ' input-email', 'pattern' : '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'}))
  Senha = forms.CharField( max_length=100, label='senha', widget=forms.TextInput(attrs={ 'class' : ''}))

class CadastroForm(forms.ModelForm): 
  
  class Meta:
        model=Pessoa
        fields= '__all__'   
        
        widgets = {  
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'senha': forms.TextInput(attrs={'class': 'form-control'})
             }