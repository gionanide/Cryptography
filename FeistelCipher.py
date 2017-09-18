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
	

		
	


	
	
	
	
	




