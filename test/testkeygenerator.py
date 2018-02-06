import unittest
import sys 
import os

sys.path.append(os.path.abspath("../src"))
from keygenerator import PseudorandomKey

class TestPseudorandomKey(unittest.TestCase):
    def test_generate_zero(self):
        with self.assertRaises(Exception):
            PseudorandomKey.generate(0)

    def test_generate_negative(self):
        with self.assertRaises(Exception):
            PseudorandomKey.generate(-1)

    def test_generate_bits(self):
        self.assertEqual(len(PseudorandomKey.generate(8)), 8)

    def test_generate_bytes(self):
        self.assertEqual(len(PseudorandomKey.generate(8, True)), 64)


if (__name__ == "__main__"):
    unittest.main()

