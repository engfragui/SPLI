import string

def isLower(ch):
    return string.find(string.lowercase, ch) != -1

def isUpper(ch):
    return not isLower(ch)

def gimmeOrderedLetterArray():
    """ Returns an array with ordered letters from a to z """
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def rotateLetterArray(letters, K):
    """ Returns a rotated version of letters, according to the key K """
    return letters[K:] + letters[:K]

def createMatch(letters):
    """ Returns an array with couples of chars, coupled by the encryption """
    ordered = gimmeOrderedLetterArray()
    matches = []
    for i in range(len(letters)):
        couple = [ordered[i],letters[i]]
        matches.append(couple)
    return matches

def gimmeMatch(K, mode):
    """ Returns an array with couples of chars, from the key K and the mode (encrypt or decrypt) """
    if mode == 'decrypt':
        K = -K
    ordered = gimmeOrderedLetterArray()
    letters = rotateLetterArray(ordered, K)
    return createMatch(letters)

def algorithm(file_input, file_output, matches):
    """ Execute the algorithm of encryption or decryption using matches array """
    f = open(file_input, 'r')
    o = open(file_output, 'w')
    t = f.read()
    f.close()

    found = False
    wasUpper = False
    strout = ''

    for c in t:

        for m in range(len(matches)):
            if isUpper(c):
                c = c.lower()
                wasUpper = True
            if c == matches[m][0]:
                if wasUpper:
                    strout += matches[m][1].upper()
                else:
                    strout += matches[m][1]
                found = True

        if found == False:
            strout += c
        found = False
        wasUpper = False

    o.write(strout)
    o.close()

def encryption(file, K, file_encrypt):
    """ Execute the operations in order to encrypt a file """

    print "\n-----Encryption-----\n"

    matches = gimmeMatch(K, 'encrypt')

    algorithm(file, file_encrypt, matches)

    print "Encryption done"

def decryption(file_encrypt, K, file_decrypt):
    """ Execute the operations in order to decrypt a file """

    print "\n-----Decryption-----\n"

    matches = gimmeMatch(K, 'decrypt')

    algorithm(file_encrypt, file_decrypt, matches)

    print "Decryption done"