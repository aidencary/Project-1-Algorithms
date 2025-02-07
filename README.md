# RSA Cryptosystem Project

## Authors
- Aiden Cary
- Nathan Wetherington
- Dalton Gorham

## Overview
This project implements an RSA Cryptosystem, which is a public-key cryptosystem used for secure data transmission. The system allows users to encrypt messages, decrypt messages, sign messages, and verify digital signatures.

## Features
- Generate public and private keys
- Encrypt messages using the public key
- Decrypt messages using the private key
- Sign messages using the private key
- Verify digital signatures using the public key

## How It Works
The RSA Cryptosystem uses a pair of keys: a public key and a private key. The public key is used to encrypt messages and verify signatures, while the private key is used to decrypt messages and sign messages.

### Key Generation
The `generate_keys` function generates a pair of public and private keys. It selects two random prime numbers, calculates their product, and computes the public and private exponents.

### Encryption and Decryption
- `encrypt_message(public_key, message)`: Encrypts a message using the public key.
- `decrypt_message(private_key, encrypted_message)`: Decrypts a message using the private key.

### Signing and Verifying
- `sign_message(message, private_key)`: Signs a message using the private key.
- `verify_signature(message, signature, public_key)`: Verifies a digital signature using the public key.

## Methods

### Key Generation
- `generate_prime(min, max)`: Generates a random prime number between `min` and `max`.
- `find_relatively_prime(phi)`: Finds an integer `e` that is relatively prime to `phi`.
- `modular_inverse(e, phi)`: Computes the modular inverse of `e` modulo `phi`.
- `generate_keys()`: Generates and returns a pair of public and private keys.

### Encryption and Decryption
- `encrypt_message(public_key, message)`: Encrypts a message using the public key.
- `decrypt_message(private_key, encrypted_message)`: Decrypts a message using the private key.

### Signing and Verifying
- `sign_message(message, private_key)`: Signs a message using the private key.
- `verify_signature(message, signature, public_key)`: Verifies a digital signature using the public key.

### User Interaction
- `user_type_menu()`: Displays the user type selection menu and returns the user's choice.
- `public_user_menu()`: Displays the public user menu and returns the user's choice.
- `owner_menu()`: Displays the key owner menu and returns the user's choice.

### Handlers
- `handle_public_user_menu(public_key, messages, signatures)`: Handles the public user menu options.
- `handle_key_owner(private_key, public_key, messages, signatures)`: Handles the key owner menu options.
- `handle_encrypt_message(public_key, messages)`: Handles encrypting a message for the public user.
- `handle_decrypt_messages(private_key, messages)`: Handles decrypting messages for the key owner.
- `handle_sign_message(private_key, messages, signatures)`: Handles signing a message for the key owner.
- `handle_authenticate_signature(public_key, messages, signatures)`: Handles authenticating a digital signature for the public user.
- `handle_generate_new_keys(private_key, public_key, messages, signatures)`: Handles generating new keys for the key owner.

### Utility Functions
- `convert_to_string(int_list)`: Converts a list of integers to a string, ensuring values are within the valid range for `chr()`.

## Main Loop
- `main_loop(public_key, private_key, messages, signatures)`: Main loop to handle user input and menu options.
- `main()`: Main function to run the RSA Cryptosystem.

## Running the Program
To run the program, execute the following command:
```sh
python RSA.py