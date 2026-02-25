class jogo:
    def __init__(self, nome):
        self.nome = nome
        self.nivel = 1
        
    def subir_nivel(self):
        self.nivel += 1
    
    def exibir(self):
        return(f"Nível atual: {self.nivel}")

jogo1 = jogo("Mario")
jogo1.subir_nivel()
print(jogo1.exibir())