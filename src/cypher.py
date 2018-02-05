import random

class otp:

    # ctor : Creates a new instance of the  One Time Pad cypher.
    def __init__(self):
        random.seed()

    # generateKey : Randomly generates a secret key that can be used to 
    # encrypt/decrypt messages.
    # @param bitSize : The number of bits the key should contain. Must be
    # greater than zero. 
    # @return : The generated key as binary string.
    # @raises Exception : The bitSize is less than or equal to zero. 
    def generateKey(self, bitSize):
        if (bitSize <= 0):
            raise Exception("Invalid key size, number of bits must be greater than zero")

        key = ""
        for i in range(0, bitSize):
            key += str(random.randint(0,1))

        return key

    # encrypt : Encrypts the supplied plaintext using the given key.
    # @param plaintext : The string message to be encrypted.
    # @param key : The key used to encrypt the message.
    # @return : The encrypted cyphertext.
    # @raises Exception : The binary length of the key and plaintext 
    # don't match. 
    def encrypt(self, plaintext, key):
        return self.cypher(plaintext, key)

    # decrypt : Decrypts the supplied cyphertext using the given key.
    # @param cyphertext : The encrypted string that will be decrypted.
    # @param key : The key used to decrypt the message.
    # @return : The decrypted plaintext.
    # @raises Exception : The binary length of the key and cyphertext 
    # don't match. 
    def decrypt(self, cyphertext, key):
        return self.cypher(cyphertext, key)

    # cypher : Encrypts or decrypts the supplied message using the given key.
    # @param msg : The message that will be encrypted/decrypted
    # @param key : The key used to translate the message.
    # @return : The resulting message after encrypted/decrypted.
    # @raises Exception : The binary length of the key and message 
    # don't match.
    def cypher(self, msg, key):
        size = len(msg)
        if (len(key) != size * 8):
            raise Exception("Invalid key length")

        keyBytes = self.keyToBytes(key)
        res = ""
        for i in range(0, size):
            byte = ord(msg[i])
            res += chr(byte ^ keyBytes[i])

        return res

    # keyToBytes : Converts a binary string to an array of bytes.
    # @param key : The binary string key to be converted to byte array.
    # @return : The byte array representation of the provided key. 
    def keyToBytes(self, key):
        if (not isinstance(key, str)):
            raise TypeError("Unexpected key type, expected 'str'")

        # Remove whitespace from key and get size
        key = key.strip()
        keySize = len(key)

        # Check length of the key
        if (keySize % 8 != 0):
            raise Exception("Invalid key length, cannot convert to byte array")

        # Convert the binary key string to byte array
        keyBytes = []
        for i in range(0, int(keySize / 8)):
            byte = key[i*8:i*8+8]
            keyBytes.append(int(byte, 2))
        
        return keyBytes
