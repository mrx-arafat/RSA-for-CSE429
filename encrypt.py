# encrypt.py
import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(message, public_key):
    n, e = public_key
    message_number = int.from_bytes(message.encode(), 'big')
    encrypted_number = pow(message_number, e, n)
    return encrypted_number

# RSA Setup
p = 61
q = 53
n = p * q
lam_n = lcm(p-1, q-1)
e = 17
d = modinv(e, lam_n)

# Encrypt a message
public_key = (n, e)
message = "Hello Arafat"
encrypted_message = encrypt(message, public_key)

# Write to cipher.txt
with open("cipher.txt", "w") as file:
    file.write(f"C: {encrypted_message}\np: {p}\nq: {q}\nN: {n}")
