from django.contrib import admin
from .models import *
from django.forms import TextInput, Textarea
from django.db import models
from django.shortcuts import redirect
from integrador.AnaplanImportCaller import envio_anaplan

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
        l_process_list = []
        l_process_list_final = []

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        for obj in queryset:
            print(obj.id)
            print(obj.modelo.descricao)
            for process_list in ProcessList.objects.filter(modelo=obj.modelo):
               for param_process_list in process_list.parametros_processlist.all():
                   l_process_list.append({param_process_list.chave: param_process_list.valor})
               l_process_list_final.append([process_list.descricao, l_process_list])
               l_process_list = []
            #print(getatt[r(obj, "id"))
            #print([getattr(obj, field) for field in field_names])
            envio_anaplan(obj.modelo.descricao, obj.diretorio, l_process_list_final)
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