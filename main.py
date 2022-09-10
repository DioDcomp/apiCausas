from flask import Flask
from flask_cors import CORS
import server

app = Flask(__name__)
CORS(app, resources=r'/curso/*')

@app.get("/curso/curso")
def index():
    return server.response

@app.get("/curso/desempenho")
def indexDesempenho():
    return server.responseDisciplina

if __name__ == "__main__":
    app.run()