class Pessoa:
    olhos=2

    def __init__(self, *filhos, nome=None, idade=23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__=='__main__':
    martinho = Pessoa(nome='Martinho')
    rennan = Pessoa(martinho, nome='Rennan')

    print(Pessoa.cumprimentar(rennan))
    print(id(rennan))
    print(rennan.cumprimentar())
    print(rennan.nome)
    print(rennan.idade)
    for filho in rennan.filhos:
        print(filho.nome)
    rennan.sobrenome = 'Lima'
    del rennan.filhos
    print(rennan.__dict__)
    print(martinho.__dict__)
    print(Pessoa.olhos)
    print(rennan.olhos)
    print(id(Pessoa.olhos), id(rennan.olhos))
