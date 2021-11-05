"""
Criar uma classe de Carro com dois atributos compostos pelas classes:

Motor
Direção

O motor controla a velocidade e tem os artibutos:
*Atributo de dado velocidade;
*Método acelerar, que incrementa a velocidade em uma unidade;
*Método frear, que decrementa em duas unidades;

A direção controla as direções com os atributos:
*Valor de direção: norte, sul, leste e oeste;
*Método girar à direita;
*Método girar à esquerda;

 N
O E
 S

    Exemplo:
    #Testando o motor
    >>>motor = Motor()
    >>>motor.velocidade
    0
    >>>motor.acelerar()
    >>>motor.velocidade
    1
    >>>motor.acelerar()
    >>>motor.velocidade
    2
    >>>motor.acelerar()
    >>>motor.velocidade
    3
    >>>motor.frear()
    >>>motor.velocidade
    1
    >>>motor.frear()
    >>>motor.velocidade
    0

    #Testando a direção:
    >>>direcao = Direcao()
    >>>direcao.valor()
    'Norte'
    >>>direcao.girar_a_direita()
    >>>direcao.valor()
    'Leste'
    >>>direcao.girar_a_direita()
    >>>direcao.valor()
    'Sul'
    >>>direcao.girar_a_direita()
    >>>direcao.valor()
    'Oeste'
    >>>direcao.girar_a_direita()
    >>>direcao.valor()
    'Norte'
    >>>direcao.girar_a_esquerda()
    >>>direcao.valor()
    'Oeste'
    >>>direcao.girar_a_esquerda()
    >>>direcao.valor()
    'Sul'
    >>>direcao.girar_a_esquerda()
    >>>direcao.valor()
    'Leste'
    >>>direcao.girar_a_esquerda()
    >>>direcao.valor()
    'Norte'

    >>>carro = Carro(direcao, motor)
    >>>carro.calcular_velocidade()
    0
    >>>carro.acelerar()
    >>>carro.calcular_velocidade()
    1
    >>>carro.acelerar()
    >>>carro.calcular_velocidade()
    2
    >>>carro.frear()
    >>>carro.calcular_velocidade()
    0
    >>>carro.calcular_direcao()
    'Norte'
    >>>carro.girar_a_direita()
    >>>carro.calcular_direcao()
    'Leste'
    >>>carro.girar_a_esquerda()
    >>>carro.calcular_direcao()
    'Norte'
    >>>carro.girar_a_esquerda()
    >>>carro.calcular_direcao()
    'Oeste'

"""

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:

    rotacao_a_direita_dct = {NORTE: LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE}
    rotacao_a_esquerda_dct = {NORTE:OESTE, OESTE:SUL, SUL:LESTE, LESTE:NORTE}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
       self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerdaa(self):
       self.valor = self.rotacao_a_esquerda_dct[self.valor]

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

