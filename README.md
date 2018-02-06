# One Time Pad Encryption

This project illustrates the use of [One Time Pad](https://en.wikipedia.org/wiki/One-time_pad) encryption. The project is capable of creating a randomly generated encryption key, encrypting, and decrypting messages. This project utilizes file IO to read and write the input and output of the given commands. Any errors will be printed to the terminal and output files will be written as an empty file.

The input and output text will be encoded/decoded as UTF-8. This means ASCII and UTF-8 characters are valid, any other encoding will result in errors.

When utilizing OTP encryption it is important to note that the length of the secret key (bytes) must be the same length as the message (bytes). Therefore, if the message is 16 characters long the key must be 16 bytes or 128 bits.



## Environment

The following information denotes the environment setup in which the code was written and tested.

**Language:** Python 3.4

**Operating System:** Windows 10



## Prerequisites

The Python 3.4 command line interface must be installed on the device. The download for Python can be found [here](https://www.python.org/downloads/).



## Usage
Navigate to the source directory `/src`. Run Python followed by the script `otp.py` then specify which command you want to run and any required arguments.

```bash
> cd ./src
> python opt.py <command> [args...]
```

Test cases can be run by navigating to the `/test` directory and running the `test.py` script.

```bash
> cd ./test
> python test.py
```



## Commands

### Encyrpt
**Name:** `enc`

**Description:** Encrypts the provided plaintext using the given secret key. The encrypted text is written to the given output filepath. If encryption or reading fails, an empty output file will be written.

**Options:**
| Char | Verbose     | Arg                        | Description
|------|-------------|----------------------------|-------------------------------------------|
| `-k` | `--key`     | `KEY`                      | Encryption key or filepath
| `-K` | `--keytype` | `text | raw | string`      | Determines how to read the encryption key
| `-m` | `--message` | `MSG`                      | Message to be ecrypted
| `-i` | `--ifile`   | `FILE`                     | Filepath of the message to be encrypted
| `-o` | `--ofile`   | `FILE`                     | Filepath the output is written to

**Key Type:**

`text`: Key is loaded from a UTF-8 encoded text file.

`raw` : Key is loaded from a raw binary file.

`string` : Key is loaded as a binary string from the command line interface

**Arguments:**
| Argument| Required | Description
|---------|----------|------------------------------------------|
| `key`   | No*      | Encryption key or filepath
| `ifile` | No*      | Filepath of the message to be encrypted
| `ofile` | No       | Filepath the output is written to

No* : Argument is not required if it's `option` counterpart is provided

**Usage:**
```bash
enc [-k KEY] [-K TYPE] [-m MSG] [-i FILE] [-o FILE] [key] [ifile] [ofile]
```

**Examples:**
```bash
> python otp.py enc ../data/key ../data/plaintext ../data/cyphertext

> python otp.py enc -k ../data/key -i ../data/plaintext -o ../data/cyphertext

> python otp.py enc -k ../data/key -m "hello there" -o ../data/cyphertext

> python otp.py enc -K string -k 0100110111010110 -m HI 
b'\x05\xc2\x9f'
```



### Decrypt
**Name:** `dec`

**Description:** Decrypts the provided cyphertext using the given secret key. The decrypted text is written to the given output filepath. If decryption or reading fails, an empty output file will be written.

**Options:**
| Char | Verbose     | Arg                        | Description
|------|-------------|----------------------------|--------------------------------------------|
| `-k` | `--key`     | `KEY`                      | Encryption key or filepath
| `-K` | `--keytype` | `text | raw | string`      | Determines how to read the encryption key
| `-m` | `--message` | `MSG`                      | Message to be decrypted
| `-i` | `--ifile`   | `FILE`                     | Filepath of the message to be decrypted
| `-o` | `--ofile`   | `FILE`                     | Filepath the output is written to

**Key Type:**

`text`: Key is loaded from a UTF-8 encoded text file.

`raw` : Key is loaded from a raw binary file.

`string` : Key is loaded as a binary string from the command line interface

**Arguments:**
| Argument| Required | Description
|---------|----------|--------------------------------|
| `key`   | No*      | Encryption key or filepath
| `ifile` | No*      | Filepath of the message to be encrypted
| `ofile` | No       | Filepath the output is written to

No* : Argument is not required if it's `option` counterpart is provided

**Usage:**
```bash
dec [-k KEY] [-K TYPE] [-m MSG] [-i FILE] [-o FILE] [key] [ifile] [ofile]
```

**Examples:**
```bash
> python otp.py dec ../data/key ../data/cyphertext ../data/plaintext

> python otp.py dec -k ../data/key -i ../data/cyphertext -o ../data/plaintext

> python otp.py dec -k ../data/key -m "hello there" -o ../data/plaintext

> python otp.py dec -K string -k 0100110111010110 -i ../data/hi-cyphertext
HI
```


### Generate Key
**Name:** `keygen`

**Description:** Creates a randomly generated key based on the provided number of bits. In order to create a useable key, the number of bits in the key must be divisible by 8. This allows the key to be properly divided in 8-bit sized bytes.  

**Options:**
| Char | Verbose       | Arg    | Description
|------|---------------|--------|-----------------------------------------|
| `-b` | `--bytes`     |        | Specifies that the size is in bytes
| `-e` | `--encodeBin` |        | Encodes the output key as binary
| `-o` | `--ofile`     | `FILE` | Filepath the key is written to

**Arguments:**
| Argument| Required | Description
|---------|----------|------------------------------------------|
| `size`  | Yes      | The size of the key, default in bits
| `ofile` | No       | Filepath the key is written to

**Usage:**
```bash
keygen [-b] [-e] [-o FILE] <size> [ofile]
```

**Example:**
```bash
> python otp.py keygen 16 ../data/key

> python otp.py keygen -b 2 -o ../data/key

> python otp.py keygen -b 2
0100111011011100

> python otp.py keygen -b -e 2
b'\xf4\xfa'
```
