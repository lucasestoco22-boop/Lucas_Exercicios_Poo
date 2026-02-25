class Pessoa:
    def __init__(self, nome, idade, cidade, profissao):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.profissao = profissao
        
    def apresentar(self):
        return(f"Nome: {self.nome}/ Idade: {self.idade}/ Cidade: {self.cidade}/ Profissão: {self.profissao}")
    
    def feliz_aniversario(self):
        self.idade += 1
        
    def mensagem(self):
        return(f"{self.nome}, É uma pessoa que tem: {self.idade} anos de idade")
    
        
pessoa1 = Pessoa("Lucas", 19, "Vitória", "Psicólogo")
pessoa1.feliz_aniversario()
print(pessoa1.mensagem())
print(pessoa1.apresentar())