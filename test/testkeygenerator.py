import unittest
import sys 
import os

sys.path.append(os.path.abspath("../src"))
import keygenerator

class TestPseudorandomKey(unittest.TestCase):
    def test_generate_zero(self):
        with self.assertRaises(Exception):
            keygenerator.generate(0)

    def test_generate_negative(self):
        with self.assertRaises(Exception):
            keygenerator.generate(-1)

    def test_generate_bits(self):
        self.assertEqual(len(keygenerator.generate(8)), 8)

    def test_generate_bytes(self):
        self.assertEqual(len(keygenerator.generate(8, True)), 64)


if (__name__ == "__main__"):
    unittest.main()

