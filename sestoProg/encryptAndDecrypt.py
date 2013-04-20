import utilities
import hashlib
from bitarray import bitarray

def f(message, key):
    """
    md5(message XOR key)
    """

    key_same = utilities.same_length(key, message)

    message_xor = utilities.xor_strings(message, key_same)

    ba = bitarray(message_xor) #obtain bitarray object from string message
    bytes = ba.tobytes() #get bytes

    md5 = hashlib.md5()
    data = bytes
    md5.update(data)
    dig = md5.digest()
    D = '' #binary representation of dig
    for i in range(0,len(dig)):
        d = bin(dig[i])[2:] #binary representation of dig[i]
        while(len(d) < 8):
            d = '0' + d
        D = D + d

    D_same = utilities.same_length(D, message)

    return D_same

def split_and_shuffle_encrypt(chunk, len_chunk_bit, key):
    """
    Li+1 = R_i
    R_i+1 = L_i XOR f(R_i)

    """

    h = len_chunk_bit // 2

    L = chunk[0:h]
    R = chunk[h:len(chunk)]

    L_new = R

    func = f(R, key)
    func_same = utilities.same_length(func, L)
    R_new = utilities.xor_strings(L, func_same)

    new_chunk = L_new + R_new

    return new_chunk

def split_and_shuffle_decrypt(chunk, len_chunk_bit, key):
    """
    R_i = Li+1
    L_i = Ri+1 XOR f(L_i+1)

    """

    h = len_chunk_bit // 2

    L = chunk[0:h]
    R = chunk[h:len(chunk)]

    func = f(L, key)
    func_same = utilities.same_length(func, R)
    L_new = utilities.xor_strings(R, func_same)

    R_new = L

    new_chunk = L_new + R_new

    return new_chunk

def algorithm(file_in, len_chunk_bit, times, K, file_out, mode):

    chunks = utilities.get_chunks_from_file(file_in, len_chunk_bit)

    keys = utilities.generate_keys(K, times) #generate keys from K

    new_chunks=[]

    #Feistel algorithm
    for c in chunks: #for each chunk
        for i in range(0,times): #for numbers of times
            if(mode=='encrypt'):
                c = split_and_shuffle_encrypt(c, len_chunk_bit, keys[i]) #shuffle c in order to encrypt
            else:
                c = split_and_shuffle_decrypt(c, len_chunk_bit, keys[len(keys)-1-i]) #shuffle c in order to decrypt
        new_chunks.append(c)

    utilities.write_chunks_on_file(file_out, new_chunks)

def encryption(file, len_chunk_bit, times, K, file_encrypt):
    """ Execute the operations in order to encrypt a file """

    algorithm(file, len_chunk_bit, times, K, file_encrypt, 'encrypt')

def decryption(file_encrypt, len_chunk_bit, times, K, file_decrypt):
    """ Execute the operations in order to decrypt a file """

    algorithm(file_encrypt, len_chunk_bit, times, K, file_decrypt, 'decrypt')