from django import forms
from django.db.models.base import Model
from django.forms import fields
from myapp.models import Veiculos


class VeiculosForm(forms.ModelForm):
    class Meta:
        model = Veiculos
        fields = '__all__'
        widgets = {
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
            'cor': forms.TextInput(attrs={'class':'form-control'}),
            'placa': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'cor': 'Cor',
            'placa': 'Placa',
        }