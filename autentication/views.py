from django.shortcuts import render
from autentication.forms import *


def index(request):
    form = LoginForm(request.POST) 
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = LoginForm()
            print('Salvou')
            context = {'form': form}
        else:
            form = LoginForm()
            context = {'form': form}
        return render(request, 'index.html', context)
        
    
   

# def index(request):
 
#     if request.method == 'POST':
#         form = CadastroForm(request.POST) 
#         if form.is_valid():
#             form.save()
#             form = CadastroForm()
#             print('Salvou')
#         else:
#             form = CadastroForm()
#         return render(request, 'index.html', {'form' : form})
