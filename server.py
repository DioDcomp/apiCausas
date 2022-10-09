import json

with open("curso.json", 'r') as file:
    dados = json.load(file)

with open("sucesso.json", 'r') as file:
    sucesso = json.load(file)

with open("cc.json", 'r') as file:
    cc = json.load(file)

with open("ec.json", 'r') as file:
    ec = json.load(file)

with open("si.json", 'r') as file:
    si = json.load(file)

responseCC = cc
responseEC = ec
responseSI = si
responseDados = dados
responseSucesso = sucesso