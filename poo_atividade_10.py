class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
        
    def mostrar_dados(self):
         return(f"Marca: {self.marca}, Ano: {self.ano}")
    
    def calcular_idade(self):
        ano_atual = 2026
        idade = ano_atual - self.ano
        print(f"A idade: {idade} anos")
    
carro1 = Carro("Fusca", 1984)
carro1.calcular_idade()
print(carro1.mostrar_dados())