from django.db import models
#from django.forms import widgets

# Create your models here.
class Veiculos(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    placa = models.CharField(max_length=100)