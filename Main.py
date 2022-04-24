from Treatment import Treatment
import os

shutdown = False
os.chdir("root")

while not(shutdown):
    place = os.getcwd() + '~#:'
    print("\n**Operações sobre arquivos**\n - Criar arquivo (touch)\n - Remover arquivo (rm)\n - Escrever no arquivo (echo 'conteudo legal' >> arquivo)\n - Ler arquivo (cat)\n - Copiar arquivo (cp arquivo1 arquivo2)\n - Renomear arquivo (mv arquivo1 arquivo2)\n")
    print("\n**Operações sobre diretorios**\n - Criar diretorio (mkdir diretorio)\n - Remover diretorio (rmdir diretorio)\n - Trocar de diretório (cd diretorio)\n - Renomear diretorio (mv diretorio1 diretorio2)\n")
    shutdown = Treatment(input(place))