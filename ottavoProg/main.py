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

if __name__ == "__main__":

    print ("\nWelcome!\n")

    file = 'immagine.png'
    #file = 'testo.txt'

    #prepare file names
    file_split = file.split(".")
    file_name = file_split[0]
    file_ext = file_split[1]
    file_encrypt = file_name + "_encrypt." + file_ext
    file_decrypt = file_name + "_decrypt." + file_ext

    #change directory
    os.chdir(file_name)

    #numeri primi grandini
    #2 ** 521 - 1
    #2 ** 4253 - 1
    #2 ** 11213 - 1
    #2 ** 44497 - 1
    #2 ** 1398269 - 1
    #2 ** 3021377 - 1
    #2 ** 20996011 - 1
    #2 ** 30402457 - 1
    #2 ** 32582657 - 1

    #CALCOLI PRELIMINARI

    #genero primi p,q
    p = 2 ** 521 - 1
    print('p = ' + str(p))
    q = 2 ** 4253 - 1
    print('q = ' + str(q))

    #calcolo n
    n = rsa.product_n(p,q)
    print('n = ' + str(n))

    #calcolo Fn
    Fn = rsa.Fn_Eulero(p,q)
    print('Fn = ' + str(Fn))

    #genero chiave pubblica e
    e = rsa.encrypt_key(Fn)
    print('e = ' + str(e))

    #calcolo chiave privata d
    d = rsa.decrypt_key(e,Fn)
    print('d = ' + str(d))


    #ENCRYPTION
    rsa.encryption(file, e, n, file_encrypt)

    #DECRYPTION
    rsa.decryption(file_encrypt, d, n, file_decrypt)

    print('\nJob done!')

