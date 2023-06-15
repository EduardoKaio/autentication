from django.contrib import admin
from autentication.models import *

class User(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'phone')

admin.site.register(Login)
admin.site.register(Pessoa)