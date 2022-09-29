# A biblioteca funciona como um "estacionamento" de rotas para poder modularizar a aplicação
from flask import Blueprint, jsonify

# Estabelece uma prioridade de leitura antes da refatoração
views = Blueprint(__name__, "views")


@views.route("/")
def principal():
    saudacoes = "Bem vindo! Vida longa e prospera 🖖"
    mensagem = {"Mensagem": saudacoes}
    return jsonify(mensagem)


@views.route("/user")
def getUser():
    return jsonify(
        {"id": 1, "nome": "Guilherme", "senha": 123456},
    )
