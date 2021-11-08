class Pessoa:
    olhos=2

    def __init__(self, *filhos, nome=None, idade=23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__=='__main__':
    martinho = Mutante(nome='Martinho')
    rennan = Homem(martinho, nome='Rennan')

    print(Pessoa.cumprimentar(rennan))
    print(id(rennan))
    print(rennan.cumprimentar())
    print(rennan.nome)
    print(rennan.idade)
    for filho in rennan.filhos:
        print(filho.nome)
    rennan.sobrenome = 'Lima'
    del rennan.filhos
    rennan.olhos = 1
    del rennan.olhos
    print(rennan.__dict__)
    print(martinho.__dict__)
    print(Pessoa.olhos)
    print(rennan.olhos)
    print(id(Pessoa.olhos), id(rennan.olhos))
    print(Pessoa.metodo_estatico(), rennan.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), rennan.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(rennan, Pessoa))
    print(isinstance(rennan, Homem))
    print(martinho.olhos)
    print(rennan.cumprimentar())
    print(martinho.cumprimentar())
