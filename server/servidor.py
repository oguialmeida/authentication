from flask import Flask
from views import views

def servidorPrincipal():
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix="/")
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    servidorPrincipal()
