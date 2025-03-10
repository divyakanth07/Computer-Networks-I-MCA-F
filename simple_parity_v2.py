import bitarray as ba 
data = ba.bitarray(endian='little')  
data.frombytes('Secret message!'.encode()) 

def parity(bitarray):
    print("Original:\t\t\t{}".format(bitarray))
    pbit = 0
    count = bitarray.count(1)
    print("Counted {} 1's in bitarray".format(count))
    if (count % 2) != 0:
        pbit = 1
    print("Parity bit is {}".format(pbit))
    bitarray.append(pbit) 
    print("Parity bitarray: \t{}".format(bitarray))
    return bitarray

parity(data)
