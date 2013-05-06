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