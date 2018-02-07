def encrypt(plaintext, key):
    """ Encrypts the supplied plaintext using the given key.
    Arguments:
    plaintext -- The string message to be encrypted.
    key -- The key, byte array, used to encrypt the message.

    Returns:
    The encrypted message.
    """
    return cypher(plaintext, key)


def decrypt(cyphertext, key):
    """ Decrypts the supplied plaintext using the given key.
    Arguments:
    cyphertext -- The string message to be decrypted.
    key -- The key, byte array, used to decrypt the message.

    Returns:
    The decrypted message.
    """
    return cypher(cyphertext, key)


def cypher(msg, key):
    """ Encrypts or decyrpts the supplied plaintext using the given key.
    Arguments:
    msg -- The string message to be passed throught the cypher.
    key -- The key, byte array, used to encrypt/decrypt the message.

    Returns:
    The encrypted message.
    
    Raises:
    Exception -- The binary length of the key and message don't match. 
    """
    size = len(msg)
    if (len(key) != size): raise Exception("Invalid key length")

    return "".join([chr(ord(msg[i]) ^ key[i]) for i in range(0, size)])