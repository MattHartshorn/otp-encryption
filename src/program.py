import cypher
import sys


class program:  
    def __init__(self):
        self.otp = cypher.otp()

    def run(self, args):
        if (len(args) < 2):
            self.error("Missing function to execute", True)

        funcName = args[1].lower()
        func = None
        argCount = 3

        # Determine which function to run
        if(funcName == "enc"):
            func = self.enc
        elif(funcName == "dec"):
            func = self.dec
        elif(funcName == "keygen"):
            func = self.keygen
            argCount = 2
        elif(funcName == "keyhisto"):
            func = self.keyhisto
        else:
            self.error("Unknown function specified: '{0}'".format(funcName), True)

        self.execute(args[2:], func, argCount)
        
    def usage(self):
        print(self.readFile("../docs/usage.txt"))

    def execute(self, args, func, argCount):
        if (len(args) < argCount):
            self.error("Missing Arguments", True)
        else:
            func(*args[:argCount])

    def enc(self, keyFile, plaintextFile, cyphertextFile):
        self.cypher(keyFile, plaintextFile, cyphertextFile, True)

    def dec(self, keyFile, cyphertextFile, resultFile):
        self.cypher(keyFile, cyphertextFile, resultFile, False)
    
    def cypher(self, keyFile, inputFile, outputFile, encrypt):
        try:             
            res = ""
            try:
                key = self.readFile(keyFile)
                msg = self.readFile(inputFile)
                if (encrypt):
                    res = self.otp.encrypt(msg, key)
                else:
                    res = self.otp.decrypt(msg, key)
            except Exception as e:
                self.writeFile("", outputFile)
                self.error(e)
                
            self.writeFile(res, outputFile)
                
        except IOError as e:
            self.error(e)

    def keygen(self, keySize, outputFile):
        try:
            key = ""
            try:
                size = int(keySize)
                if (size < 1 or size > 128):
                    self.error("Key size out of range, valid range is [1, 128]")

                key += self.otp.generateKey(size)
            except Exception as e:
                self.writeFile("", outputFile)
                self.error(e)
            
            self.writeFile(key, outputFile)
            
        except IOError as e:
            self.error(e)

    def keyhisto(self, keySize, keyCount, outputFile):
        try:
            # Convert and validate input
            size = int(keySize)
            count = int(keyCount)

            if (count <= 0):
                self.error("Invalid key count, must be greater than zero")
            if (size < 1 or size > 128):
                self.error("Key size out of range, valid range is [1, 128]")

            # Generate the specified number of keys
            keys = {}
            for i in range(0, count):
                key = self.otp.generateKey(size)
                if (key in keys):
                    keys[key] += 1
                else:
                    keys[key] = 1

            # Write all the keys and their count to the file
            with open(outputFile, 'w') as fs:
                fs.write("Key,Count\n")
                for key in keys:
                    fs.write("'{0}',{1}\n".format(key, keys[key]))
            
        except Exception as e:
            self.error(e)

    def readFile(self, filename):
        with open(filename, 'rb') as fs:
            return fs.read().decode("utf-8")
        
        return ""

    def writeFile(self, content, filename):
        with open(filename, 'wb') as fs:
            return fs.write(content.encode("utf-8"))
    
    def error(self, msg, printUsage = False):
        print("error: {0}".format(msg))
        if (printUsage):
            print("")
            self.usage()
        sys.exit()