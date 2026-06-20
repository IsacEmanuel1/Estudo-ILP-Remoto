import csv

novos_alunos = [
    ["Ana", 25, 86.0],
    ["Isac", 19, 96.0]
]

with open("alunos.csv", "a",  newline="", encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    for linha in novos_alunos:
        escritor.writerow(linha)
