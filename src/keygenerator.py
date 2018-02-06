import random

class PseudorandomKey:
    seeded = False

    # generate : Randomly generates a binary string key that can be used for encryption.
    # @param size : The number of bits or bytes the key should contain.
    # @param bytes : The input size will be in bit if True, otherwise in bytes.
    # @return : The generated key as binary string.
    # @raises Exception : The size is less than one. 
    @classmethod
    def generate(cls, size, bytes = False):
        if (size <= 0): raise Exception("Invalid key size, number of bits must be greater than zero")

        if (not cls.seeded): cls.seed()

        if (bytes): size *= 8
        return "".join([str(random.randint(0,1)) for i in range(0, size)])

    # seed : Seeds the random number generator
    # @param seed : Value to seed the generator with
    @classmethod
    def seed(cls, seed = None):
        if (seed == None):
            random.seed()
        else:
            random.seed(seed)
        
        cls.seeded = True