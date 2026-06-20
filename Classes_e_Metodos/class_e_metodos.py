
class computador:
    
    def __init__(self, marca, memoria_RAM, placa_de_video):
        self.marca = marca
        self.memoria_RAM = memoria_RAM
        self.placa_de_video = placa_de_video
        
    def ligar(self):
        print('Ligando')
        
    def desligar(self):
        print('Desligando')
        
    def ExibirInformacoes(self):
            print(self.marca, self.memoria_RAM, self.placa_de_video)
    
computador1 = computador("asus", "16gb", "intelGrapigh")
computador2 = computador('Sansung', '8gb', 'rx580')
computador3 = computador('Mecbook', '22gb', 'ephol23gf')

print(computador1.marca, computador1.memoria_RAM, computador1.placa_de_video)
print(computador2.marca, computador2.memoria_RAM, computador2.placa_de_video)
print(computador3.marca, computador3.memoria_RAM, computador3.placa_de_video)

print()
computador1.ligar()
computador1.desligar()
computador1.ExibirInformacoes()
computador2.ExibirInformacoes()