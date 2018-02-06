import random

class OtpCypher:
    # encrypt : Encrypts the supplied plaintext using the given key.
    # @param plaintext : The string message to be encrypted.
    # @param key : The key, byte array, used to encrypt the message.
    # @return : The encrypted cyphertext.
    # @raises Exception : The binary length of the key and plaintext 
    # don't match. 
    @classmethod
    def encrypt(cls, plaintext, key):
        return cls.cypher(plaintext, key)

    # decrypt : Decrypts the supplied cyphertext using the given key.
    # @param cyphertext : The encrypted string that will be decrypted.
    # @param key : The key, byte array, used to decrypt the message.
    # @return : The decrypted plaintext.
    # @raises Exception : The binary length of the key and cyphertext 
    # don't match. 
    @classmethod
    def decrypt(cls, cyphertext, key):
        return cls.cypher(cyphertext, key)

    # cypher : Encrypts or decrypts the supplied message using the given key.
    # @param msg : The message that will be encrypted/decrypted
    # @param key : The key, byte array, used to translate the message.
    # @return : The resulting message after encrypted/decrypted.
    # @raises Exception : The binary length of the key and message 
    # don't match.
    @classmethod
    def cypher(cls, msg, key):
        size = len(msg)
        if (len(key) != size): raise Exception("Invalid key length")

        return "".join([chr(ord(msg[i]) ^ key[i]) for i in range(0, size)])