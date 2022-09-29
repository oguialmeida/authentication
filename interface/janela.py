import PySimpleGUI as sg
import requests as rq

# Busca uma resposta no endereço da API
dadosUsuario = rq.get("http://127.0.0.1:5000/user")

# Transforma a resposta obtida em um objeto
dadosUsuario = dadosUsuario.json()

# Cria o layout da janela
layout = (
    [
        [sg.Text("Usuário")],
        [sg.Input(key="usuario")],
        [sg.Text("Senha")],
        [sg.Input(key="senha")],
        [sg.Button("Login")],
        [sg.Text("", key="Mensagem")],
    ],
)

# Inicia a janela e atribui os respectivos valores do objeto para o nome de usuario e a senha
def iniciarTela():
    window = sg.Window("Login", layout=layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Login":
            senhaCorreta = str(dadosUsuario["senha"])
            usuarioCorreto = str(dadosUsuario["nome"])
            usuario = str(values["usuario"])
            senha = str(values["senha"])

            if senha == senhaCorreta and usuario == usuarioCorreto:
                window["Mensagem"].update("Login feito com sucesso! :)")
            else:
                window["Mensagem"].update("Senha ou usuário incorretos! :(")


if __name__ == "__main__":
    iniciarTela()
