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
    


def encrypt_message(public_key, message):
    e, n = public_key
    # Convert the message to a list of integers (ASCII values)
    message_encoded = [ord(c) for c in message]
    # Encrypt each character using RSA formula: c = m^e % n
    encrypted_message = [pow(m, e, n) for m in message_encoded]
    return encrypted_message

# Decrypt the message
def decrypt_message(private_key, encrypted_message):
    d, n = private_key
    # Decrypt each character using RSA formula: m = c^d % n
    decrypted_message = [pow(c, d, n) for c in encrypted_message]
    # Convert the decrypted message back to characters
    return "".join(chr(m) for m in decrypted_message)


# Prints the user selection menu
def user_type_menu():
    print("\nPlease select your user type:")
    print("1. A public user")
    print("2. The owner of the keys")
    print("3. Exit program")
    return input("Enter your choice: ")


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


def handle_public_user_menu(public_key):
    while True:
        user_choice = public_user_menu()
        if user_choice == 1:
            message = input("Enter a message: ")

            encrypted_message = encrypt_message(public_key, message)
            print("Message encrypted and sent.")
            
        elif user_choice == 2:
            print("Digital signature authentication feature is not yet implemented.")
            # Add implementation later
        elif user_choice == 3:
            print("Exiting public user menu.")
            return encrypted_message
        else:
            print("Invalid option. Please try again.")


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
            




def main():
    
    # TODO - Implement the rest of handle_key_owner options and the digital signature functionality
    signatures = []
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

    

    while True:
        user_input = user_type_menu()
        if user_input == '1':
           encrypted_message = handle_public_user_menu(public_key)
        elif user_input == '2':
            print("Owner of the keys functionality is not yet implemented.")
            handle_key_owner(private_key, encrypted_message)
        elif user_input == '3':
            print("Exiting program. Goodbye!")
            break
    




if __name__ == "__main__":
    main()