from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=20)

class Login(models.Model):
    usuario = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)


