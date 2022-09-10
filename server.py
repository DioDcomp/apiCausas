import json

with open("curso.json", 'r') as file:
    dados = json.load(file)

with open("desempenho.json", 'r') as files:
    disciplina = json.load(files)
  
response = dados
responseDisciplina = disciplina