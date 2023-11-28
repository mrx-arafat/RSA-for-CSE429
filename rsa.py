def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(e, n, plaintext):
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

def decrypt(d, n, ciphertext):
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

def main():
    p = input("Factor 1 (prime number) P= ").strip()
    q = input("Factor 2 (prime number) Q= ").strip()
    e = input("Public Key E (Usually E=65537) E= ").strip()
    d = input("Private Key value (Integer) D= ").strip()
    phi = input("Intermediate value Phi (Integer) φ= ").strip()
    message = input("Enter a message to encrypt (leave empty if decrypting): ").strip()
    c = input("Value of the cipher message (Integer) C= (leave empty if encrypting) ").strip()

    if p and q:
        p, q = int(p), int(q)
        n = p * q
        print("Computed Public Key value (Integer) N=", n)
    else:
        n = input("Public Key value (Integer) N= ").strip()
        n = int(n) if n.isdigit() else None

    if e and phi:
        e, phi = int(e), int(phi)
        d = modinv(e, phi)
        print("Computed Private Key value (Integer) D=", d)
    elif e and n:
        e = int(e)
        if not d.isdigit():
            print("Cannot compute D without φ. Please provide φ or D.")
            return
    else:
        print("E and N or φ are required to proceed.")
        return

    if message:
        encrypted_msg = encrypt(e, n, message)
        encrypted_msg_int = ' '.join(map(str, encrypted_msg))
        print("Encrypted message (Integer):", encrypted_msg_int)
    
    if c.isdigit():
        c = int(c)
        decrypted_message = decrypt(d, n, [c])
        print("Decrypted message:", decrypted_message)

if __name__ == '__main__':
    main()
