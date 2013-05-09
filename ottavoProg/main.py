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

import os
import rsa
import time

if __name__ == "__main__":

    print ("\nWelcome!")

    file = 'immagine.png'
    #file = 'immagine2.jpg'
    #file = 'testo.txt'

    #prepare file names
    file_split = file.split(".")
    file_name = file_split[0]
    file_ext = file_split[1]
    file_encrypt = file_name + "_encrypt." + file_ext
    file_decrypt = file_name + "_decrypt." + file_ext

    #change directory
    os.chdir(file_name)

    start = time.time()


    #CALCOLI PRELIMINARI
    (p, q, n, Fn, e, d) = rsa.preliminaries(file)

    #ENCRYPTION
    rsa.encryption(file, e, n, file_encrypt)

    #DECRYPTION
    rsa.decryption(file_encrypt, d, n, file_decrypt)

    #CHECKING
    rsa.checking(file,file_decrypt)


    stop = time.time()

    print('Time spent: ' + "%.2f" % (stop-start) + ' seconds')


    print('\n\nJob done!')