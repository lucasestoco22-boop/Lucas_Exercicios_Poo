class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def valor_total(self):
        print(f"Nome: {self.nome}, Preço: R${self.preco}")
        return self.preco * self.quantidade
    
produto1 = Produto("tupperware", 29.99, 100)
produto1.valor_total()
print(f"O valor total em estoque: R${produto1.valor_total():.2f}")