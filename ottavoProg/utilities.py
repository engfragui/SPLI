from bitarray import bitarray

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

def get_string_from_file(filename):

    #open source file
    file = open(filename, 'rb')

    str = ''

    while(1):
        b = file.read(1) #read a byte
        if not b:
            break
        str = str + get_byte_array(b)

    file.close()

    return str

def write_str_on_file(filename, str):

    #open destination file
    file = open(filename, 'wb')

    ba = bitarray(str) #obtain bitarray object from string i
    file.write(ba.tobytes()) #write bytes on file

    file.close()

def get_decimal_from_file(file):

    binario = get_string_from_file(file)

    decimale = int(str(binario),2)

    return decimale

def write_decimal_on_file(decimale, file):

    binario = bin(decimale)[2:]

    while (len(binario) % 8) != 0:
        binario = '0' + binario

    write_str_on_file(file, binario)