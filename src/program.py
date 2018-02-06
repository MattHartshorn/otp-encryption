from cypher import OtpCypher
from keygenerator import PseudorandomKey
import helper
import argparse
import sys
import actions

class Program:
    # Run execution
    @classmethod
    def run(cls, args = None):
        parser = cls.getParser()
        cls.executeCommands(parser, parser.parse_args())

    @classmethod
    def executeCommands(cls, parser, args):
        if (args.cmd == "enc" or args.cmd == "dec"):
            cls.cypher(args)
        elif (args.cmd == "keygen"):
            cls.keygen(args)
        else:
            parser.print_help()


    # Encrypt & decrypt methods
    @classmethod
    def cypher(cls, args):
        cls.cypher_validate_args(args)
        ofile = args.ofile[0] if isinstance(args.ofile, list) else args.ofile

        try:
            try:
                # Load data
                key = cls.cypher_loadkey(args)
                msg = cls.cypher_loadmsg(args)
                
                # Encrypt/decrypt
                output = OtpCypher.cypher(msg, key)
            except Exception as e:
                cls.cypher_write(args, "", ofile)
                cls.error(e)

            # Write data
            cls.cypher_write(args, output, ofile)
        except IOError as e:
            cls.error(e)

    @classmethod
    def cypher_validate_args(cls, args):
        requiredArgs = []
        if (args.key == None and args.keyOpt == None):
            requiredArgs.append("key")
        if (args.ifile == None and args.input == None and args.message == None):
            requiredArgs.append("ifile/message")
        if (len(requiredArgs) > 0):
            cls.error("the following arguments are required: {0}".format(", ".join(requiredArgs)))

    @classmethod
    def cypher_loadkey(cls, args):
        key = args.key if args.key != None else args.keyOpt[0]
        ktype = args.keytype if isinstance(args.keytype, str) else args.keytype[0]

        if (ktype == "text"):
            return helper.binStrToBytes(cls.read(key))
        elif (ktype == "raw"):
            return cls.read(key, False)
        elif (ktype == "string"):
            return helper.binStrToBytes(key)
        else:
            raise Exception("Unknown keyType: '{0}'".format(ktype))
            
    @classmethod
    def cypher_loadmsg(cls, args):
        filename = args.input[0] if args.input != None else args.ifile 
        if (filename == None):
            return args.message[0]
        else:
            return cls.read(filename)

    @classmethod
    def cypher_write(cls, args, output, filename):
        if (filename != None):
            cls.write(output, filename)
        elif (output != ""):
            print(output.encode("utf-8"))

    # Key gen methods
    @classmethod
    def keygen(cls, args):
        if (args.size < 1 or args.size > 128):
            cls.error("argument 'size' out of range: [0, 128]")

        ofile = args.output[0] if args.output != None else args.ofile
        try:
            try:
                # Generate key
                key = PseudorandomKey.generate(args.size, args.bytes)
            except Exception as e:
                cls.keygen_write(args, key, ofile)
                cls.error(e)

            cls.keygen_write(args, key, ofile)

        except IOError as e:
            cls.error(e)

    @classmethod
    def keygen_write(cls, args, key, filename):
        try:
            # Attempt to write the file
            if (filename != None):
                if (args.encodeBin and key != ""):
                    cls.writeBytes(helper.binStrToBytes(key), filename)
                else:
                    cls.write(key, filename)
            
            elif (key != ""):
                # Print key
                if (args.encodeBin):
                    print(bytes(helper.binStrToBytes(key)))
                else:
                    print(key)
        except Exception as e:
            cls.error(e)


    # Read/write methods
    @classmethod
    def read(cls, filename, decode = True):
        with open(filename, "rb") as fs:
            content = fs.read()
            if (decode): return content.decode("utf-8")
            return content

    @classmethod
    def write(cls, content, filename):
        with open(filename, "wb") as fs:
            fs.write(content.encode("utf-8"))

    @classmethod
    def writeBytes(cls, content, filename):
        with open(filename, "wb") as fs:
            fs.write(bytes(content))

    # Print errors
    @classmethod
    def error(cls, content):
        print("error: {0}".format(content))
        sys.exit(1)

    # Create parser
    @classmethod
    def getParser(cls):
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument("-h", "--help", help="Shows this help message or command help and exit", nargs="?", const="", default="", action=actions.HelpAction, metavar="CMD")
        subparsers = parser.add_subparsers(help="Commands", dest="cmd")
        cls.setupCypherParser(subparsers, "enc", "Encrypts a message using the provided key", "encrypted")
        cls.setupCypherParser(subparsers, "dec", "Decrypts a message using the provided key", "decrypted")
        cls.setupKeyGenParser(subparsers)
        return parser

    @classmethod
    def setupCypherParser(cls, subparsers, title, help_txt, func):
        parser = subparsers.add_parser(title, help=help_txt)
        parser.add_argument("-k", "--key", dest="keyOpt", help="Encryption key or filepath", nargs=1, metavar="KEY")
        parser.add_argument("-K", "--keytype", help="Determines how to read the encryption key", nargs=1, metavar="TYPE", default="text", choices=["text", "raw", "string"])
        parser.add_argument("-m", "--message", help="Message text to be {0}".format(func), nargs=1, metavar="MSG")
        parser.add_argument("-i", "--ifile", dest="input", help="Filepath of the message to be {0}".format(func), nargs=1, metavar="FILE")
        parser.add_argument("-o", "--ofile", dest="output", help="Filepath the output is written to", nargs=1, metavar="FILE")
        parser.add_argument("key", help="Encryption key or filepath", nargs="?")
        parser.add_argument("ifile", help="Filepath of the message to be {0}".format(func), nargs="?")
        parser.add_argument("ofile", help="Filepath the output is written to", nargs="?")

    @classmethod
    def setupKeyGenParser(cls, subparsers):
        parser = subparsers.add_parser("keygen", help="Generates a pseudorandom encryption key")
        parser.add_argument("-b", "--bytes", help="Specifies that the size is in bytes", action="store_true")
        parser.add_argument("-e", "--encodeBin", help="Encodes the output key as binary", action="store_true")
        parser.add_argument("-o", "--ofile", dest="output", help="Filepath the key is written to", nargs=1, metavar="FILE")
        parser.add_argument("size", help="The size of the key, default in bits", type=int)
        parser.add_argument("ofile", help="Filepath the key is written to", nargs="?")