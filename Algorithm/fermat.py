import random

def squareAndMultiply(base, exponent, modulus):
    bit = bin(exponent)[2:]
    z = 1

    for bits in bit:
        if bits == '0':
            z = z * z % modulus
        else: z = base * z * z % modulus

    return(z)

def fermat(n):
    k = 0
    while k <= 3:
        a = random.randint(2, n - 2)
        if squareAndMultiply(a, n - 1, n) != 1:
            return("Komposit")
        else:
            k += 1
            if k >= 3:
                return("Kemungkinan Prima")