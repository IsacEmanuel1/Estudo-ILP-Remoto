class MeuErro(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        