def checkDecrypt(file1, file2):
    """ Checks if file1 is equal to file2 """

    print "\n-----Checking decryption-----\n"

    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    t1 = f1.read()
    t2 = f2.read()
    f1.close
    f2.close
    if t1 == t2:
        print "Correct decryption"
    else:
        print 'Uncorrect decryption'

def checkGuessed(file_decrypt, file_guessed):
    """ Checks the differences between file_decrypt and file_guessed """

    print "\n-----Checking guess-----\n"

    sameLetters=0
    sameWords=0
    word1 = ""
    word2 = ""
    words=0
    fd = open(file_decrypt, 'r')
    fg = open(file_guessed, 'r')
    td = fd.read()
    tg = fg.read()
    fd.close
    fg.close

    l = len(td)

    print "Letters number: " + str(l)

    for i in range(l):
        if (td[i] == tg[i]):
            sameLetters=sameLetters+1
        if td[i] != " ":
            word1 = word1 + td[i]
            word2 = word2 + tg[i]
        else: #space
            if (word1 == word2):
                sameWords = sameWords + 1
            words = words + 1
            word1 = ""
            word2 = ""

    percLetters = (sameLetters + 0.0) * 100 / l
    percLetters = "%.2f" % percLetters

    print "Guessed letters percentage: " + str(percLetters) + " %"

    percWords = (sameWords + 0.0) * 100 / words
    percWords = "%.2f" % percWords

    print "Guessed words percentage: " + str(percWords) + " %"