import random

seeded = False

def generate(size, bytes = False):
    """ Randomly generates a binary string key that can used for encryption

    Arguments:
    size -- The number of bits or bytes the key should contain
    bytes -- The input size will be in bits if True, otherwise in bytes
    
    Returns:
    The generated key as a binary string

    Raises:
    Exception -- The size is less than one 
    """
    if (size <= 0): raise Exception("Invalid key size, number of bits must be greater than zero")

    if (not seeded): seed()

    if (bytes): size *= 8
    return "".join([str(random.randint(0,1)) for i in range(0, size)])

def seed(seed = None):
    """ Seeds the random number generator

    Arguments:
    seed -- value to see the generator with 
    """
    if (seed == None):
        random.seed()
    else:
        random.seed(seed)
    
    seeded = True