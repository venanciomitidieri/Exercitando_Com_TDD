import unittest
from PedraPapelTesoura.jokenpo import jokenpo


class TestRPS(unittest.TestCase):
    def teste_entrada_quando_nao_for_pedra_papel_tesoura(self):
        self.assertEqual(jokenpo('computer', 'paper'), 'As opções são Pedra, papel ou tesoura. Tente novamente!')

    def entrada_teste_nao_deve_estar_vazia(self):
        self.assertEqual(jokenpo('paper', ''), 'As opções são Pedra, papel ou tesoura. Tente novamente!')

    def teste_empate_quando_a_eh_igual_b(self):
        self.assertEqual(jokenpo('papel', 'papel'), 'Empate')

    def teste_entrada_pedra_papel_tesoura(self):
        self.assertNotEqual(jokenpo('papel', 'tesoura'), 'As opções são Pedra, papel ou tesoura. Tente novamente!')

    def teste_se_papel_vs_pedra_vence(self):
        self.assertEqual(jokenpo('papel', 'pedra'), 'Vencedor Jogador 1!')

    def teste_se_pedra_vs_papel_vence(self):
        self.assertEqual(jokenpo('pedra', 'papel'), 'Vencedor Jogador 2!')

    def teste_se_papel_vs_tesoura_vence(self):
        self.assertEqual(jokenpo('papel', 'tesoura'), 'Vencedor Jogador 2!')

    def teste_se_tesoura_vs_papel_vence(self):
        self.assertEqual(jokenpo('tesoura', 'papel'), 'Vencedor Jogador 1!')

    def teste_se_pedra_vs_tesoura_vence(self):
        self.assertEqual(jokenpo('pedra', 'tesoura'), 'Vencedor Jogador 1!')

    def teste_se_tesoura_vs_pedra_vence(self):
        self.assertEqual(jokenpo('tesoura', 'pedra'), 'Vencedor Jogador 2!')