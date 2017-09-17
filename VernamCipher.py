#!usr/bin/python
import binascii

plainText='informationsecurity'
key1='vlaksjdhfgqodzmxncb'
print 'The plain text is: ' , plainText
print'The first key is: ' , key1 , '\n'

plainText = bin(int(binascii.hexlify('informationsecurity'), 16))
key = bin(int(binascii.hexlify('vlaksjdhfgqodzmxncb'), 16))
print 'Plain text in bits:  ' , plainText , '\n'
print 'Key in bits: '  , key , '\n'


#XOR logical gate
def xor(m, k):
    r = []
    for i, j in zip(m, k):
		if(i.isalpha() and j.isalpha()):
			r.append(i)
		else:
        		r.append(str(int(i) ^ int(j)))  # xor between bits i and j
    return "".join(r)

result = xor(plainText,key)
n = int(result, 2)
print 'XOR result for the encryption with the normal key: ' , result , '\n'
print 'Encrypted text: ' , binascii.unhexlify('%x' % n) , 
decryption = xor(result,key)
print ' \n '
print 'Decryption result: ' , decryption , '\n'
l = int(decryption,2)
print 'Decrypted text with the normal key: ' , binascii.unhexlify('%x' % l) , '\n'


print'Decryption with the alternative key \n'
alternativeKey = bin(int(binascii.hexlify('tlftrffwmixor|{xbch'), 16))
print 'Alternative key in bits: ' , alternativeKey , '\n'
result1 = xor(result,alternativeKey)
k = int(result1,2)
print 'Decrypted text with the alternative key : ' , binascii.unhexlify('%x' % k)
