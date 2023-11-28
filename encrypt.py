# encrypt.py
import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        if m == 0:
            return None  # This would mean e and λ(n) are not coprime
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(message, public_key):
    n, e = public_key
    message_number = int.from_bytes(message.encode(), 'big')
    encrypted_number = pow(message_number, e, n)
    return encrypted_number

# User inputs
p = int(input("Enter a prime number for p (e.g., 17): "))
q = int(input("Enter a different prime number for q (e.g., 19): "))
e = int(input("Enter public exponent e (e.g., 65537): "))
message = input("Enter a message to encrypt: ")

# RSA Setup
n = p * q
lam_n = lcm(p-1, q-1)
d = modinv(e, lam_n)

if d is None:
    print("Public exponent e is not coprime with λ(n). Please choose a different e.")
else:
    # Encrypt the message
    public_key = (n, e)
    encrypted_message = encrypt(message, public_key)

    # Write to cipher.txt with numeric C value
    with open("cipher.txt", "w") as file:
        file.write(f"C: {encrypted_message}\np: {p}\nq: {q}\nN: {n}\nd: {d}\ne: {e}")
