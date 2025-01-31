# RSA Cyptosystem Project 1
# Aiden Cary, Nathan Wetherington, Dalton Gorham

# Imports
import random
import math
from math import gcd # gcd = greatest common denominator

# Helper function to check if a number is prime
# Returns true if prime and false if not prime
def is_prime(n):
    if (n < 2):  # If a number is less than 2, it cannot be prime
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        # If n has any factors other than 1 and itself, at least one of them must be <= sqrt(n)
        # If n is divisible by any number in this range, it is not a prime number
        if n % i == 0:
            return False
    return True  # Return True only if no divisors were found

# Helper function for generating a random prime number
# Returns a prime number
def generate_prime(start = 100, end = 1000):
    # While numbers generated are not prime, loop again
     while True:
        # Generates a random number between 100 and 1000
        p = random.randint(start, end)
        if is_prime(p):
            return p

# Helper function for computing the modular inverse using the Extended Euclidean Algorithm
# egcd finds the greatest common divisor of two numbers, a and b, while also computing coefficients x and y
# such that ax + by = gcd(a, b)
def modular_inverse(e, phi):
    # egcd is a recursive function that checks if a == 0, it returns (b, 0, 1) since the GCD of 0 and b, is b
    # else it recurses with b % a and a, computing coefficients x and y using the returned values
    def egcd(a, b):
        if a == 0:
            return b, 0, 1 # Breaks out of recursion
        g, x, y = egcd(b % a, a) # Recursive statement
        # b // a is floor division that returns the integer quotient, discarding the remainder
        return g, y, - (b // a) * x, x
    # The underscore is a placeholder for y since it is not used
    g, x, _  = egcd(e, phi)
    return x % phi if g == 1 else None

# Generates the RSA keys for encryption
def generate_keys():
    # Generate keys p and q
    key_p = generate_prime() # Public key
    key_q = generate_prime() # Private key

    # While q is equal to p, generate a new prime number for q
    while key_q == key_p:
        key_q = generate_prime()

    # key_n is the product of p and q
    key_n = (key_p * key_q)

    # phi is Euler's toient function and helps determine the valid values for the coprime e
    phi = (key_p - 1) * (key_q - 1)

    # e is the public exponent chosen randomly such that...
    # 1 < e < phi && gcd(e, phi) = 1 making e coprime to phi
    # Coprime means that two numbersb have no common factor other than 1
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = modular_inverse(e, phi)

    return (e, key_n), (d, key_n)

# Prints the user selection menu
def user_type_menu():
    print("\nPlease select your user type:")
    print("1. A public user")
    print("2. The owner of the keys")
    print("3. Exit program")
    input = ("Enter your choice: ")
    return input


def main():
    # Generate keys
    public_key, private_key = generate_keys()
    # Create arrays for messages and signatures to hold input
    messages = []
    signatures = []

    print("RSA keys have been generated.")

    while True:
        user_type = user_type_menu()


    
