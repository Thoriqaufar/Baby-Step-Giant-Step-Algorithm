import random
from fermat import fermat
from find_primitive_root import findPrimitiveRoot

def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m % n)

def squareAndMultiply(base, exponent, modulus):
    bit = bin(exponent)[2:]
    z = 1

    for bits in bit:
        if bits == '0':
            z = z * z % modulus
        else:
            z = base * z * z % modulus
    
    return(z)

def primeGenerator():
    prime = random.randint(minVal, maxVal)
    while not fermat(prime) == 'Kemungkinan Prima':
        prime = random.randint(minVal, maxVal)

    return(prime)

def findBigPrimitiveRoot(prime):
    a = findPrimitiveRoot(prime)
    phi = prime - 1

    m = 2
    while m < phi:
        if gcd(m, phi) == 1:
            bigPrimitiveRoot = squareAndMultiply(a, m, prime)
            if bigPrimitiveRoot >= (minVal * 0.8) and bigPrimitiveRoot <= maxVal:
                return(bigPrimitiveRoot)
        
        m += 1

def privateKeyGenerator(prime):
    privateKeyA = random.randint(minVal, prime - 1)
    privateKeyB = random.randint(minVal, prime - 1)

    while privateKeyA == privateKeyB:
        privateKeyB = random.randint(minVal, prime - 1)

    return(privateKeyA, privateKeyB)

def publicKeyGenerator(a, privateKeyA, privateKeyB, prime):
    publicKeyA = squareAndMultiply(a, privateKeyA, prime)
    publicKeyB = squareAndMultiply(a, privateKeyB, prime)

    return(publicKeyA, publicKeyB)

def secretKeyGenerator(privateKeyA, publicKeyB, prime):
    secretKey = squareAndMultiply(publicKeyB, privateKeyA, prime)

    return(secretKey)
