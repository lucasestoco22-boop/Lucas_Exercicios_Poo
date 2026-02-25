class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def aniversario(self):
        self.idade += 1
        
    def mensagem(self):
        return(f"{self.nome}, É uma pessoa que tem: {self.idade} anos de idade")
        
pessoa1 = Pessoa("Lucas", 19)
pessoa1.aniversario()
print(pessoa1.mensagem())