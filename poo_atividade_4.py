class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.velocidade = 0
    
    def acelerar(self, valor):
        print(f"Velocidade antes de aclerar: {self.velocidade}km/h")
        self.velocidade += valor
     
        
    def frear(self, valor):
        self.valor = valor
        self.velocidade -= valor
       
    def status(self):
        return(f"Modelo: {self.modelo}, Velocidade atual: {self.velocidade}km/h")

carro1 = Carro("BMW")
carro1.acelerar(100)
carro1.frear(20)
print(carro1.status())