import unittest
from controle_trem import Trem

class TestTrem(unittest.TestCase):
    def test_mover_direita(self):
        trem = Trem()
        trem.mover("DIREITA")
        self.assertEqual(trem.obter_posicao(), 1)

    def test_mover_esquerda(self):
        trem = Trem()
        trem.mover("ESQUERDA")
        self.assertEqual(trem.obter_posicao(), -1)

    def test_limite_movimentos(self):
        trem = Trem()
        comandos = ["DIREITA"] * 51
        trem.executar_comandos(comandos)
        self.assertEqual(trem.obter_posicao(), 50)

    def test_limite_movimentos_consecutivos(self):
        trem = Trem()
        comandos = ["DIREITA"] * 21
        trem.executar_comandos(comandos)
        self.assertEqual(trem.obter_posicao(), 20)

if __name__ == '__main__':
    unittest.main()
