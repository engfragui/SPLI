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

import utilities
import os
import rsa

if __name__ == "__main__":

    print ("\nWelcome!\n")

    #file = 'immagine.jpg'
    file = 'testo.txt'

    #prepare file names
    file_split = file.split(".")
    file_name = file_split[0]
    file_ext = file_split[1]
    file_encrypt = file_name + "_encrypt." + file_ext
    file_decrypt = file_name + "_decrypt." + file_ext

    #change directory
    os.chdir(file_name)


    #CALCOLI PRELIMINARI

    #genero primi p,q
    p = rsa.generate_prime_number()
    print('p = ' + str(p))
    q = rsa.generate_prime_number()
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

    print("")


    #ENCRYPTION

    #estrapolo numero decimale M partendo dal file
    M = utilities.get_decimal_from_file(file)
    print('M = ' + str(M))

    #cripto messaggio
    C = rsa.encrypt_message(M,e,n)
    print('C = ' + str(C))

    #scrivo decimale C su file
    utilities.write_decimal_on_file(C, file_encrypt)

    print("")


    #DECRYPTION

    #calcolo numero decimale C partendo dal file
    C = utilities.get_decimal_from_file(file_encrypt)

    #decripto messaggio
    D = rsa.decrypt_message(C,d,n)
    print('D = ' + str(D))

    #scrivo decimale D su file
    utilities.write_decimal_on_file(D, file_decrypt)


    print('Job done!')