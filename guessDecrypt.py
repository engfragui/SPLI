import string

def isLower(ch):
    return string.find(string.lowercase, ch) != -1

def isUpper(ch):
    return not isLower(ch)

def gimmeEmptyStat():
    """ Returns an empty array with letters """

    return [['a', 0], ['b', 0], ['c', 0], ['d', 0], ['e', 0],
            ['f', 0], ['g', 0], ['h', 0], ['i', 0], ['j', 0],
            ['k', 0], ['l', 0], ['m', 0], ['n', 0], ['o', 0],
            ['p', 0], ['q', 0], ['r', 0], ['s', 0], ['t', 0],
            ['u', 0], ['v', 0], ['w', 0], ['x', 0], ['y', 0], ['z', 0]]

def gimmeStatArray():
    """ Returns an array with statistics of letters """

    return [['a', 11.70], ['b', 0.95], ['c', 4.5], ['d', 3.73], ['e', 11.74],
            ['f', 0.92], ['g', 1.64], ['h', 1.54], ['i', 11.28], ['j', 0.49],
            ['k', 0.3], ['l', 5.62], ['m', 3.05], ['n', 6.88], ['o', 9.83],
            ['p', 3.01], ['q', 0.5], ['r', 6.51], ['s', 4.98], ['t', 6.37],
            ['u', 3.05], ['v', 2.10], ['w', 0.2], ['x', 0.1], ['y', 0.4], ['z', 0.51]]

def orderedStatArray(statArray):
    """ Returns an array of letters and their frequency, ordered by fixed letters frequency """

    ordered = sorted(statArray, key=lambda statArray: statArray[1], reverse=True)

    return ordered

def getStatOfText(file_encrypt):
    """ Returns an array of letters and their frequency, ordered by text letters frequency """

    countStat = gimmeEmptyStat()

    fe = open(file_encrypt, 'r')
    te = fe.read()
    fe.close

    for i in range(len(te)):
        c = te[i]
        for j in range(len(countStat)):
            if isUpper(c):
                c = c.lower()
            if c == countStat[j][0]:
                countStat[j][1] = countStat[j][1] + 1

    return countStat

def writeGuessedFile(fileEncrypt, fileGuessed, fixedStat, textStat):

    f = open(fileEncrypt, 'r')
    o = open(fileGuessed, 'w')
    t = f.read()
    f.close()

    found = False
    strout = ''

    wasUpper = False

    for c in t:

        for f in range(len(textStat)):
            if isUpper(c):
                c = c.lower()
                wasUpper = True
            if c == textStat[f][0]:
                if wasUpper:
                    strout += fixedStat[f][0].upper()
                else:
                    strout += fixedStat[f][0]
                found = True

        if found == False:
            strout += c
        found = False
        wasUpper = False

    o.write(strout)
    o.close()

def guess(file_encrypt, file_guessed):
    """ Guesses the decryption of file_encrypt, based on letters frequency """

    print "\n-----Guessing-----\n"

    fixedStat = gimmeStatArray()
    orderedFixedStat = orderedStatArray(fixedStat)

    l=''
    stampa=''
    for l in orderedFixedStat:
         stampa = stampa + l[0] + " "
    print 'Statistiche fisse: ' + stampa

    textStat = getStatOfText(file_encrypt)
    orderedTextStat = orderedStatArray(textStat)

    l=''
    stampa=''
    for l in orderedTextStat:
        stampa = stampa + l[0] + " "
    print 'Statistiche testo: ' + stampa

    writeGuessedFile(file_encrypt, file_guessed, orderedFixedStat, orderedTextStat)


