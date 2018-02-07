import unittest
import sys 
import os

sys.path.append(os.path.abspath("../src"))
import keygenerator
from helper import binStrToBytes

class TestHelper(unittest.TestCase):
    def test_binStrToBytes(self):
        key = keygenerator.generate(8, True)
        self.assertEqual(len(binStrToBytes(key)), 8)

    def test_binStrToBytes_invalidSize_bits(self):
        key = keygenerator.generate(14)
        with self.assertRaises(Exception):
            binStrToBytes(key)

    def test_binStrToBytes_type(self):
        key = 36
        with self.assertRaises(TypeError):
            binStrToBytes(key)

    def test_binStrToBytes_nonBinary(self):
        key = "01011001g0100101"
        with self.assertRaises(Exception):
            binStrToBytes(key)


if (__name__ == "__main__"):
    unittest.main()

