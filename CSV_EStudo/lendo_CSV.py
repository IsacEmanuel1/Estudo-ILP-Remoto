import csv

with  open("alunos.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)

    for linha in leitor:
        print(f"Aluno: {linha[0]} | Idade: {linha[1]} | Nota: {linha[2]}")