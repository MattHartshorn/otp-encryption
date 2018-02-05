# One Time Pad Encryption

This project illustrates the use of [One Time Pad](https://en.wikipedia.org/wiki/One-time_pad) encryption. The project is capable of creating a randomly generated encryption key, encrypting, and decrypting messages. The encryption and decryption process is done by reading and writing text to and from files.

## Environment

**Language:** Python 3.4

**Operating System:** Windows 10

## Prerequisites

Python 3.4 command line interface must be installed on the device. The download for Python can be found [here](https://www.python.org/downloads/).

## Usage
Navigate to the source directory `/src`.

```bash
cd ./src
```

Run Python followed by the script `otp.py` then specify which function you want to run and any required arguments.

```bash
./python opt.py <function> <args...>
```

## Functions

### Encyrpt
**Name:** `enc`

**Description:** Encrypts the provided plaintext using the given secret key.

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
./python otp.py enc ../data/key.txt ../data/message.txt ../data/cyphertext.txt
```



### Decrypt
**Name:** `dec`

**Description:** Decrypts the provided cyphertext using the given secret key.

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
./python otp.py dec ../data/key.txt ../data/cyphertext.txt ../data/result.txt
```


### Generate Key
**Name:** `keygen`

**Description:** Creates a randomly generated key based on the provided number of bits.

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
./python otp.py keygen 16 ../data/key.txt
```

**Note:**
In order for the key to be accepted to encrypt/decrypt the number of bits must be divisable by 8.



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
./python otp.py keygen 16 100000 ../data/keyhisto.csv
```