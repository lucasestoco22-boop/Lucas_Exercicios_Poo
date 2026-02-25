
#Exercício 2
media = 0
class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = media
        
    def calcular_media(self):
     return(self.nota1 + self.nota2)/2
        
    def situacao(self, media):
        if media >= 7:
            return("Aprovado")
        else:
            return("Reprovado")
    
    def exibir(self):
        return(f"Nome: {self.nome}, Nota1: {self.nota1}, Nota2: {self.nota2}, Média: {self.media}")
aluno1 = Aluno("Maria", 7, 10)
aluno1.calcular_media(7,10)
print(aluno1.exibir())        