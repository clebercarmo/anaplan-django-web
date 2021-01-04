from os import listdir
from os.path import isfile, join
import pathlib 
import shutil

#MOVER ARQUIVOS
def mover_arquivos(origem, destino):
    lista = listdir(origem) 
    
    lista_len = len(lista)
    x = 0
    
    while x < lista_len:
        caminhoCompleto_old = origem + lista[x] 
        caminhoCompleto_new = destino + lista[x] 
        shutil.move(caminhoCompleto_old, caminhoCompleto_new)
        x += 1


def ler_arquivos_pasta(caminho_arquivos):
    lista_arquivos = []
    [lista_arquivos.append([f, caminho_arquivos+f])  for f in listdir(caminho_arquivos) if isfile(join(caminho_arquivos, f))]
    return lista_arquivos
