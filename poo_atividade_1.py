
def lin():
    print("-" * 40)

#Exercício 1
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.valor += valor
        
    def exibir_saldo(self):
        return (f"Titular: {self.titular}, Saldo: R${self.saldo}")    
conta1 = ContaBancaria("Lucas", 300)
conta1.depositar(200)
print(conta1.exibir_saldo())

lin()

