from django.contrib import admin

from . models import Cargo, Servicos, Funcionario


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servicos)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class Funcionario(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')
