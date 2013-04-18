import utilities
import hashlib

def f(message, key):
    """
    md5(message XOR key)
    """

    key_same = utilities.same_length(key, message)

    message = utilities.xor_strings(message, key_same)

    #message = hashlib.md5(message.encode()).hexdigest() #TODO capire come fare questa cosa dell'md5

    return message

def split_and_shuffle(chunk, len_chunk_bit, key):

    h = len_chunk_bit // 2

    L = chunk[0:h]
    R = chunk[h:len(chunk)]

    L_new = R

    func = f(R, key)
    func_same = utilities.same_length(func, L)
    R_new = utilities.xor_strings(L, func_same)

    new_chunk = L_new + R_new

    return new_chunk

def encryption(file, len_chunk_bit, times, K, file_encrypt):
    """ Execute the operations in order to encrypt a file """

    print ("\n-----Encryption-----\n")

    chunks = utilities.get_chunks_from_file(file, len_chunk_bit)

    keys = utilities.generate_keys(K, times) #generate keys from K

    new_chunks=[]

    #Feistel algorithm to encrypt file
    for c in chunks: #for each chunk
        for i in range(0,times): #for numbers of times
            c = split_and_shuffle(c, len_chunk_bit, keys[i]) #shuffle c in order to encrypt
        new_chunks.append(c)

    utilities.write_chunks_on_file(file_encrypt, new_chunks)

    print ("Encryption done")

def decryption(file_encrypt, K, file_decrypt):
    """ Execute the operations in order to decrypt a file """

    print ("\n-----Decryption-----\n")

    #TODO

    print ("Decryption done")