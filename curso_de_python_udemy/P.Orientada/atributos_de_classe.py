#atributos de classe
#eu posso criar uma variavel constante para utilizar na minha classe e utilizar o Pessoa.ano_atual
#isso pode ser uma configuracao ou uma caracteristica constante da minha classe

class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Joao', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())