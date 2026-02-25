
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def aplicar_desconto(self, percentual):
        print(f"O preço inicial: {self.preco}")
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto
    
    def mostrar(self):
        return(f"Nome: {self.nome}, Preço com desconto: R${self.preco}")        
    
produto1 = Produto("Tablet", 1999)
produto1.aplicar_desconto(20)
print(produto1.mostrar())

