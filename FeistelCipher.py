#!usr/bin/python
import hashlib
import struct
import itertools

password = raw_input('Give me a password: ')
firstPass = hashlib.sha256(password.encode()).hexdigest()
print 'First sha256 pass: ' , firstPass , '\n'
secondPass = hashlib.sha256(firstPass.encode()).hexdigest()
print 'Second sha256 pass: ' , secondPass , '\n'

#reading the file
fileInput=open('/home/manos/text.txt','r').read()
print 'The text we want to encrypt is: ' , fileInput , '\n'
if(not(len(fileInput)%8)==0):
	print 'Previous length without padding : ' , len(fileInput) , '\n'
	padding = 8-len(fileInput)%8
	print 'Because the string can not be divided exactly with 8 , so padding of : ' , padding, ' was added' , '\n'
	fileInput = fileInput.ljust(len(fileInput)+padding)
	print 'New input length after padding: ' , len(fileInput) , '\n'
#convert the text into bytes
text=[]
for x in range(len(fileInput)):
	text.append(hex(ord(fileInput[x])))
print 'The text in bytes: ' , text , '\n'
print 'Text length : ' , len(text) , '\n'
	

firstPassBytes=[]
secondPassBytes=[]
i=0
for x in range(len(firstPass)/2):
	firstPassBytes.append(''.join(['0x',firstPass[i:i+2]]))
	secondPassBytes.append(''.join(['0x',secondPass[i:i+2]]))
	i+=2
print 'Bytes of the first sha256sum: ' , firstPassBytes , '\n'
print 'Bytes of the second sha256sum: ' , secondPassBytes , '\n'
	
#Initalize keys for every iteration
keys=[]
e=0
for x in range(len(firstPassBytes)/4):
	keys.append(firstPassBytes[e:e+4])
	e+=4
e=0
for x in range(len(secondPassBytes)/4):
	keys.append(secondPassBytes[e:e+4])
	e+=4
print '16 keys for all the rounds are: ' , keys , '\n'


#seperate plain text into blocks
def seperate(text,position):
	block=[]
	for x in range(position-8,position):
		block.append(text[x])
	return block

#XOR logical gate
def xor(list1,list2):
	xorList=[]
	for x in range(len(list1)):
		a=list1[x]
		b=list2[x]
		print 'XORed charachters' ,  a,b , '\n'
		c = int(a,0) #convert to integer
		d = int(b,0)
		e = c^d #XOR the integers
		xorList.append(hex(e)) #convert to hexadecimal again
	return xorList


def depSeperation(block):
	#deepest seperation left,right 
	print 'BLOCK: ' , block , '\n'
	sides = []
	sides.append(block[:4])
	sides.append(block[4:])
	return sides

#Encrypted text in bytes
encryptedText=[]
#Main procedure of the Feistel cihper
#block chain
def cipherBlock(left,right,keys,flag,i):
	i+=1
	if(flag):
		print 'The encrypted sides after 16 rounds of the procedure :\n'
		print 'Left side: ' , left , '\n'
		print 'Right side: ' , right , '\n'
		encryptedText.append(left + right) 
		import itertools
		print 'Encrypted text bytes: ' , list(itertools.chain.from_iterable(encryptedText)) , '\n'
		lastResult = list(itertools.chain.from_iterable(encryptedText))
		lastlastResult=[]
		for x in range(len(lastResult)):
			lastlastResult.append(chr(int(lastResult[x],0)))
		print 'Encrypted text letters: ' , ''.join(lastlastResult) , '\n'
		print'Encrypted text length: ' , len(lastlastResult) , '\n'
	else:
		left=right	
		right=xor(right,keys[i-1])
		print 'Next round right' , right , '\n'
		print 'Next round left' , left , '\n'
		print 'Mext round key' , keys[i-1] , '\n'
		if(i==16):
			flag = True
		cipherBlock(left,right,keys,flag,i)
	
#main procedure of each block
def encryptBlock(text,keys,position):
	block = seperate(text,position)
	sides = depSeperation(block)
	print 'SIDES : ' , sides 
	print 'LEFT : ' , sides[0]#left side of the block
	print 'RIGHT : ' , sides[1]#right side of the block
	flag=False
	i=0
	encryptedSides = cipherBlock(sides[0],sides[1],keys,flag,i)

def mainProcedure():
	position=8
	#division in order to split the text(text in bytes) into blocks of 8
	for x in range(len(text)/8):
		encryptBlock(text,keys,position)
		position+=8#go to another block

mainProcedure()
	

		
	


                                                    DECRYPTION
		
		
import hashlib
import struct


def get_passw():
    password = raw_input('Give me a password: ')
    firstPass = hashlib.sha256(password.encode()).hexdigest()
    secondPass = hashlib.sha256(firstPass.encode()).hexdigest()
    print "LEN HASH_PSW",len(firstPass+secondPass)
    return firstPass+secondPass


def XOR(op1, op2):
    # compute op1 ^ op2 must to be strings of format hexa
    a=int(op1,16)
    b=int(op2,16)
    return hex(a^b)[2:]

def do_round(left, right,key):
    tmp=right
    right=XOR(left,f(key,right))
    left=tmp
    return left,right


def encipher_block(plaintext_block,ks):
    #encryption algo
    plaintext_block=str2hex(plaintext_block)
    print "str2hex of plaintext_block", plaintext_block
    left=plaintext_block[:len(plaintext_block)/2]
    right=plaintext_block[len(plaintext_block)/2:]
    for i in range(len(ks)):
        left ,right=do_round(left,right,ks[i])
    return right+left

def do_round_decr(left,right,key):
    tmp=left
    left=XOR(right,f(key,left))
    right=tmp
    return left,right


def decipher_block(cipher_block,ks):
    cipher_block=str2hex(cipher_block)
    left=cipher_block[:len(cipher_block)/2] #this is actually Rn+1
    right=cipher_block[len(cipher_block)/2:] #this is actually Ln+1
    for k in reversed(ks):
        left,right= do_round_decr(left,right,k)
    return left+right

def blockify(plaintext,blocksize):
    #split text in block of blocksize byte
    lenght=len(plaintext)
    padding=0
    if lenght % blocksize != 0 :
        padding=blocksize - (lenght % blocksize)
    print "PLAIN LEN: ",len(plaintext)
    plaintext+=padding*" "
    print "PLAIN+PADDING LEN: ",len(plaintext)
    plaintext=map(''.join, zip(*[iter(plaintext)]*blocksize))
    return plaintext

def str2hex(string):
    hexa=""
    for i in string:
        hexa+=hex(ord(i))[2:]
    return hexa #return just the hexa string without 0x

def hex2str(hex_string):
    if len(hex_string)%2 == 0:
        pass
    else :
        hex_string="0"+hex_string
    return hex_string.decode("hex")

def f(key,oper):
    return key

def build_keys_stream(password):
    KS=map(''.join, zip(*[iter(password)]*8))
    for i in range(len(KS)):
        KS[i]="0x"+KS[i]
    return KS

def main_routine(plaintext):
    passw=get_passw()
    KS=build_keys_stream(passw)
    plaintext_blocked=blockify(plaintext,8)
    cipher=""
    for block in plaintext_blocked:
        cipher+=encipher_block(block,KS)
    cipher=hex2str(cipher)
    print"CIPHER", cipher

    ciphertext_blocked=blockify(cipher,8)
    res=""
    for cblock in reversed(ciphertext_blocked):
        res=hex2str(decipher_block(cblock,KS))+res
    print"\ndecription:", res, " len: ", len(res)


#main
#main_routine('Hello my name is Manos')

passw=get_passw()
KS=build_keys_stream(passw)
res=""
fi=open("/home/manos/fei.Feistel","rb").read()
for cblock in reversed(blockify(fi,8)):
    res=hex2str(decipher_block(cblock,KS))+res
print "RES: ",res
#

	
	
	
	




