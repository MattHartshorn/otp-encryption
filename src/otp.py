import otpcypher
import keygenerator
import helper
import argparse
import sys
import actions

# Run execution
def main(args = None):
    parser = getParser()
    run(parser, parser.parse_args())

def run(parser, args):
    if (args.cmd == "enc" or args.cmd == "dec"):
        cypher(args)
    elif (args.cmd == "keygen"):
        keygen(args)
    else:
        parser.print_help()


# Encrypt & decrypt methods
def cypher(args):
    cypher_validate_args(args)
    ofile = args.ofile[0] if isinstance(args.ofile, list) else args.ofile

    try:
        try:
            # Load data
            key = cypher_loadkey(args)
            msg = cypher_loadmsg(args)
            
            # Encrypt/decrypt
            output = otpcypher.cypher(msg, key)
        except Exception as e:
            cypher_write(args, "", ofile)
            error(e)

        # Write data
        cypher_write(args, output, ofile)
    except IOError as e:
        error(e)

def cypher_validate_args(args):
    requiredArgs = []
    if (args.key == None and args.keyOpt == None):
        requiredArgs.append("key")
    if (args.ifile == None and args.input == None and args.message == None):
        requiredArgs.append("ifile/message")
    if (len(requiredArgs) > 0):
        error("the following arguments are required: {0}".format(", ".join(requiredArgs)))

def cypher_loadkey(args):
    key = args.key if args.key != None else args.keyOpt[0]
    ktype = args.keytype if isinstance(args.keytype, str) else args.keytype[0]

    if (ktype == "text"):
        return helper.binStrToBytes(read(key))
    elif (ktype == "raw"):
        return read(key, False)
    elif (ktype == "string"):
        return helper.binStrToBytes(key)
    else:
        raise Exception("Unknown keyType: '{0}'".format(ktype))
        
def cypher_loadmsg(args):
    filename = args.input[0] if args.input != None else args.ifile 
    if (filename == None):
        return args.message[0]
    else:
        return read(filename)

def cypher_write(args, output, filename):
    if (filename != None):
        write(output, filename)
    elif (output != ""):
        print(output.encode("utf-8"))

# Key gen methods
def keygen(args):
    if (args.size < 1 or args.size > 128):
        error("argument 'size' out of range: [0, 128]")

    ofile = args.output[0] if args.output != None else args.ofile
    try:
        try:
            # Generate key
            key = keygenerator.generate(args.size, args.bytes)
        except Exception as e:
            keygen_write(args, key, ofile)
            error(e)

        keygen_write(args, key, ofile)

    except IOError as e:
        error(e)

def keygen_write(args, key, filename):
    try:
        # Attempt to write the file
        if (filename != None):
            if (args.encodeBin and key != ""):
                writeBytes(helper.binStrToBytes(key), filename)
            else:
                write(key, filename)
        
        elif (key != ""):
            # Print key
            if (args.encodeBin):
                print(bytes(helper.binStrToBytes(key)))
            else:
                print(key)
    except Exception as e:
        error(e)


# Read/write methods
def read(filename, decode = True):
    with open(filename, "rb") as fs:
        content = fs.read()
        if (decode): return content.decode("utf-8")
        return content

def write(content, filename):
    with open(filename, "wb") as fs:
        fs.write(content.encode("utf-8"))

def writeBytes(content, filename):
    with open(filename, "wb") as fs:
        fs.write(bytes(content))

# Print errors
def error(content):
    print("error: {0}".format(content))
    sys.exit(1)

# Create parser
def getParser():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--help", help="Shows this help message or command help and exit", nargs="?", const="", default="", action=actions.HelpAction, metavar="CMD")
    subparsers = parser.add_subparsers(help="Commands", dest="cmd")
    setupCypherParser(subparsers, "enc", "Encrypts a message using the provided key", "encrypted")
    setupCypherParser(subparsers, "dec", "Decrypts a message using the provided key", "decrypted")
    setupKeyGenParser(subparsers)
    return parser

def setupCypherParser(subparsers, title, help_txt, func):
    parser = subparsers.add_parser(title, help=help_txt)
    parser.add_argument("-k", "--key", dest="keyOpt", help="Encryption key or filepath", nargs=1, metavar="KEY")
    parser.add_argument("-K", "--keytype", help="Determines how to read the encryption key", nargs=1, metavar="TYPE", default="text", choices=["text", "raw", "string"])
    parser.add_argument("-m", "--message", help="Message text to be {0}".format(func), nargs=1, metavar="MSG")
    parser.add_argument("-i", "--ifile", dest="input", help="Filepath of the message to be {0}".format(func), nargs=1, metavar="FILE")
    parser.add_argument("-o", "--ofile", dest="output", help="Filepath the output is written to", nargs=1, metavar="FILE")
    parser.add_argument("key", help="Encryption key or filepath", nargs="?")
    parser.add_argument("ifile", help="Filepath of the message to be {0}".format(func), nargs="?")
    parser.add_argument("ofile", help="Filepath the output is written to", nargs="?")

def setupKeyGenParser(subparsers):
    parser = subparsers.add_parser("keygen", help="Generates a pseudorandom encryption key")
    parser.add_argument("-b", "--bytes", help="Specifies that the size is in bytes", action="store_true")
    parser.add_argument("-e", "--encodeBin", help="Encodes the output key as binary", action="store_true")
    parser.add_argument("-o", "--ofile", dest="output", help="Filepath the key is written to", nargs=1, metavar="FILE")
    parser.add_argument("size", help="The size of the key, default in bits", type=int)
    parser.add_argument("ofile", help="Filepath the key is written to", nargs="?")




# Execute the program
if (__name__ == "__main__"):
    main(sys.argv)