class Filme:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao
        
    def longo(self):
        (print(f"Titulo: {self.titulo}, Duração: {self.duracao}min"))
        
    def eh_longo(self):
        if self.duracao > 120:
            return(True)
        else:
            return(False)
 
    
filme1 = Filme("Queer", 145)
filme1.longo()
print(filme1.eh_longo())