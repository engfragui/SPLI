from bitarray import bitarray
import time

def bits(byte):
    for i in range(8):
        yield (ord(byte) >> i) & 1

def get_byte_array(byte):
    """
    Returns an array of bit from a byte
    """
    vett = ''
    for b in bits(byte):
        vett = str(b) + vett
    return vett

def complete_last_chunk(chunks, len_chunk_bit):
    """
    Completes last chunk, giving it same length of other chunks
    """

    last = len(chunks)-1
    while (len(chunks[last]) < len_chunk_bit):
        chunks[last] = chunks[last] + '0'

def get_chunks_from_file(filename, len_chunk_bit):
    """
    Returns an array of chunks
    """

    len_chunk_byte = len_chunk_bit // 8

    #open source file
    file = open(filename, 'rb')

    n=0
    chunk=''
    chunks=[]
    while(1):
        b = file.read(1) #read a byte
        if not b:
            if (chunk!=''):
                chunks.append(chunk)
            break
        chunk = chunk + get_byte_array(b)
        n=n+1
        if n==len_chunk_byte:
            chunks.append(chunk)
            n=0
            chunk=''

    file.close()

    complete_last_chunk(chunks, len_chunk_bit)

    return chunks

def write_chunks_on_file(filename, chunks):

    #open destination file
    file = open(filename, 'wb')

    for i in chunks:
        ba = bitarray(i) #obtain bitarray object from string i
        file.write(ba.tobytes()) #write bytes on file

    file.close()

def xor_strings(xs, ys):
    """
    Returns XOR result from two string
    """
    return "".join(str(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

def generate_keys(K, num_keys):
    """
    Generate keys from K, simply shifting the bits
    """

    keys=[]

    for i in range(0, num_keys):
        key = K[(i % len(K)):] + K[:(i % len(K))]
        keys.append(key)

    return keys

def generate_random_key(len_K):
    """
    Generate a random number
    """

    now = time.time()

    enter = input("Press enter to stop the counter! ")

    duration = time.time() - now

    print(str(duration) + ' seconds')

    # se voglio una chiave lunga 32 bit
    # dovro' prendere 32 // 4 = 8 cifre di duration
    num_figures = len_K // 4

    decimals = ("%.*f" % (num_figures, duration)).split(".")[-1]

    K = ''
    for d in decimals:
        key = str(bin(int(d))[2:])
        while(len(key) < 4):
            key = '0' + key
        K = K + key

    print('Key: ' + K)

    print("")

    return(K)