from django.db import models

# Create your models here.

SITUACAO = [("SUCESSO", "SUCESSO"),
             ("ERRO", "ERRO")]

class TimeStampedModel(models.Model):
    data = models.DateField(auto_now=True)
    hora = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Modelo(TimeStampedModel):
    descricao = models.CharField(max_length=80, unique=True, verbose_name="Modelo")

    def __str__(self):
        return self.descricao


class ProcessList(TimeStampedModel):
    descricao = models.CharField(max_length=80, unique=True)
    modelo = models.ForeignKey(Modelo, models.CASCADE, verbose_name="Modelo", related_name='modelo_processlist')

    def __str__(self):
        return self.descricao


class ParametrosProcessList(TimeStampedModel):
    processlist = models.ForeignKey(ProcessList, models.CASCADE, verbose_name="Process List", related_name="parametros_processlist")
    chave = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)

    def __str__(self):
        return self.chave


class Processo(TimeStampedModel):
    nome = models.CharField(max_length=80, unique=True)
    modelo = models.ForeignKey(Modelo, models.CASCADE, verbose_name="Modelo", related_name='modelo_processo')
    diretorio = models.CharField(max_length=150, verbose_name="Diretorio Arquivos")

    def __str__(self):
        return self.nome


class Historico(TimeStampedModel):
    processo = models.ForeignKey(Processo, models.CASCADE, verbose_name="Processo", related_name='modelo_historico')
    situacao = models.CharField(choices=SITUACAO, verbose_name="Situação", max_length=20)

    def __str__(self):
        return self.processo.nome



