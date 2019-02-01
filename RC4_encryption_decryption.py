#!usr/bin/python
import binascii
import hashlib


def RepresentsInt(s):
    try: 
	#check if a number is either integer (True) or float (False)
        int(s)
        return True
    except ValueError:
        return False


def onlyBytes(listA):
	listB=[]
	#represent a sequence or a string or a number to only bytes
	for x in listA:
		if not(RepresentsInt(x)):
			pass
		else:
			listB.append(x)
	return listB


def KSA(key):
	keylength = len(key)
	#initialize S
    	S = range(256)
    	j = 0
    	for i in range(256):
        	j = (j + S[i] + key[i % keylength]) % 256
        	S[i], S[j] = S[j], S[i]  # swap
    	return S

#stream generator
def PRGA(S,text):
	i = 0
    	j = 0
	k=[]
    	for x in range(len(text)):
		i = (i + 1) % 256
		j = (j + S[i]) % 256
		S[i], S[j] = S[j], S[i]  # swap
		K = S[(S[i] + S[j]) % 256]
		k.append(K)
	return k

def convertText(s):
        return [ord(c) for c in s]

def initialize(text,key):
	print 'The text for decryption/encryption is: ',text,' , with the key:  ',key,'\n'
	#textBytes = bin(int(binascii.hexlify(text), 16))
	#keyBytes = bin(int(binascii.hexlify(key), 16))
	e=0
	key  = convertText(key)
	text = convertText(text)
	#just to check 
	textBytes = onlyBytes(textBytes)
	keyBytes = onlyBytes(keyBytes)
	print 'The text in bytes: ',textBytes,'\n'
	for x in range(len(text)%8):
	
		textLetterBytes.append(textBytes[e:e+8])
		e+=8
	print textLetterBytes
	
	#random key stream in order to randomize the procedure
	S = KSA(key)
	random=[]
	for x in range(257):
		#call the random key stream byte 256 before encryption/decryption
		random = PRGA(S,text)
	cipherText=[]
	for x in range(len(text)):
		cipherText.append(chr(text[x]^random[x]))#XOR logical gate
	result = ''.join(cipherText)
	print 'The text after RC4 procedure is: ' ,result,'\n'
	return result
	

def decryptUniversity():
	f=open('/home/manos/rc4(3).enc','r')
	textHex = f.read()
	print textHex ,'\n'
	textHex1 = hashlib.sha256(textHex).hexdigest()
	print 'sha256 is: ' ,textHex1,'\n'
#[0xac,0xe2,0xd5,0xa0,0x81,0x7d,0x3d,0x45,0x5b,0xe3,0x99,0x5f,0x52,0xa3,0x23,0x37,0x04,0x9d,0xad,0x83,0x66,0xff,0x68,0xde,0x32,0x47,0x15,0x04,0x6b,0xfe,0xc2,0x20]
	return textHex

def main():
	#text = raw_input('Give me the text: ')
	text = decryptUniversity()
	key = raw_input('Give me the key: ')
	result = initialize(text,key)
	flag1  = raw_input('If you want to encrypt/decrypt again press 1  ')
	print 'Your answer: ',flag1
	if(flag1=='1'):
		key = raw_input('Give me the key: ')
		flag2 = raw_input('If you want to encrypt/decrypt the previous result press 1  ')
		if(flag2=='1'):
			initialize(result,key)
			#print 'Encryption/Decryption the text: ',result,' with the key: ',key,'\n'
		else:
			text = raw_input('Give me the text: ')
			initialize(text,key)
	
	

main()


