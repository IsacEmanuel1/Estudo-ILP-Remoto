import random # números aleatórios
import csv # manipulação de arquivo csv
import os # manipulação do terminal
import funcoes_Projeto as funcoes # funções do projeto

def sortearNumeros(limite): #FUNÇÃO PARA SORTEAR NUMEROS, CRIA UMA MATRIZ COM NUMERO ALEATORIOS DE 1 A 30
    while True:
        numerosSorteados=[] # Lista para armazenar números sorteados
        compare = [] # Lista utilziada para comparação de números iguais
        
        for linha in range(2): # monta a matriz
            numerosSorteados.append([])
            while True:
                for coluna in range(3):
                    numerosSorteados[linha].append(random.randint(1, limite)) # Sorteia um limite de números para cada linha
                break
        for i in numerosSorteados: #
            for j in i:
                compare.append(j) # Adiciona cada número sorteado a lista de comparação
                
        compareConj = set(compare) 
        
        if len(compareConj) < len(compare): # Após criar um conjunto da mesma lista, compara a diferença entre eles
            continue # Refaz um novo sorteio
        else:
            return numerosSorteados # Retorna os números sorteados

def compararNumeros(sorteados):#RECEBE COMO PARAMETRO A LISTA INT DO USUARIO E COMPARA COM A MATRIZ

    numeros_sorteados = [int(num) for sublista in sorteados for num in sublista] # converte para uma lista simples
    num_acertados = [] # Guardará os números acertados [reset constante]
    resultados = [] # Guardará o resultado de todos os usuários
    
    premiosCategoria = {"sena":1000000,"quinta":500000,"quarta":350000} # Atribui o valor total para cada categoria
    qntCategoria = {"sena":0,"quinta":0,"quarta":0} # Quantidade de cada categoria [será alterado]

    with open('csv/apostas.csv', "r", encoding="utf-8") as arquivo: # Lê arquivo das apostas
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            usuarios = linha.get("Usuarios")
            quantidadeAcertos = 0
            categoria = "n/a" 
            premio = 0 

            for chave in linha: # Verifica números acertados
                
                if chave != "Usuarios":
                    if int(linha[chave]) in numeros_sorteados:
                        quantidadeAcertos += 1
                        num_acertados.append(int(linha[chave]))
                        
            match quantidadeAcertos: # Verifica qual categoria
                case 6:
                    categoria = "sena"
                case 5:
                    categoria = "quinta"
                case 4:
                    categoria = "quarta" 

            if categoria != "n/a":
                qntCategoria[categoria] += 1 # Altera a contagem de cada categoria

            resultados.append({ # Guarda todos os resultados
                "usuario":usuarios,
                "quantidadeAcertos":quantidadeAcertos,
                "num_acertados":num_acertados,
                "categoria":categoria,
                "premio":premio
            })

            num_acertados = [] # reset
            
    with open('csv/resultadoApostas.csv', "a", newline="", encoding="utf-8") as arquivo: # Guarda os resultados adiquiridos no arquivo csv
        escritor = csv.writer(arquivo)
        for usu in resultados:
            
            if usu["categoria"] != "n/a": 
                usu["premio"] = premiosCategoria[usu["categoria"]] // qntCategoria[usu["categoria"]] # Divisão proporcional do prêmio, pela categoria

            resultadoToCsv = usu.values() # Pega o resultado final do usuário
            escritor.writerow(resultadoToCsv)

def configuar_EStrutura_CSV(limite):#DEIXA A ESTRUTURA DO CSV PRONTA
    colunasApostas = ["Usuarios"] + [f"N{x}°" for x in range(1,limite + 1)] # Cabeçalho das apostas
    
    with open('csv/apostas.csv', 'w', newline='', encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(colunasApostas) # reset no aquivo
        
    colunasResultado = ["Usuarios", "Quantidade de Acrtos", "Numeros Acertados", "Categoria", "Prêmio"] # Cabeçalho dos resultados
    
    with open('csv/resultadoApostas.csv', "w", newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(colunasResultado) # reset no aquivo

def guardarAposta(aposta): #GUARDA OS VALORES APOSTADOS NO ARQUIVO CSV, APÓS SEREM CONVERTIDOS PARA STRING
    with open("csv/apostas.csv", "a", newline="", encoding="utf-8") as arquivo:
        write = csv.writer(arquivo)
        write.writerow(aposta) # Guarda a aposta no arquivo csv

def demonstracao():
    listaNomes,numerosApostados,dicioAposta=[],[],{}

    numerosSorteados=funcoes.sortearNumeros(6)#adiciona lista dos numeros sorteados
    listaSorteados = [int(numero) for sublista in numerosSorteados for numero in sublista]

    for aposta in range(4):
        numerosApostados+=[random.sample(range(1,30),6)]#sorteia numeros unicos para as apostas
    
    with open("csv/nomes.csv", "r", newline="", encoding="utf-8") as arquivo:#lê nomes.csv e sorteia 4 aleatorios
        leitor = csv.reader(arquivo)
        for nome in leitor:
            if nome:
                listaNomes.append(nome[0])#se a linha não estiver vazia
        listaNomes=random.sample(listaNomes,4)

        for aposta in range(4):
            dicioAposta[listaNomes[aposta]]=numerosApostados[aposta]#dicionario recebe chave e valor pelas listas
    
    with open("csv/apostas.csv", "w", newline="", encoding="utf-8") as arquivo: #escrever no arquivo aposta o dicionario
        escritor = csv.writer(arquivo)
        escritor.writerow(["Usuarios", "N1", "N2", "N3", "N4", "N5", "N6"])
        for chave, valor in dicioAposta.items():
            escritor.writerow([chave, *valor])

    num_acertados,resultados = [],[]   
    premiosCategoria = {"sena":1000000,"quinta":500000,"quarta":350000} # Atribui o valor total para cada categoria
    qntCategoria = {"sena":0,"quinta":0,"quarta":0} # Quantidade de cada categoria [será alterado]

    with open('csv/apostas.csv', "r", encoding="utf-8") as arquivo: # Lê arquivo das apostas
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            usuarios = linha.get("Usuarios")
            quantidadeAcertos = 0
            categoria = "n/a" 
            premio = 0 

            for chave in linha: # Verifica números acertados               
                if chave != "Usuarios":
                    if int(linha[chave]) in listaSorteados:
                        quantidadeAcertos += 1
                        num_acertados.append(int(linha[chave]))
                        
            match quantidadeAcertos: # Verifica qual categoria
                case 6:
                    categoria = "sena"
                case 5:
                    categoria = "quinta"
                case 4:
                    categoria = "quarta" 

            if categoria != "n/a":
                qntCategoria[categoria] += 1 # Altera a contagem de cada categoria

            resultados.append({ # Guarda todos os resultados
                "usuario":usuarios,
                "quantidadeAcertos":quantidadeAcertos,
                "num_acertados":num_acertados,
                "categoria":categoria,
                "premio":premio
            })

            num_acertados = [] # reset
            
    with open('csv/resultadoApostas.csv', "w", newline="", encoding="utf-8") as arquivo: # Guarda os resultados adiquiridos no arquivo csv
        escritor = csv.writer(arquivo)
        escritor.writerow(["Usuarios", "Quantidade de Acrtos", "Numeros Acertados", "Categoria", "Prêmio"])
        for usu in resultados:           
            if usu["categoria"] != "n/a": 
                usu["premio"] = premiosCategoria[usu["categoria"]] // qntCategoria[usu["categoria"]] # Divisão proporcional do prêmio, pela categoria
            resultadoToCsv = usu.values() # Pega o resultado final do usuário
            escritor.writerow(resultadoToCsv)

             
             
       