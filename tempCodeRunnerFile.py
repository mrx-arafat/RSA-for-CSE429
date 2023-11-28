# decrypt.py
import math

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Read from cipher.txt
with open("cipher.txt", "r") as file:
    lines = file.readlines()
    C = int(lines[0].split(": ")[1])
    p = int(lines[1].split(": ")[1])
    q = int(lines[2].split(": ")[1])
    N = int(lines[3].split(": ")[1])
    d = int(lines[4].split(": ")[1])
    e = int(lines[5].split(": ")[1])

# Calculate the decryption key
phi = (p - 1) * (q - 1)
d = modinv(e, phi)

if d is None:
    print("Public exponent e is not coprime with λ(n). Please choose a different e.")
else:
    # Decrypt the message
    decrypted_message = pow(C, d, N)

    # Convert the decrypted message to bytes
    decrypted_message_bytes = decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, 'big')

    print("Decrypted Data:")
    print(decrypted_message_bytes)
