from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView
from myapp.models import Veiculos
from .forms import VeiculosForm
from django.shortcuts import redirect

def home(request):
    return render(request, 'bootstrap-admin-template-free/home.html')
def base(request):
    return render(request, 'bootstrap-admin-template-free/base.html')
def crud(request):
    veiculos = Veiculos.objects.all()
    return render(request, 'bootstrap-admin-template-free/crud.html', {'veiculos': veiculos})
def consulta(request):
    return render(request, 'bootstrap-admin-template-free/consulta.html')
def listagem(request):
    veiculos = Veiculos.objects.all()
    return render(request, 'bootstrap-admin-template-free/listagem.html', {'veiculos': veiculos})
def sobre(request):
    return render(request, 'bootstrap-admin-template-free/sobre.html')

def adicionar(request):
    form = VeiculosForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Veiculo cadastrado com sucesso!')
        return redirect('crud')
    return render(request, 'bootstrap-admin-template-free/adicionar.html', {'form': form})

def update(request, id):
    veiculos = Veiculos.objects.get(id=id)
    form = VeiculosForm(request.POST or None, instance=veiculos)
    if form.is_valid():
        form.save()
        return redirect('crud')
    return render(request, 'bootstrap-admin-template-free/update.html', {'form': form, 'veiculos': veiculos})

def delete(request, id):
    veiculo = Veiculos.objects.get(id=id)
    veiculo.delete()
    return redirect('crud')

def busca(request):
    busca = request.GET.get('busca')
    veiculos = Veiculos.objects.filter(marca__icontains=busca)
    return render(request, 'bootstrap-admin-template-free/busca.html', {'veiculos': veiculos})
