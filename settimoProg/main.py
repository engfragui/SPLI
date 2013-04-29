# python 3.3.0
# please download bitarray from https://pypi.python.org/pypi/bitarray/
# install bitarray:
#     tar xzf bitarray-0.8.1.tar.gz
#     cd bitarray-0.8.1
#     python3 setup.py install

"""
Before running this main you have to:
1) Create a directory with name "example"
2) Put file "example.ext" inside the directory --> directory and file has to have the same name

At the and, in the directory you will see "example_encrypt.ext", "example_decrypt.ext", "example_guessed.ext", ...
"""

import encryptAndDecrypt
import guessDecrypt
import utilities

import random
import os

if __name__ == "__main__":

    print ("\nWelcome!\n")

    file = 'immagine.jpg' #'testo.txt'
    len_chunk_bit = 512 #typ = 512
    times = 16 #typ = 16

    len_K = 6 #typ = 64, to_guess = 16
    K = ''
    for i in range(0,len_K):
        K = K + str(random.randrange(0, 2))
    print('Key: ' + K)

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

    print ("\nEncryption done")

    #decryption algorithm --> creation of file_decrypt
    encryptAndDecrypt.decryption(file_encrypt, len_chunk_bit, times, K, file_decrypt)

    print ("\nDecryption done")

    #get md5 from file_decrypt
    md5_file = utilities.get_md5_file(file_decrypt)
    print('\nChosen file has md5: ' +  md5_file)

    #guessing algorithm --> creation of file_guess
    guessDecrypt.guess(file_encrypt, len_chunk_bit, times, len_K, file_guessed, md5_file) #you don't know K, just len_K