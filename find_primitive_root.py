def squareAndMultiply(base, exponent, modulus):
    bit = bin(exponent)[2:]
    z = 1

    for bits in bit:
        if bits == '0':
            z = z * z % modulus
        else: z = base * z * z % modulus

    return(z)

def findPrimeFactors(n):
    primeFactors = []

    while(n % 2 == 0):
        primeFactors.append(2)
        n = n // 2

    for i in range(3, int(n ** 0.5), 2):
        while(n % i == 0):
            primeFactors.append(i)
            n = n // i

    if(n > 2):
        primeFactors.append(n)

    return(list(set(primeFactors)))

def findPowers(n, set):
    powers = []
    for i in range(len(set)):
        power = n // set[i]
        powers.append(power)

    return(powers)

def findPrimitiveRoot(n):
    s = n - 1

    primeFactors = findPrimeFactors(s)

    powers = findPowers(s, primeFactors)

    for i in range(2, n):
        for j in range(len(powers)):
            flag = False
            if(squareAndMultiply(i, powers[j], n) == 1):
                flag = True
                break

        if(flag == False):
            return(i)