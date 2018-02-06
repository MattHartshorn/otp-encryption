import unittest
import sys 
import os

sys.path.append(os.path.abspath("../src"))
from cypher import OtpCypher
from helper import binStrToBytes
from keygenerator import PseudorandomKey

class TestCypher(unittest.TestCase):
    def test_encrypt_length(self):
        key = self.getKey()
        plaintext = "abcdefghijklmnopqrstuvwxyz"
        cyphertext = OtpCypher.encrypt(plaintext, key)
        self.assertEqual(len(cyphertext), len(plaintext))

    def test_encrypt_equality(self):
        key = self.getKey()
        plaintext = "abcdefghijklmnopqrstuvwxyz"
        cyphertext = OtpCypher.encrypt(plaintext, key)
        self.assertNotEqual(cyphertext, plaintext)

    def test_encrypt_invalidLength(self):
        key = self.getKey(25)
        plaintext = "abcdefghijklmnopqrstuvwxyz"
        with self.assertRaises(Exception):
            cyphertext = OtpCypher.encrypt(plaintext, key)


    def test_decrypt_equality(self):
        key = self.getKey()
        plaintext = "abcdefghijklmnopqrstuvwxyz"
        cyphertext = OtpCypher.encrypt(plaintext, key)
        decrypted = OtpCypher.decrypt(cyphertext, key)
        self.assertEqual(decrypted, plaintext)

    def test_decrypt_invalidLength(self):
        key = self.getKey(27)
        cyphertext = "abcdefghijklmnopqrstuvwxyz"
        with self.assertRaises(Exception):
            plaintext = OtpCypher.decrypt(cyphertext, key)

    def test_decrypt_invalidKey(self):
        key = self.getKey()
        plaintext = "abcdefghijklmnopqrstuvwxyz"
        cyphertext = OtpCypher.encrypt(plaintext, key)
        
        key = self.getKey()
        decrypted = OtpCypher.decrypt(cyphertext, key)
        self.assertNotEqual(decrypted, plaintext)

    def getKey(self, size = 26):
        return binStrToBytes(PseudorandomKey.generate(size, True))
    

if (__name__ == "__main__"):
    unittest.main()

