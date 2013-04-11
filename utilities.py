import string

def isLower(ch):
    """ Returns True if the char is lower case """

    return string.find(string.lowercase, ch) != -1

def isUpper(ch):
    """ Returns True if the char is upper case """

    return not isLower(ch)