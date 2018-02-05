import random

class otp:
    def __init__(self):
        random.seed()

    def generateKey(self, bitSize):
        if (bitSize <= 0):
            raise Exception("Invalid key size, number of bits must be greater than zero")

        key = ""
        for i in range(0, bitSize):
            key += str(random.randint(0,1))

        return key

    def encrypt(self, plaintext, key):
        size = len(plaintext)
        keyBytes = self.keyToBytes(key, size)

        cyphertext = ""
        for i in range(0, size):
            byte = ord(plaintext[i])
            cyphertext += chr(byte ^ keyBytes[i])

        return cyphertext

    def decrypt(self, cyphertext, key):
        size = len(cyphertext)
        keyBytes = self.keyToBytes(key, size)

        plaintext = ""
        for i in range(0, size):
            byte = ord(cyphertext[i])
            plaintext += chr(byte ^ keyBytes[i])

        return plaintext

    def keyToBytes(self, key, byteSize):
        if (not isinstance(key, str)):
            raise TypeError("Unexpected key type, expected 'string'")

        # Remove whitespace from key and get size
        key = key.strip()
        keySize = len(key)

        # Check length of the key
        if (keySize % 8 != 0):
            raise Exception("Invalid key length, cannot convert to byte array")
        elif (keySize != byteSize * 8):
            raise Exception("Invalid key length")

        # Convert the binary key string to byte array
        keyBytes = []
        for i in range(0, byteSize):
            byte = key[i*8:i*8+8]
            keyBytes.append(int(byte, 2))
        
        return keyBytes
