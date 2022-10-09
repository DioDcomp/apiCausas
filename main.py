from flask import Flask
from flask_cors import CORS
import server

app = Flask(__name__)
CORS(app, resources=r'/*')

@app.get("/")
def index():
    return "<h1>Not found!</h1>"

@app.get("/curso")
def indexDados():
    return server.responseDados

@app.get("/sucesso")
def indexSucesso():
    return server.responseSucesso

@app.get("/cc")
def indexCC():
    return server.responseCC

@app.get("/ec")
def indexEC():
    return server.responseEC

@app.get("/si")
def indexSI():
    return server.responseSI

if __name__ == "__main__":
    app.run()