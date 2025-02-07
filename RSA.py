# RSA Cyptosystem Project 1
# Aiden Cary, Nathan Wetherington, Dalton Gorham
import math
import random


# This function was from Dr. Hu's slides 
def test_prime(p = 137):
    '''Test if p is prime with Fermat\'s little theorem\n'''
    t = True
    for i in range(1, p):
        if pow(i, p-1, p) != 1:
            t = False
            break
        
    return t

# Function to generate a random prime number between min and max
def generate_prime(min, max):
    prime = random.randint(min, max)

    while not test_prime(prime):
        prime = random.randint(min, max)
    return prime



# Function to find an integer 'e' that is relatively prime to 'phi'
def find_relatively_prime(phi):
    # Start with a small number greater than 1
    e = 2
    # Keep increasing e until we find one that is coprime with phi
    while math.gcd(e, phi) != 1:
        e += 1
    return e



def modular_inverse(e, phi):
    # Function to compute the greatest common divisor (GCD) using the Euclidean Algorithm
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

    # Compute the GCD of e and phi
    gcd, x, y = extended_gcd(e, phi)

    # If the GCD is 1, then e and phi are coprime, and the modular inverse exists
    if gcd == 1:
        # Ensure the modular inverse is positive
        return x % phi
    else:
        # If GCD is not 1, no modular inverse exists
        return None
    

# Encrypts the message using the public key
def encrypt_message(public_key, message):
    e, n = public_key
    # Convert the message to a list of integers (ASCII values)
    message_encoded = [ord(c) for c in message]
    # Encrypt each character using RSA formula: c = m^e % n
    encrypted_message = [pow(m, e, n) for m in message_encoded]
    return encrypted_message

# Decrypts the message using the private key
def decrypt_message(private_key, encrypted_message):
    d, n = private_key
    # Decrypt each character using RSA formula: m = c^d % n
    decrypted_message = [pow(c, d, n) for c in encrypted_message]
    # Convert the decrypted message back to characters
    return "".join(chr(m) for m in decrypted_message)

# Sign a message
def sign_message(message, private_key):
    d, n = private_key
    hashed = sum(ord(char) for char in message)
    return pow(hashed, d, n)

# Verify signature
def verify_signature(message, signature, public_key):
    e, n = public_key
    hashed = sum(ord(char) for char in message)
    return hashed == pow(signature, e, n)


def display_welcome_message():
    """Display the welcome message."""
    print("\nWelcome to the RSA Cryptosystem!")

# Prints the user selection menu and returns input
def user_type_menu():
    print("\n=====================================")
    print("\nPlease select your user type:")
    print("1. A public user")
    print("2. The owner of the keys")
    print("3. Exit program")
    choice = input("Enter your choice: ")
    if choice in ['1', '2', '3']:
        return choice
    else:
        print("\nInvalid input. Please enter 1, 2, or 3.")
        return user_type_menu()


# Prints the public user menu and returns input
def public_user_menu():
    print("\n=====================================")
    print("\nPublic User Menu:")
    print("What would you like to do?")
    print("1: Send an encrypted message")
    print("2: Authenticate a digital signature")
    print("3: Return to main menu")
    choice = input("Enter your choice: ")
    
    if choice in ['1', '2', '3']:
        return int(choice)
    else:
        print("\nInvalid input. Please enter 1, 2, or 3.")
        return public_user_menu()

# Handles public user menu options
def handle_public_user_menu(public_key, messages, signatures):
    
    while True:
        user_choice = public_user_menu()
        if user_choice == 1:
            send_encrypted_message(public_key, messages)
        elif user_choice == 2:
            handle_authenticate_signature(public_key, messages, signatures)
        elif user_choice == 3:
            print("\nExiting public user menu.")
            return 
        else:
            print("\nInvalid input. Please enter 1, 2, or 3.")

# Prints the owner menu and returns the input
def owner_menu():
    print("\n=====================================")
    print("\nKey Owner Menu:")
    print("As the owner of the keys, what would you like to do?")
    print("1. Decrypt a received message")
    print("2. Digitally sign a message")
    print("3. Show the keys")
    print("4. Generate a new set of keys")
    print("5. Return to main menu")
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter 1, 2, or 3.")
        return owner_menu()

# Handles the key owner menu options
def handle_key_owner(private_key, public_key, messages, signatures):
    
    while True:
        owner_choice = owner_menu()
        if owner_choice == 1:
            handle_decrypt_messages(private_key, messages)
        elif owner_choice == 2:
            handle_sign_message(private_key, messages, signatures)
        elif owner_choice == 3:
            show_keys(public_key, private_key)
        elif owner_choice == 4:
            handle_generate_new_keys(private_key, public_key, messages, signatures)
        elif owner_choice == 5:
            return (messages, signatures, public_key, private_key)
        else:
            print("\nInvalid input.")

# helper function to send an encrypted message for the public user
def send_encrypted_message(public_key, messages):
    input_msg = input("Enter a message: ")
    encrypted_message = encrypt_message(public_key, input_msg)
    print("\nMessage encrypted and sent.")
    messages.append(encrypted_message)


# helper function to decrypt messages for the key owner
def handle_decrypt_messages(private_key, messages):
    if messages == []:
        print("\nNo message to decrypt.")
    else:
        print("\nThe following messages are available:")
        decrypted_messages = [decrypt_message(private_key, message) for message in messages]
        for i, decrypted_message in enumerate(decrypted_messages, start=1):
            print(f"{i}. (length = {len(decrypted_message)})")
        choice = int(input("Enter your choice: "))
        if choice > len(decrypted_messages) or choice < 1:
            print("\nInvalid choice. Please select a valid message.")
        else:
            print(f"\nDecrypted message: {decrypted_messages[choice - 1]}")


# function to show the keys
def show_keys(public_key, private_key):
    print("\nShowing keys:")
    print(f"\nPublic Key: {public_key}")
    print(f"Private Key: {private_key}")


# helper function to generate new keys for the key owner
def handle_generate_new_keys(private_key, public_key, messages, signatures):
    choice = input(("Generating new keys will delete all the encrypted messages sent, are you sure? (y/n)"))
    choice = choice.lower()
    if (choice == 'y'):
        print ("Generating new keys...")
        public_key, private_key = generate_keys()
        print("New keys generated!")
        messages.clear() # Clear the messages list after generating new keys
        signatures.clear() # Clear the signatures list after generating new keys


# helper function to sign a message for the key owner
def handle_sign_message(private_key, messages, signatures):
    if not messages:
        print("\nThere are no messages to sign.")
    else:
        print("\nThe following messages are available:")
        decrypted_messages = [decrypt_message(private_key, message) for message in messages]

        for i in range(len(decrypted_messages)):
            print(f"{i + 1}. {decrypted_messages[i]}")
        choice = int(input("Enter your choice: "))
        if choice > len(messages) or choice < 1:
            print("\nInvalid choice. Please select a valid message.")
        else:
            message_to_sign = messages[choice - 1] # go back to 0-based index
            try:
                message_to_sign_str = "".join(chr(m) for m in message_to_sign if 0 <= m < 0x110000) # convert to string
                signature_input = input("Enter your signature: ")
                signature = sign_message(message_to_sign_str, private_key)
                signatures.append((signature_input, signature))
                print("\nMessage signed and sent.")
            except ValueError as e:
                print(f"\nError: {e}")


# helper function to authenticate a digital signature for the public user
def handle_authenticate_signature(public_key, messages, signatures):
    """Handle authenticating a digital signature."""
    if not signatures:
        print("\nThere are no signatures to authenticate")
    else:
        print("\nThe following messages are available:")
        for i in range(len(signatures)):
            print(f"{i + 1}. {signatures[i][0]}")
        choice = int(input("Enter your choice: "))
        if choice > len(signatures) or choice < 1:
            print("\nInvalid choice. Please select a valid signature.")
        else:
            signature_to_be_verified = signatures[choice - 1]
            message_to_verify = messages[choice - 1]
            try:
                message_to_verify_str = "".join(chr(m) for m in message_to_verify if 0 <= m < 0x110000) # convert to string
                if verify_signature(message_to_verify_str, signature_to_be_verified[1], public_key):
                    print(f"\nSignature '{signature_to_be_verified[0]}' is valid.")
                else:
                    print(f"\nSignature '{signature_to_be_verified[0]}' is not valid.")
            except ValueError as e:
                print(f"\nError: {e}")

# Generates public and private keys      
def generate_keys():
    p = generate_prime(100, 5000)
    q = generate_prime(100, 5000)

    n = p * q

    phi = (p - 1) * (q - 1)

    e = find_relatively_prime(phi)

    d = modular_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


# Main loop to handle user input and menu options
def main_loop(public_key, private_key, messages, signatures):
    """Main loop to handle user input and menu options."""
    while True:
        user_input = user_type_menu()
        if user_input == '1':
            handle_public_user_menu(public_key, messages, signatures)
        elif user_input == '2':
            result = handle_key_owner(private_key, public_key, messages, signatures)
            if result is not None:
                messages, signatures, public_key, private_key = result
        elif user_input == '3':
            print("Exiting program. Goodbye!")
            break




def main():
    # Generate public and private keys
    public_key, private_key = generate_keys()
    messages = []
    signatures = []
    display_welcome_message()
    main_loop(public_key, private_key, messages, signatures)



if __name__ == "__main__":
    main()
