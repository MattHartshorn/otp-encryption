import cypher
import sys


class program:  
    def __init__(self):
        self.otp = cypher.otp()

    def run(self, args):
        if (len(args) < 2):
            self.error("Missing function to execute")
            self.usage()
            return

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
            self.error("Unknown function specified: '" + funcName + "'")
            self.usage()
            return

        self.execute(args[2:], func, argCount)
        
    def usage(self):
        print(self.readFile("../docs/usage.txt"))

    def execute(self, args, func, argCount):
        if (len(args) < argCount):
            self.error("Missing Arguments")
            self.usage()
        else:
            func(*args[:argCount])

    def enc(self, keyFile, plaintextFile, cyphertextFile):
        try:             
            cyphertext = ""
            try:
                key = self.readFile(keyFile)
                plaintext = self.readFile(plaintextFile)
                cyphertext = self.otp.encrypt(plaintext, key)
            except Exception as e:
                self.error(str(e))
                self.writeFile("", cyphertextFile)
                return
                
            self.writeFile(cyphertext, cyphertextFile)
                
        except IOError as e:
            self.error(str(e))

    def dec(self, keyFile, cyphertextFile, resultFile):
        try:             
            resultText = ""
            try:
                key = self.readFile(keyFile)
                cyphertext = self.readFile(cyphertextFile)
                resultText = self.otp.decrypt(cyphertext, key)
            except Exception as e:
                self.error(str(e))
                self.writeFile("", resultFile)
                return
                
            self.writeFile(resultText, resultFile)
                
        except IOError as e:
            self.error(str(e))
    
    def keygen(self, keySize, outputFile):
        try:
            key = ""
            try:
                key += self.otp.generateKey(int(keySize))
            except Exception as e:
                self.error(str(e))
                self.writeFile("", outputFile)
                return
            
            self.writeFile(key, outputFile)
            
        except IOError as e:
            self.error(str(e))

    def keyhisto(self, keySize, keyCount, outputFile):
        try:
            # Convert and validate input
            size = int(keySize)
            count = int(keyCount)

            if (count <= 0):
                self.error("Invalid key count, must be greater than zero")
                return

            # Generate the specified number of keys
            keys = {}
            for i in range(0, count):
                key = self.otp.generateKey(int(keySize))
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
            self.error(str(e))

    def readFile(self, filename):
        with open(filename, 'rb') as fs:
            return fs.read().decode("utf-8")
        
        return ""

    def writeFile(self, content, filename):
        with open(filename, 'wb') as fs:
            return fs.write(content.encode("utf-8"))
    
    def error(self, msg):
        print("error: " + msg)