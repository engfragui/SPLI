import utilities
import encryptAndDecrypt

def guess(file_encrypt, len_chunk_bit, times, len_K, file_guessed, md5_file):
    """ Guesses the decryption of file_encrypt, based on letters frequency """

    print ("\n-----Guessing-----\n")

    K = []
    len_int = 2 ** len_K
    #generate all possible keys of len_K
    for i in range(0,len_int):
        key = bin(i)[2:]
        while(len(key) < len_K):
            key = '0' + key
        K.append(key)

    #prepare file names
    file_split = file_guessed.split(".")
    file_name = file_split[0]
    file_ext = file_split[1]
    file_guessed_incipit = file_name + "_"

    t=0

    for k in K: #for each key
        t = t+1
        print('Attempt n.' + str(t) + ' - key: ' + k)
        file_i = file_guessed_incipit + k + '.' + file_ext
        encryptAndDecrypt.decryption(file_encrypt, len_chunk_bit, times, k, file_i)
        print('Guessed file has md5: ' +  utilities.get_md5_file(file_i))
        if (utilities.get_md5_file(file_i) == md5_file):
            print('Successful attempt!')
            break
        print('Failed attempt!\n')