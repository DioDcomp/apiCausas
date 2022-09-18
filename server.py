import json

with open("curso.json", 'r') as file:
    dados = json.load(file)

with open("desempenho.json", 'r') as file:
    disciplina = json.load(file)

with open("sucesso.json", 'r') as file:
    sucesso = json.load(file)
  
responseDados = dados
responseDisciplina = disciplina
responseSucesso = sucesso