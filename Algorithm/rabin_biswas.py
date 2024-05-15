def encrypt(inputMessage, Key):
    asciiArray = []
    Q = []
    R = []
    ciphertext = []

    for char in inputMessage:
        inputMessageToASCII = ord(char)
        asciiArray.append(inputMessageToASCII)

    for i in range(len(asciiArray)):
        Q.append(int(asciiArray[i] ** 2 / Key))
        R.append(asciiArray[i] ** 2 % Key)

    for i in range(len(Q)):
        ciphertext.append((Q[i], R[i]))

    return(ciphertext)

def decrypt(ciphertext, Key):
    decryptASCII = []

    for i in range(len(ciphertext)):
        decryptASCII.append((ciphertext[i][0] * Key + ciphertext[i][1]) ** 0.5)

    for i in range(len(decryptASCII)):
        decryptASCII[i] = chr(int(decryptASCII[i]))

    plaintext = ''.join(decryptASCII)

    return(plaintext)

def textToArray(inputText):
    inputText = inputText.strip('[] ')
    splitInputText = inputText.split('), ')

    ciphertextArr = []

    for stringInputText in splitInputText:
        x, y = stringInputText.strip('()').split(', ')
        ciphertextArr.append((int(x), int(y)))

    return(ciphertextArr)

input_message = 'THORIQ'
kunci = 334

# enkripsi
ciphertext = encrypt(input_message, kunci)
print("Ciphertext :", ciphertext)

# dekripsi
decryptedCt = decrypt(ciphertext, kunci)
print("Decrypted Ciphertext :", decryptedCt)