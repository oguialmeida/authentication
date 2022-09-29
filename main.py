# Tem o intuito de iniciar o servidor e a aplicação simultaneamente
from server import servidor as sv
from interface import janela as jn

if __name__ == "__main__":
    sv.servidorPrincipal()
    jn.iniciarTela()
