import integrador.PyTools.dataAcquisition as dtAquisicao
import pathlib 
from integrador.util import ler_arquivos_pasta, mover_arquivos
from django.contrib.auth.models import User


def envio_anaplan(model, diretorio, processList):
   
    usuario_anaplan = User.objects.get(groups__name='Acesso Anaplan')
    model = model
    user="paolo.malafaia@flexthink.com.au"
    pwd = "Number28"
    #user = usuario_anaplan.username
    #pwd = usuario_anaplan.password

    diretorio_script = pathlib.Path(__file__).parent.absolute()

    pasta_in = diretorio + '/IN/'
    pasta_out = diretorio + '/OUT/'

    dataList = ler_arquivos_pasta(pasta_in)

    importList =\
    [
    ]

    processList=processList
    dtAquisicao.main(user, pwd, model, dataList, importList, processList)
    mover_arquivos(pasta_in, pasta_out)