# python 3.3.0
# please download bitarray from https://pypi.python.org/pypi/bitarray/

"""
Before running this main you have to:
1) Create a directory with name "example"
2) Put file "example.txt" inside the directory --> directory and file has to have the same name

At the and, in the directory you will see "example_encrypt.txt", "example_decrypt.txt", "example_guessed.txt"
"""

import encryptAndDecrypt
import guessDecrypt
import checking

import random
import os

if __name__ == "__main__":

    print ("\nWelcome!\n")

    file = 'foto.jpg'
    len_chunk_bit = 512
    times = 16

    K = ''
    for i in range(0,64):
        K = K + str(random.randrange(0, 2))
    print(K)

    #prepare file names
    file_split = file.split(".")
    file_name = file_split[0]
    file_ext = file_split[1]
    file_encrypt = file_name + "_encrypt." + file_ext
    file_decrypt = file_name + "_decrypt." + file_ext
    file_guessed = file_name + "_guessed." + file_ext

    #change directory
    os.chdir(file_name)

    #encryption algorithm --> creation of file_encrypt
    encryptAndDecrypt.encryption(file, len_chunk_bit, times, K, file_encrypt)

    #decryption algorithm --> creation of file_decrypt
    encryptAndDecrypt.decryption(file_encrypt, K, file_decrypt)

    #checking if file and decrypted file are the same
    checking.checkDecrypt(file, file_decrypt)

    #guessing algorithm --> creation of file_guess
    guessDecrypt.guess(file_encrypt, file_guessed)

    #comparison between file decrypted file and guessed file
    checking.checkGuessed(file_decrypt, file_guessed)