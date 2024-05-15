import math
import time

def babyStepGiantStep(q, a, publicKey):
    m = math.ceil(math.sqrt(q))
    
    tableAJ = {}
    
    for j in range(m):
        aj = squareAndMultiply(a, j, q)
        tableAJ[aj] = j

    am = negativeExponent(a, -m, q)

    y = publicKey

    for i in range(m):
        jTarget = tableAJ.get(y)
        if jTarget is not None:
            return(i * m + jTarget % q)
        y = (y * am) % q

def negativeExponent(base, exponent, modulus):
    if exponent > -1:
        exponent = exponent - (2 * exponent)
    
    totient = modulus - 1

    x = exponent + totient
    y = squareAndMultiply(base, x, modulus)

    return(y)

def squareAndMultiply(base, exponent, modulus):
    bit = bin(exponent)[2:]
    z = 1

    for bits in bit:
        if bits == '0':
            z = z * z % modulus
        else:
            z = base * z * z % modulus
    
    return(z)

def calcSK(publicKey, privateKey, q):
    secretKey = squareAndMultiply(publicKey, privateKey, q)

    return(secretKey)

q = 922615262936663
a = 849545799838169
publicKey = 827474071641716
publicKey2 = None

session_start = time.time()

privateKey = babyStepGiantStep(q, a, publicKey)
print(privateKey)

# secretKey = calcSK(publicKey2, privateKey, q)
# print(secretKey)

session_end = time.time()

print("Execution time", session_end - session_start, "secs")