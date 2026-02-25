class Professor:
    
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina
        
    def lecionar(self):
        return(f"Nome do professor: {self.nome}, Disciplina que o professor ministra: {self.disciplina}")
    
professor1 = Professor("Jonas", "História")
print(professor1.lecionar())
    