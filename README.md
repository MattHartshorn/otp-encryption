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
Navigate to the source directory `/src`. Run Python followed by the script `otp.py` then specify which function you want to run and any required arguments.

```bash
cd ./src
python opt.py <function> <args...>
```

Test cases can be run by navigating to the `/test` directory and running the `test-cypher.py` script.

```bash
cd ./test
python test-cypher.py
```



## Functions

### Encyrpt
**Name:** `enc`

**Description:** Encrypts the provided plaintext using the given secret key. The encrypted text is written to the given output filepath. If encryption or reading fails, an empty output file will be written.

**Arguments:**
| Argument      | Description                                                            |
|---------------|------------------------------------------------------------------------|
| `key_file`    | The path to the file that contains the secret encyrption key.
| `input_file`  | The path to the plaintext file to be encrypted.
| `output_file` | The path to the output file that the encrypted text will be written to.

**Usage:**
```bash
enc <key_file> <input_file> <output_file>
```

**Example:**
```bash
python otp.py enc ../data/key.txt ../data/message.txt ../data/cyphertext.txt
```



### Decrypt
**Name:** `dec`

**Description:** Decrypts the provided cyphertext using the given secret key. The decrypted text is written to the given output filepath. If decryption or reading fails, an empty output file will be written.

**Arguments:**
| Argument      | Description                                                            |
|---------------|------------------------------------------------------------------------|
| `key_file`    | The path to the file that contains the secret encyrption key.
| `input_file`  | The path to the cyphertext file to be decrypted.
| `output_file` | The path to the output file that the decrypted text will be written to.

**Usage:**
```bash
dec <key_file> <input_file> <output_file>
```

**Example:**
```bash
python otp.py dec ../data/key.txt ../data/cyphertext.txt ../data/result.txt
```



### Generate Key
**Name:** `keygen`

**Description:** Creates a randomly generated key based on the provided number of bits. In order to create a useable key, the key size must be divisible by 8. This allows the key to be properly divided in 8-bit sized bytes.  

**Arguments:**
| Argument      | Description                                                                        |
|---------------|------------------------------------------------------------------------------------|
| `key_size`    | The number of bits that the generated key will contain. Must be greater than zero.
| `output_file` | The path to the output file that the key will be written to.

**Usage:**
```bash
keygen <key_size> <output_file>
```

**Example:**
```bash
python otp.py keygen 16 ../data/key.txt
```



### Key Histogram
**Name:** `keyhisto`

**Description:** Randomly generates the specified number of keys and counts the number of occurances of each unique key.

**Arguments:**
| Argument      | Description                                                                        |
|---------------|------------------------------------------------------------------------------------|
| `key_size`    | The number of bits that the generated key will contain. Must be greater than zero.
| `count`       | The number of keys to generate.
| `output_file` | The path to the output csv file that contains all unique keys and their count.

**Usage:**
```bash
keyhist <key_size> <count> <output_file>
```

**Example:**
```bash
python otp.py keygen 16 100000 ../data/keyhisto.csv
```