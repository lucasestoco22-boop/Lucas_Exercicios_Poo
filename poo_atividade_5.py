class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def detalhes(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas} ")
        
    def longo(self):
        if self.paginas > 300:
           return(True)
        else:
            return(False)

livro1 = Livro("A bibilioteca da meia-noite", "Sarah Larson", 350) 
livro1.detalhes()
print(livro1.longo())
           