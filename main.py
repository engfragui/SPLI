"""
Before running this main you have to:
1) Create a directory with name "example"
2) Put file "example.txt" inside the directory --> directory and file has to have the same name

At the and, in the directory you will see "example_encrypt.txt", "example_decrypt.txt", "example_guessed.txt"

If you want to color your output:
print '\033[95m' + "prova" + '\033[0m' --> fucsia
print '\033[94m' + "prova" + '\033[0m' --> blu
print '\033[92m' + "prova" + '\033[0m' --> verde
print '\033[91m' + "prova" + '\033[0m' --> rosso
"""

import encryptAndDecrypt
import guessDecrypt
import checking

import os

if __name__ == "__main__":

    print "\nWelcome!\n"

    file = raw_input("Insert file name: ")

    print ""

    K = int(raw_input("Insert secret key K: "))

    print ""

    #prepare file names
    file_split = file.split(".")
    file_name = file_split[0]
    file_encrypt = file_name + "_encrypt.txt"
    file_decrypt = file_name + "_decrypt.txt"
    file_guessed = file_name + "_guessed.txt"

    #change directory
    os.chdir(file_name)

    #encryption algorithm --> creation of file_encrypt
    encryptAndDecrypt.encryption(file, K, file_encrypt)

    #decryption algorithm --> creation of file_decrypt
    encryptAndDecrypt.decryption(file_encrypt, K, file_decrypt)

    #checking if file and decrypted file are the same
    checking.checkDecrypt(file, file_decrypt)

    #guessing algorithm --> creation of file_guess
    guessDecrypt.guess(file_encrypt, file_guessed)

    #comparison between file decrypted file and guessed file
    checking.checkGuessed(file_decrypt, file_guessed)