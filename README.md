# CodioLinuxRepo

## Description
A Python-based Caesar cipher implementation written and executed in a 
Linux environment via Codio. Demonstrates fundamental cryptography 
concepts through one of history's oldest encryption techniques.

## Tech Stack
- **Language**: Python
- **Environment**: Linux (Codio)

## What is a Caesar Cipher?
A Caesar cipher is one of the oldest and simplest encryption techniques. 
It works by shifting each letter in a message by a fixed number of 
positions in the alphabet.

For example with a shift of 3:
- `A → D`
- `B → E`
- `HELLO → KHOOR`

To decrypt, simply shift in the opposite direction by the same amount.

## Files
- `mycipher.py` — Caesar cipher encryption and decryption logic
- `hello_world.txt` — sample text file used for testing the cipher

## How to Run
```bash
python3 mycipher.py
```

## What I Learned
- Python string manipulation
- Modular arithmetic for letter shifting
- Basic cryptography concepts
- Working in a Linux terminal environment
- File I/O in Python

## Future Improvements
- Support for Vigenère cipher
- GUI interface
- File encryption support
- Brute force decryption mode

## License
MIT License
