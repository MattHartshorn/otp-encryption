import unittest
import sys 
import os

sys.path.append(os.path.abspath("../src"))
import cypher

class TestCypher(unittest.TestCase):
    def test_genKey_zero(self):
        otp = cypher.otp()
        with self.assertRaises(Exception):
            otp.generateKey(0)

    def test_genKey_negative(self):
        otp = cypher.otp()
        with self.assertRaises(Exception):
            otp.generateKey(-1)

    def test_genKey_length(self):
        otp = cypher.otp()
        self.assertEqual(len(otp.generateKey(8)), 8)


    def test_keyToBytes(self):
        otp = cypher.otp()
        key = otp.generateKey(16)
        self.assertEqual(len(otp.keyToBytes(key)), 2)

    def test_keyToBytes_invalidSize_bits(self):
        otp = cypher.otp()
        key = otp.generateKey(14)
        with self.assertRaises(Exception):
            otp.keyToBytes(key)

    def test_keyToBytes_type(self):
        otp = cypher.otp()
        key = 36
        with self.assertRaises(TypeError):
            otp.keyToBytes(key)

    def test_keyToBytes_nonBinary(self):
        otp = cypher.otp()
        key = "01011001g0100101"
        with self.assertRaises(Exception):
            otp.keyToBytes(key)


    def test_encrypt_length(self):
        otp = cypher.otp()
        key =  otp.generateKey(208)
        plaintext = "abcdefghijklmnopqrstuvwxyz"
        cyphertext = otp.encrypt(plaintext, key)
        self.assertEqual(len(cyphertext), len(plaintext))

    def test_encrypt_equality(self):
        otp = cypher.otp()
        key = otp.generateKey(208)
        plaintext = "abcdefghijklmnopqrstuvwxyz"
        cyphertext = otp.encrypt(plaintext, key)
        self.assertNotEqual(cyphertext, plaintext)

    def test_encrypt_invalidLength(self):
        otp = cypher.otp()
        key = otp.generateKey(210)
        plaintext = "abcdefghijklmnopqrstuvwxyz"
        with self.assertRaises(Exception):
            cyphertext = otp.encrypt(plaintext, key)

    def test_decrypt_equality(self):
        otp = cypher.otp()
        key = otp.generateKey(208)
        plaintext = "abcdefghijklmnopqrstuvwxyz"
        cyphertext = otp.encrypt(plaintext, key)
        decrypted = otp.decrypt(cyphertext, key)
        self.assertEqual(decrypted, plaintext)

    def test_decrypt_invalidLength(self):
        otp = cypher.otp()
        key = otp.generateKey(210)
        cyphertext = "abcdefghijklmnopqrstuvwxyz"
        with self.assertRaises(Exception):
            plaintext = otp.decrypt(cyphertext, key)

    def test_decrypt_invalidKey(self):
        otp = cypher.otp()
        key = otp.generateKey(208)
        plaintext = "abcdefghijklmnopqrstuvwxyz"
        cyphertext = otp.encrypt(plaintext, key)
        
        key = otp.generateKey(208)
        decrypted = otp.decrypt(cyphertext, key)
        self.assertNotEqual(decrypted, plaintext)

    

if (__name__ == "__main__"):
    unittest.main()

