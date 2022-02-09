"""
As regras são as seguintes:

O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.

1. Pedra empata com Pedra e ganha de Tesoura
2. Tesoura empata com Tesoura e ganha de Papel
3. Papel empata com Papel e ganha de Pedra
"""


def jokenpo(opção_1, opção_2):
    if (opção_1 == 'papel' and opção_2 == 'pedra') or (opção_1 == 'tesoura' and opção_2 == 'papel') or (opção_1 == 'pedra' and opção_2 == 'tesoura'):
        return 'Ganhou'
    if (opção_1 == 'papel' and opção_2 == 'papel') or (opção_1 == 'tesoura' and opção_2 == 'tesoura') or (opção_1 == 'pedra' and opção_2 == 'pedra'):
        return 'Empate'
    if (opção_1 == 'papel' and opção_2 == 'tesoura') or (opção_1 == 'pedra' and opção_2 == 'papel') or (opção_1 == 'tesoura' and opção_2 == 'pedra'):
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
