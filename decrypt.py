# decrypt.py
import math

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_number = pow(encrypted_message, d, n)
    decrypted_message = decrypted_number.to_bytes((decrypted_number.bit_length() + 7) // 8, 'big').decode()
    return decrypted_message

# Read from cipher.txt
with open("cipher.txt", "r") as file:
    lines = file.readlines()
    C = int(lines[0].split(": ")[1])
    p = int(lines[1].split(": ")[1])
    q = int(lines[2].split(": ")[1])
    N = int(lines[3].split(": ")[1])
    d = int(lines[4].split(": ")[1])

private_key = (N, d)

# Decrypt the message
decrypted_message = decrypt(C, private_key)

# Write the decrypted message to output.txt
with open("output.txt", "w") as file:
    file.write(decrypted_message)
