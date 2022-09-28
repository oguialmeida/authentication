import PySimpleGUI as sg
import requests as rq


dadosUsuario = rq.get("http://127.0.0.1:5000/user")
dadosUsuario = dadosUsuario.json()
print(dadosUsuario)

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
