import utilities

def f(message, key):
    """
    message XOR key
    """

    return utilities.xor_strings(message, key)

def algorithm(file_in, len_chunk_bit, K, file_out):

    chunks = utilities.get_chunks_from_file(file_in, len_chunk_bit)

    num_keys = len(chunks) #una chiave per ogni chunk

    keys = utilities.generate_keys(K, num_keys) #generate keys from K

    new_chunks=[]

    i=0
    for c in chunks: #for each chunk
        c = f(c, keys[i]) #primo chunk con prima chiave, secondo chunk con seconda chiave, ecc
        new_chunks.append(c)
        i = i + 1

    utilities.write_chunks_on_file(file_out, new_chunks)

def encryption(file_in, len_chunk_bit, K, file_encrypt):
    """ Execute the operations in order to encrypt a file """

    algorithm(file_in, len_chunk_bit, K, file_encrypt)

def decryption(file_in, len_chunk_bit, K, file_decrypt):
    """ Execute the operations in order to decrypt a file """

    algorithm(file_in, len_chunk_bit, K, file_decrypt)