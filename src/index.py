import json
from flask import Flask
from aplicacao.processamento_imagem import realizar_treino

app = Flask(__name__)


@app.route("/")
def index():
    texto = "Hello world"
    return json.dumps(texto)


@app.route("/processamentoImagem")
def processamento_imagem():    
    
    resultado = realizar_treino()

    return json.dumps(resultado)
