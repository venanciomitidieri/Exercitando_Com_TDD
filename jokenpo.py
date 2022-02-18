"""
As regras são as seguintes:

O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.

1. Pedra empata com Pedra e ganha de Tesoura
2. Tesoura empata com Tesoura e ganha de Papel
3. Papel empata com Papel e ganha de Pedra
"""
from random import randint


def gerar_jogadas():
    total = 0
    while total <= 1:
        jogadas = ('pedra', 'papel', 'tesoura')
        jogada_1 = jogadas[randint(0, 2)]
        jogada_2 = jogadas[randint(0, 2)]
        total += 1
        return jogada_1, jogada_2


jogador_1 = gerar_jogadas()[0]
jogador_2 = gerar_jogadas()[1]


def jokenpo(jogador_1, jogador_2):
    if (jogador_1 == 'papel' and jogador_2 == 'pedra') or (jogador_1 == 'tesoura' and jogador_2 == 'papel') or (jogador_1 == 'pedra' and jogador_2 == 'tesoura'):
        return 'Ganhou'
    if (jogador_1 == 'papel' and jogador_2 == 'papel') or (jogador_1 == 'tesoura' and jogador_2 == 'tesoura') or (jogador_1 == 'pedra' and jogador_2 == 'pedra'):
        return 'Empate'
    if (jogador_1 == 'papel' and jogador_2 == 'tesoura') or (jogador_1 == 'pedra' and jogador_2 == 'papel') or (jogador_1 == 'tesoura' and jogador_2 == 'pedra'):
        return 'Perdeu'


if __name__ == '__main__':
    assert jokenpo('pedra', 'pedra') == 'Empate'
    assert jokenpo('pedra', 'papel') == 'Perdeu'
    assert jokenpo('pedra', 'tesoura') == 'Ganhou'

    assert jokenpo('tesoura', 'tesoura') == 'Empate'
    assert jokenpo('tesoura', 'pedra') == 'Perdeu'
    assert jokenpo('tesoura', 'papel') == 'Ganhou'

    assert jokenpo('papel', 'papel') == 'Empate'
    assert jokenpo('papel', 'tesoura') == 'Perdeu'
    assert jokenpo('papel', 'pedra') == 'Ganhou'
