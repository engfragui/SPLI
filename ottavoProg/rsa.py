import fractions
import random
import utilities

def product_n(p,q):

    return p*q


def Fn_Eulero(p,q):

    return (p-1)*(q-1)


def encrypt_key(Fn):
    """
    genero e tale che (e,Fn)=1
    """

    e = random.randint(Fn-(Fn//100),Fn)

    while fractions.gcd(e,Fn) != 1:
        e = random.randint(Fn-(Fn//100),Fn)

    return e


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


def decrypt_key(e,Fn):
    """
    calcolo d tale che ed = 1 (mod Fn)
    """

    return modinv(e,Fn)


def modular_exponent(base, exponent, mod):
    """
    Modular exponentiation through binary decomposition
    Scelgo la potenza modulare piuttosto che fare a**b mod m
    Perchè l'elevamento a potenza è molto dispendioso in termini di tempo
    """

    exponent = bin(exponent)[2:][::-1]

    x = 1
    power = base % mod
    for i in range(0, len(exponent)):
        if exponent[i] == '1':
            x = (x * power) % mod
        power = (power ** 2) % mod
    return x


def preliminaries(file):

    #database con primi grandi
    primes = [2 ** 521 - 1,
              2 ** 4253 - 1,
              2 ** 11213 - 1,
              2 ** 44497 - 1,
              2 ** 1398269 - 1,
              2 ** 3021377 - 1,
              2 ** 20996011 - 1,
              2 ** 30402457 - 1,
              2 ** 32582657 - 1]

    M = utilities.get_decimal_from_file(file)

    print("\n\n-----Preliminaries-----")

    i=0
    p=1
    q=1
    n = product_n(p,q)
    while n < M:
        #genero primi p,q
        p = primes[i]
        q = primes[i+1]
        n = product_n(p,q)
        i=i+1

    print('p = ' + str(p))
    print('q = ' + str(q))

    print('n = ' + str(n))

    #calcolo Fn
    Fn = Fn_Eulero(p,q)
    print('Fn = ' + str(Fn))

    #genero chiave pubblica e
    e = encrypt_key(Fn)
    print('e = ' + str(e))

    #calcolo chiave privata d
    d = decrypt_key(e,Fn)
    print('d = ' + str(d))

    return (p, q, n, Fn, e, d)


def encryption(file,e,n,file_encrypt):

    print("\n-----Encryption-----")

    #estrapolo numero decimale M partendo dal file
    M = utilities.get_decimal_from_file(file)
    print('M = ' + str(M))

    if (M > n):
        print('Il messaggio M non può essere più lungo del prodotto n --> devo aumentare p e q')
        return False

    #cripto messaggio
    C = modular_exponent(M,e,n)
    print('C = ' + str(C))

    #scrivo decimale C su file
    utilities.write_decimal_on_file(C, file_encrypt)

    return True


def decryption(file_encrypt,d,n,file_decrypt):

    print("\n-----Decryption-----")

    #calcolo numero decimale C partendo dal file
    C = utilities.get_decimal_from_file(file_encrypt)

    #decripto messaggio
    D = modular_exponent(C,d,n)
    print('D = ' + str(D))

    #scrivo decimale D su file
    utilities.write_decimal_on_file(D, file_decrypt)


def checking(file,file_decrypt):

    print('\n-----Checking-----')

    if utilities.get_md5_file(file) == utilities.get_md5_file(file_decrypt):
        print('Original file and decrypted file have same md5')
    else:
        print('Original file and decrypted file have different md5')