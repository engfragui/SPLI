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

    e = random.randint(1,Fn)

    while fractions.gcd(e,Fn) != 1:
        e = random.randint(1,Fn)

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
    Modular exponentiation through binary decomposition.
    """

    exponent = bin(exponent)[2:][::-1]

    x = 1
    power = base % mod
    for i in range(0, len(exponent)):
        if exponent[i] == '1':
            x = (x * power) % mod
        power = (power ** 2) % mod
    return x

def encryption(file,e,n,file_encrypt):

    print("\n-----Encryption-----")

    #estrapolo numero decimale M partendo dal file
    M = utilities.get_decimal_from_file(file)
    print('M = ' + str(M))

    if (M > n):
        print('Il messaggio M non può essere più lungo del prodotto n')
        exit(0)

    #cripto messaggio
    C = modular_exponent(M,e,n)
    print('C = ' + str(C))

    #scrivo decimale C su file
    utilities.write_decimal_on_file(C, file_encrypt)

def decryption(file_encrypt,d,n,file_decrypt):

    print("\n-----Decryption-----")

    #calcolo numero decimale C partendo dal file
    C = utilities.get_decimal_from_file(file_encrypt)

    #decripto messaggio
    D = modular_exponent(C,d,n)
    print('D = ' + str(D))

    #scrivo decimale D su file
    utilities.write_decimal_on_file(D, file_decrypt)