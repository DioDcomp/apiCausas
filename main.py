from flask import Flask
from flask_cors import CORS
import server

app = Flask(__name__)
CORS(app, resources=r'/curso/*')

@app.get("/curso/curso")
def indexDados():
    return server.responseDados

@app.get("/curso/desempenho")
def indexDesempenho():
    return server.responseDisciplina

@app.get("/curso/sucesso")
def indexSucesso():
    return server.responseSucesso

if __name__ == "__main__":
    app.run()