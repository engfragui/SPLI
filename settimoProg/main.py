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
import utilities
import os

if __name__ == "__main__":

    print ("\nWelcome!\n")

    file = 'immagine.jpg' #'testo.txt'
    len_chunk_bit = 32

    len_K = len_chunk_bit #lunghezza chiave = lunghezza del chunk
    print("Generating key KA...")
    KA = utilities.generate_random_key(len_K)
    print("Generating key KB...")
    KB = utilities.generate_random_key(len_K)

    #prepare file names
    file_split = file.split(".")
    file_name = file_split[0]
    file_ext = file_split[1]
    file_encryptA = file_name + "_encryptA." + file_ext
    file_encryptB = file_name + "_encryptB." + file_ext
    file_decryptA = file_name + "_decryptA." + file_ext
    file_decryptB = file_name + "_decryptB." + file_ext

    #change directory
    os.chdir(file_name)

    encryptAndDecrypt.encryption(file, len_chunk_bit, KA, file_encryptA)

    encryptAndDecrypt.encryption(file_encryptA, len_chunk_bit, KB, file_encryptB)

    encryptAndDecrypt.decryption(file_encryptB, len_chunk_bit, KA, file_decryptA)

    encryptAndDecrypt.decryption(file_decryptA, len_chunk_bit, KB, file_decryptB)

    print('Job done!')