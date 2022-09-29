# Flask é um micro-framework que visa ofecer ferramentas para a contrução de aplicações modularizadas
from flask import Flask
from views import views

# Inicia o servidor na porta desejada
def servidorPrincipal():
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix="/")
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    servidorPrincipal()
