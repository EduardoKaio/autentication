from django.contrib import admin
from autentication.models import *

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

admin.site.register(Login)
admin.site.register(Pessoa, PessoaAdmin)