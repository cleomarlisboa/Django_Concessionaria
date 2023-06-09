from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from .models import Venda
from carros.models import Carro, Versao
from clientes.models import Cliente
from colaboradores.models import Colaborador
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import VendasModelForm
from permissoes.redirecionar import RedirectPermissionRequiredMixin


class VendasListar(RedirectPermissionRequiredMixin, ListView):
    model = Venda
    template_name = 'vendas/vendas.html'
    permission_required = 'vendas.permissao_funcionario'
    paginate_by = 10

class VendasCriar(RedirectPermissionRequiredMixin, CreateView):
    model = Venda
    form_class = VendasModelForm
    template_name = 'vendas/vendaForm.html'
    permission_required = 'vendas.permissao_funcionario'
    success_url = reverse_lazy('vendas:listar')

    def form_valid(self, form):
        versao = form.cleaned_data['versao']
        if versao.estoque <= 0:
            form.add_error('versao', f'{versao.nome} sem estoque!')
            return self.form_invalid(form)
        else:
            messages.success(self.request, 'venda realizada com sucesso. ')
            versao.estoque -= 1
            versao.save()
            return super().form_valid(form)

class VendasEditar(RedirectPermissionRequiredMixin, UpdateView):
    model = Venda
    form_class = VendasModelForm
    template_name = 'vendas/vendaForm.html'
    permission_required = 'vendas.permissao_funcionario'
    success_url = reverse_lazy('vendas:listar')

    def form_valid(self, form):
        versaoAposEditar = form.cleaned_data['versao']
        versaoAntesEditar = self.versaoAntesEditar
        if (versaoAposEditar != versaoAntesEditar):
            if versaoAposEditar.estoque <=0:
                form.add_error('versao', f'{versaoAposEditar.nome} sem estoque!')
                return self.form_invalid(form)
            versaoAntesEditar.estoque += 1
            versaoAposEditar.estoque -= 1
            versaoAposEditar.save()
            versaoAntesEditar.save()
        messages.success(self.request, 'venda editada com sucesso. ')
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        object_ = self.get_object()
        initial['dataHora'] = object_.dataHora.strftime('%Y-%m-%dT%H:%M')
        self.versaoAntesEditar = object_.versao
        return initial

class VendasExcluir(RedirectPermissionRequiredMixin, DeleteView):
    model = Venda
    template_name = 'vendas/vendaExcluir.html'
    permission_required = 'vendas.permissao_supervisor'
    success_url = reverse_lazy('vendas:listar')

    def form_valid(self, form):
        messages.success(self.request, 'venda excluida com sucesso. ')
        object_ = self.get_object()
        versao = object_.versao
        versao.estoque += 1
        versao.save()
        return super().form_valid(form)
