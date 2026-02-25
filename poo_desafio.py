class Aluno:
    def __init__(self, nome, nota1, nota2, media):
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

class Professor:
    
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina
        
    def lecionar(self):
        return(f"Nome do professor: {self.nome}, Disciplina que o professor ministra: {self.disciplina}")
    
professor1 = Professor("Jonas", "História")
print(professor1.lecionar())
    
class Turma:
    def __init__(self, alunos):
        self_alunos = []
        
    def adicionar_alunos(self, nome):
        self.alunos.append(nome)
        
    def listar_alunos(self):
        print("Listas de alunos: ")
        print(self.alunos)
        
turma1 = Turma()
turma1.adicionar_alunos("Lucas")
turma1.adicionar_alunos("Maria")
turma1.adicionar_alunos("João")
turma1.listar_alunos()