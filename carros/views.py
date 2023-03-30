from django.shortcuts import render, redirect
from .models import Carro
from django.urls import reverse
from django.http import HttpResponse
from fornecedores.models import Fornecedor

def carros(request):
    if request.method == "GET":
        carros = Carro.objects.all()
        fornecedores = Fornecedor.objects.all()
        return render(request, 'carros.html', {'carros':carros, 'fornecedores':fornecedores})
    elif request.method == "POST":
        placaCarro = request.POST.get('placaCarro')
        nomeCarro = request.POST.get('nomeCarro')
        combustivelCarro = request.POST.get('combustivelCarro')
        especificacaoCarro = request.POST.get('especificacaoCarro')
        fornecedor = request.POST.get('fornecedor')
        anoFabricacaoCarro = request.POST.get('anoFabricacaoCarro')
        anoModeloCarro = request.POST.get('anoModeloCarro')
        chassiCarro = request.POST.get('chassiCarro')
        carro = Carro(
            placaCarro = placaCarro,
            nomeCarro = nomeCarro,
            combustivelCarro = combustivelCarro,
            especificacaoCarro = especificacaoCarro,
            fornecedor_id = fornecedor,
            anoFabricacaoCarro = anoFabricacaoCarro,
            anoModeloCarro = anoModeloCarro,
            chassiCarro = chassiCarro
        )
        carro.save()
        return redirect(reverse('carros'))

def editar_carro(request,id):
    carro = Carro.objects.get(id=id)
    fornecedores = Fornecedor.objects.all()
    return render(request, 'upd_carro.html', {'carro':carro, 'fornecedores':fornecedores})

def upd_carro(request, id):
    carro = Carro.objects.get(id=id)
    placaCarro = request.POST.get('placaCarro')
    nomeCarro = request.POST.get('nomeCarro')
    combustivelCarro = request.POST.get('combustivelCarro')
    especificacaoCarro = request.POST.get('especificacaoCarro')
    fornecedor_id = request.POST.get('fornecedor')
    anoFabricacaoCarro = request.POST.get('anoFabricacaoCarro')
    anoModeloCarro = request.POST.get('anoModeloCarro')
    chassiCarro = request.POST.get('chassiCarro')
    
    carro.placaCarro = placaCarro
    carro.nomeCarro = nomeCarro
    carro.combustivelCarro = combustivelCarro
    carro.especificacaoCarro = especificacaoCarro
    carro.fornecedor_id = fornecedor_id
    carro.anoFabricacaoCarro = anoFabricacaoCarro
    carro.anoModeloCarro = anoModeloCarro
    carro.chassiCarro = chassiCarro
    carro.save()
    return redirect(reverse('carros'))