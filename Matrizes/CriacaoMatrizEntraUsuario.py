linhas = 2
colunas = 3

matriz_2x3 = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor para a posiçõa ({i}, {j}): "))
        linha += [valor]      
    matriz_2x3 += [linha]

for i in range(linhas):
    for j in range(colunas):
        print(matriz_2x3 [i] [j], end=" ")
    print()
