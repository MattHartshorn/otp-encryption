# binStrToBytes : Converts a binary string to an array of bytes.
# @param bin : The binary string to be converted to byte array.
# @return : The byte array representation of the provided binary string. 
def binStrToBytes(bin):
    if (not isinstance(bin, str)):
        raise TypeError("Unexpected type, expected 'str'")

    # Remove whitespace from key and get size
    bin = bin.replace(" ", "")
    size = len(bin)

    # Check length of the key
    if (size % 8 != 0):
        raise Exception("Invalid length, cannot convert to byte array")

    # Convert the binary key string to byte array
    return bytes([int(bin[i:i+8], 2) for i in range(0, size, 8)])

