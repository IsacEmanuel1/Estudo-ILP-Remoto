#Declaração de Classes
class Gafanhoto:
    """
Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
Para cira uma nova pessoa, use
variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "", idade = 0): # Metodo construtor
        #Atributos de instacias
        self.nome = nome
        self.idade = idade
    
    
    #Métodos de instância
    def aniversario(self):
        self.idade += 1
        
    def __str__(self): # Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"
    
    
    
#Declaração de objetos
g1 = Gafanhoto("isac", 19)
g1.aniversario()
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__str__())

print(g1.__doc__)

g2 = Gafanhoto("vitoria", 24)
g2.aniversario()

print(g2.__str__())
print(g2.__getstate__())

