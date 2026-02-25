class Animal:
    def __ini__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        
    def informacao(self):
        return(f"{self.nome}, é um(a) {self.especie}")
    
animal1 = Animal("Gato", "Persa" )
print(animal1.informacao())
