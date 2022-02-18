"""
As regras são as seguintes:

O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.

1. Pedra empata com Pedra e ganha de Tesoura
2. Tesoura empata com Tesoura e ganha de Papel
3. Papel empata com Papel e ganha de Pedra
"""


def jokenpo(jogador_1, jogador_2):
    opções = ('pedra', 'papel', 'tesoura')
    if jogador_1 not in opções or jogador_2 not in opções:
        return 'As opções são Pedra, papel ou tesoura. Tente novamente!'

    if (jogador_1 == 'papel' and jogador_2 == 'pedra') or (jogador_1 == 'tesoura' and jogador_2 == 'papel') or (jogador_1 == 'pedra' and jogador_2 == 'tesoura'):
        return 'Vencedor Jogador 1!'
    if (jogador_1 == 'papel' and jogador_2 == 'tesoura') or (jogador_1 == 'pedra' and jogador_2 == 'papel') or (jogador_1 == 'tesoura' and jogador_2 == 'pedra'):
        return 'Vencedor Jogador 2'
    if jogador_1 == jogador_2:
        return 'Empate'


