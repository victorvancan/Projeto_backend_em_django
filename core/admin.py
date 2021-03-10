from django.contrib import admin

from .models import Cargo, Servico, Funcionario, Feature

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificados')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servicos', 'icone', 'ativo', 'modificados')

@admin.register(Funcionario)
class funcionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'funcao', 'bio', 'ativo', 'modificados')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('features', 'icon', 'descricao', 'ativo', 'modificados')
