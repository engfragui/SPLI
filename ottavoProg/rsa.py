import fractions
import random

def is_prime(a):
    return all(a % i for i in range(2, a))

def generate_prime_number():

    p = random.randint(100,1000)
    while not(is_prime(p)):
        p = random.randint(100,1000)

    return p

def product_n(p,q):

    return p*q

def Fn_Eulero(p,q):

    return (p-1)*(q-1)

def encrypt_key(Fn):
    """
    genero e tale che (e,Fn)=1
    """

    e = random.randint(100,1000)

    while fractions.gcd(e,Fn) != 1:
        e = random.randint(100,1000)

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

def encrypt_message(M,e,n):

    return (M**e) % n

def decrypt_message(C,d,n):

    return (C**d) % n