import unittest
from TrucoOTrato import trucoTrato
from TrucoOTrato import Niño
class PruebasTruco(unittest.TestCase):
    def test_trato(self):
        self.assertEqual(trucoTrato("trato", [Niño("Paco",9,160),Niño("Antonio",4,90)]),[5,5])

    def test_truco(self):
        self.assertEqual(trucoTrato("truco", [Niño("Paco",9,160),Niño("Antonio",4,90)]),[13,10])

    def test_fallos(self):
        self.assertEqual(trucoTrato("trato", [9,Niño("Antonio",4,90)]),"Si llegaste aqui feliz Halloween")
        self.assertEqual(trucoTrato("Patata", [Niño("Antonio",4,90)]),"Si llegaste aqui feliz Halloween")
        self.assertEqual(trucoTrato(9, [Niño("Antonio",4,90)]),"Si llegaste aqui feliz Halloween")

unittest.main()