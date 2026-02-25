class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def latir(self):
        return(f"{self.nome}, disse: auau/ Ele tem: {self.idade} anos")
    
cachorro1 = Cachorro("Mel", 8)
cachorro2 = Cachorro("Malu", 6)
print(cachorro1.latir())
print(cachorro2.latir())

