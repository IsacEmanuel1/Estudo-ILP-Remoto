import csv

with  open("alunos.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(f"Aluno: {linha["Aluno"]} | Idade: {linha["idade"]} | Nota: {linha["nota"]}")