from erros import QunatidadeApostasError, ValoresApostaIguaisError, ValorMaiorQueMaxError

def obter_quantidade_usuario(mensagem):
    while True:
        try:
            quantidade = int(input(mensagem))
            return quantidade
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def obter_valores_aposta(mensagem, nomeUsuario, limiteAposta, maxAposta):
    while True:
        try:
            valores_aposta = input(mensagem).split()
            valores_aposta_int = [int(x) for x in valores_aposta]

            for i in valores_aposta_int:
                if (i > maxAposta) or (i <= 0):
                    raise ValorMaiorQueMaxError
            if len(valores_aposta_int) != limiteAposta:
                raise QunatidadeApostasError
            elif len(set(valores_aposta_int)) < len(valores_aposta_int):
                raise ValoresApostaIguaisError
            else:
                usuario_aposta = [nomeUsuario] + valores_aposta_int
                return usuario_aposta
            
        
        except ValueError:
            print("Erro: Você digitou uma letra ou caractere inválido! Use apenas números inteiros.")
        except QunatidadeApostasError:
            print(f"\nAposta Inválida | Aposte em {limiteAposta} números \n")
        except ValoresApostaIguaisError:
            print("Aposta Inválida | Aposte em números diferentes \n")
        except ValorMaiorQueMaxError:
            print(f"Aposta Inválida | Aposte em números de 1-{maxAposta} \n")


if __name__ == '__main__':
    
    obter_valores_aposta("Digite seus numeros de aposta: ")