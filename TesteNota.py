import unittest
from Nota import Nota

class TesteNota(unittest.TestCase):

    def test_nota(self):
        self.nova_nota = Nota
        self.assertTrue(Nota(10, 6))


if __name__ == "__main__":
    unittest.main()