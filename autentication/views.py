from django.shortcuts import render
from autentication.forms import *
from django.contrib.auth.forms import UserCreationForm  
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def cadastro(request):
    mensagemErro = False
    if request.method == 'POST':
        form_cadastro = CadastroForm(request.POST) 
        if form_cadastro.is_valid():
            form_cadastro.save()
            messages.success(request, 'Conta criada com sucesso')
            print('Salvou')
            return redirect('logar_usuario')
        else:
            mensagemErro = True
            print('Não salvou')
    else:
        form_cadastro = CadastroForm(request.POST)
    
    context = {'mensagemErro' : mensagemErro, 
               'form_cadastro' : form_cadastro, }
    
    return render(request, 'cadastro.html',context)
        

def logar_usuario(request):
    mensagemErro = False
    if request.method == "POST":
        form_login = AuthenticationForm()
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        
        if usuario is not None:
            login(request, usuario)
            print('entrou')
            return redirect('index')
        else:
            print('não entrou')
            form_login = AuthenticationForm()
            mensagemErro = True

    else:
        form_login = AuthenticationForm()
    
    context = {'mensagemErro' : mensagemErro, 
               'form_login' : form_login, }
    
    return render(request, 'logar_usuario.html', context)


def logout_aplicacao(request):
    logout(request)
    return redirect('logar_usuario')



@login_required
def index(request):
    return render(request, 'index.html')



