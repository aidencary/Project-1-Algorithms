# RSA Cyptosystem Project 1
# Aiden Cary, Nathan Wetherington, Dalton Gorham
import math
import random

def test_prime(p = 137):
    '''Test if p is prime with Fermat\'s little theorem\n'''
    t = True
    for i in range(1, p):
        if pow(i, p-1, p) != 1:
            t = False
            break
        
    return t


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

# Prints the user selection menu and returns input
def user_type_menu():
    print("\nPlease select your user type:")
    print("1. A public user")
    print("2. The owner of the keys")
    print("3. Exit program")
    return input("Enter your choice: ")

# Prints the public user menu and returns input
def public_user_menu():
    print("\nPublic User Options:")
    print("1: Send an encrypted message")
    print("2: Authenticate a digital signature")
    print("3: Exit")
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter 1, 2, or 3.")
        return public_user_menu() 

# Handles public user menu options
def handle_public_user_menu(public_key, message, signature):
    while True:
        user_choice = public_user_menu()
        if user_choice == 1:
            input_msg = input("Enter a message: ")

            encrypted_message = encrypt_message(public_key, input_msg)
            print("Message encrypted and sent.")
            
        elif user_choice == 2:
            #print("Digital signature authentication feature is not yet implemented.")
            # Add implementation later
            if signature is None:
                print("There are no signature to authenticate")
            elif verify_signature(message, signature, public_key ):
                print("The following messages are available:")
                print(f"1. {message}")
        elif user_choice == 3:
            print("Exiting public user menu.")
            return encrypted_message
        else:
            print("Invalid option. Please try again.")

# Prints the owner menu and returns the input
def owner_menu():
    print("\nAs the owner of the keys, what would you like to do?")
    print("1. Decrypt a received message")
    print("2. Digitally sign a message")
    print("3. Show the keys")
    print("4. Generate a new set of keys")
    print("5. Exit")
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter 1, 2, or 3.")
        return owner_menu()


def handle_key_owner(private_key, encrypted_message):
    while True:
        owner_choice = owner_menu()
        if owner_choice == 1:
            if encrypted_message is None:
                print("No message to decrypt.")
            else:
                decrypted_message = decrypt_message(private_key, encrypted_message)
                print(f"Decrypted message: {decrypted_message}")
        elif owner_choice == 2:
            message = input("Enter a message: ")
            signature = sign_message(message, private_key)
            print("Message signed and sent")
        elif owner_choice == 3:
            print("Implementation has not been added.")
        elif owner_choice == 4:
            print ("Implementation has not been added")
        elif owner_choice == 5:
            return (message, signature)

            




def main():
    
    # TODO - Implement the rest of handle_key_owner options and the digital signature functionality
    p = generate_prime(100, 5000)
    q = generate_prime(100, 5000)

    n = p * q

    phi = (p - 1) * (q - 1)

    e = find_relatively_prime(phi)


    d = modular_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Sets encrypted message to None so key owner menu can be accessed without their being a message
    encrypted_message = None
    message = None
    signature = None
    
    while True:
        user_input = user_type_menu()
        if user_input == '1':
           encrypted_message = handle_public_user_menu(public_key, message, signature)
        elif user_input == '2':
            print("Owner of the keys functionality is not yet implemented.")
            message, signature = handle_key_owner(private_key, encrypted_message)
        elif user_input == '3':
            print("Exiting program. Goodbye!")
            break
    




if __name__ == "__main__":
    main()