# Created by: Spencer Briguglio
# Student Number: 103 746 720
# Date: November 9th, 2020
from sympy import *
import random


def RSA_Keygen(p1, p2):
    # RSA_Keygen
    # Input: two prime numbers, p1 and p2
    # Output: publicKey, privateKey

    # check in p1 and p2 are prime
    if not(isprime(p1) and isprime(p2)):
        print("[!!] Error: numbers are not prime.")
        return -1, -1

    # calculate n and phi(n)
    n = p1 * p2
    phin = (p1-1)*(p2-1)

    # find e such that e is relative prime to phi(n)
    f = 0
    while f == 0:
        m = random.randint(2, phin)
        if gcd(phin, m) == 1:
            f = e = m

    # find d
    i = 2
    e1 = phin + 1
    while e1 % e != 0:
        e1 = (phin * i) + 1
        i += 1
    d = int(e1 / e)

    # set public and private keys
    publicKey = [e, n]
    privateKey = [d, n]

    return publicKey, privateKey


def RSA_Encryption(message, ku):
    # RSA_Encryption
    # Input: message to be encrypted, ku public key
    # Output: ciphertext
    ciphertext = (message ** ku[0]) % ku[1]
    return ciphertext


def RSA_Decryption(ciphertext, kr):
    # RSA_Decryption
    # Input: ciphertext to be decrypted, kr private key
    # Output: message which was encrypted
    plaintext = (ciphertext ** kr[0]) % kr[1]
    return plaintext


def main():
    # create and choose two primes
    primes = [i for i in range(11, 1000) if isprime(i)]
    p = random.choice(primes)
    q = random.choice(primes)

    # get input message from user
    message = input("Type a message to be encrypted: ")

    # set public and private keys
    ku, kr = RSA_Keygen(p, q)
    print("=== RSA_Keygen ===")
    print("Public Key: ", ku)
    print("Private Key: ", kr, "\n")

    # encrypt message
    print("=== RSA_Encryption ===")
    ciphertext = ""
    for e in message:
        print(e, "->", end='')
        c = (chr(RSA_Encryption(ord(e), ku)))
        ciphertext += c
        print(c)
    print("ciphertext: ", ciphertext)

    # decrypt message
    print("\n=== RSA_Decryption ===")
    plaintext = ""
    for f in ciphertext:
        print(f, "->", end='')
        d = chr(RSA_Decryption(ord(f), kr))
        plaintext += d
        print(d)
    print("plaintext: ", plaintext)

    # print results
    print("\n[RESULTS]\n=== Input Message ===\n\"", message, "\"\n\n=== Encrypted Ciphertext ===\n\" ", ciphertext,
          "\"\n\n=== Decrypted Plaintext ===\n\"", plaintext, "\"")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
