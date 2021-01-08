from django.db import models

# Create your models here.

SITUACAO = [("ENVIADO PARA PROCESSAMENTO", "ENVIADO PARA PROCESSAMENTO"),
             ("CARGA REALIZADA COM SUCESSO", "CARGA REALIZADA COM SUCESSO"),   
             ("ERRO AO RELIZAR A CARGA DO ARQUIVOS", "ERRO AO RELIZAR A CARGA DO ARQUIVOS"),
             ("ANAPLAN", "ANAPLAN"),
             ("ERRO ANAPLAN", "ERRO ANAPLAN")]

class TimeStampedModel(models.Model):
    data = models.DateField(auto_now=True)
    hora = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Modelo(TimeStampedModel):
    descricao = models.CharField(max_length=80, unique=True, verbose_name="Modelo")

    def __str__(self):
        return self.descricao


class Processo(TimeStampedModel):
    nome = models.CharField(max_length=80, unique=True)
    modelo = models.ForeignKey(Modelo, models.CASCADE, verbose_name="Modelo", related_name='modelo_processo')

    def __str__(self):
        return self.nome


class ProcessList(TimeStampedModel):
    descricao = models.CharField(max_length=80, unique=True, verbose_name="Nome")
    nome_processo_anaplan = models.CharField(max_length=80, verbose_name="Nome Processo Anaplan")
    modelo = models.ForeignKey(Modelo, models.CASCADE, verbose_name="Modelo", related_name='modelo_processlist')

    class Meta:
        verbose_name_plural = 'Processos'
        verbose_name = 'Processo'

    def __str__(self):
        return self.descricao


class Execucao(TimeStampedModel):
    descricao = models.CharField(max_length=80, verbose_name="Nome")
    pasta_arquivos = models.CharField(max_length=100, verbose_name="Pasta dos Arquivos")
    processlist = models.ManyToManyField(ProcessList, verbose_name="Processos")

    class Meta:
        verbose_name_plural = 'Execuções'

    def __str__(self):
        return self.descricao


class ArquivosExecucao(TimeStampedModel):
    pasta = models.CharField(max_length=100)
    arquivo = models.CharField(max_length=60)
    execucao = models.ForeignKey(Execucao, models.CASCADE, verbose_name="Execucao", related_name='execucao_arquivoexecucao')

    def __str__(self):
        return self.pasta 




class ParametrosProcessList(TimeStampedModel):
    processlist = models.ForeignKey(ProcessList, models.CASCADE, verbose_name="Process List", related_name="parametros_processlist")
    chave = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Parâmetros'

    def __str__(self):
        return self.chave

class ParametrosExecucao(TimeStampedModel):
    execucao = models.ForeignKey(Execucao, models.CASCADE, verbose_name="Execução", related_name="parametrosexecucao_execucao")
    arquivo_anaplan = models.CharField(max_length=50)
    arquivo_forno = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Parâmetro"

    def __str__(self):
        return self.arquivo_anaplan


class Historico(TimeStampedModel):
    processo = models.ForeignKey(Processo, models.CASCADE, verbose_name="Processo", related_name='modelo_historico', blank=True, null=True)
    execucao = models.ForeignKey(Execucao, models.CASCADE, verbose_name="Execucao", related_name='execucao_historico', blank=True, null=True)
    situacao = models.CharField(choices=SITUACAO, verbose_name="Situação", max_length=40)
    observacao = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Log de Carga Arquivos Anaplan'

    def __str__(self):
        return self.situacao

    def nome_processo(self):  
        return self.processo.nome 




