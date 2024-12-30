# class - Classes sao moldes para criar novos objetos
# As classes geram novos objetos (instancias) que
# podem ter seus proprios atributos e metodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar varias acoes.
# Por convencao, usamos PascalCase para nomes de classes.
# string = 'Luiz' #str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa: 
    def __init__(self, nome, sobrenome):
        self.nome = nome 
        self.sobrenome = sobrenome

p1 = Pessoa('Luiz', 'otavio')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otavio'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)