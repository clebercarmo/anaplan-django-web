from django.contrib import admin
from .models import *
from django.forms import TextInput, Textarea
from django.db import models
from django.shortcuts import redirect

# Register your models here.
class ParametrosProcessListInline(admin.StackedInline):
    model = ParametrosProcessList


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    pass


@admin.register(Processo)
class ProcessoAdmin(admin.ModelAdmin):
    
    actions = ['carga_anaplan']

    def carga_anaplan(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        for obj in queryset:
            print(obj.id)
            #print(getattr(obj, "id"))
            #print([getattr(obj, field) for field in field_names])
            Historico.objects.create(processo =obj, situacao="ENVIADO PARA PROCESSAMENTO", observacao="Arquivos Enviados com Sucesso")
        return redirect('/anaplan/integrador/historico/')


@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        return False
    
    list_display = ['hora', 'nome_processo', 'situacao']
    search_fields = ['situacao']
    list_filter = ['situacao']
    ordering = ['-hora']


@admin.register(ProcessList)
class ProcessListAdmin(admin.ModelAdmin):

    inlines = [
        ParametrosProcessListInline
    ]

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'90'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

    list_display = ['descricao', 'modelo']
    search_fields = ['modelo']
    list_filter = ['modelo']
    ordering = ['-hora']