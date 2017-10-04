#!usr/bin/python

from Tkinter import *
from tkFileDialog import *
import tkMessageBox
import os
from PIL import Image 
from PIL import ImageFilter
from PIL import ImageChops
import math
import hashlib
import binascii
import io


#XOR logical gate
def xor(a,b):
	#print 'XORed charachters' ,  a,b , '\n'
	#c = int(a,0) #convert to integer
	d = int(b,16)
	e = a^d #XOR the integers
	#result = hex(e) #convert to hexadecimal again
	#print 'Result: ',e
	return e

def keySchedule():
	passA= raw_input('Give me a password: ')
	print ''
	password = passA + '.jpg'
	firstPass = hashlib.sha256(password.encode()).hexdigest()
	print 'First sha256 pass: ' , firstPass , '\n'
	secondPass = hashlib.sha256(firstPass.encode()).hexdigest()
	print 'Second sha256 pass: ' , secondPass , '\n'

	firstPassBytes=[]
	secondPassBytes=[]
	i=0
	for x in range(len(firstPass)/2):
		firstPassBytes.append(''.join(['0x',firstPass[i:i+2]]))
		secondPassBytes.append(''.join(['0x',secondPass[i:i+2]]))
		i+=2

	key = firstPassBytes+secondPassBytes
	return key

def encrypt(name):
	privateKey = [ ]
	key = keySchedule()
	#open the image
	image = Image.open(name,mode='r')
	width,height = image.size
	print 'Width: ',width,' Height: ',height
	i=0
	e=0
	for y in range(height):
		for x in range(width):
			cc = image.getpixel((x,y))
			privateKey.append(cc)
			#PUTPIXEL( (X,Y) , color(R,G,B) )
			image.putpixel((x,y),(0,0,0))
	image.show()	
	image.save('encrypted.jpg')
	e=0
	with open('key.txt','w') as private:
		for x in range(len(privateKey)):
			for y in range(3):
				private.write(str(xor(privateKey[x][y],key[e])))
				if(e==len(key)-1):
					e=0
				else:
					e+=1
				private.write('\n')




def decrypt(name,private):
	key = keySchedule()
	#open the image
	privateK = []
	image = Image.open(name,mode='r')
	e=0
	with open(private) as pk:	
		for f in pk.readlines():
			privateK.append(xor(int(f),key[e]))
			if(e==len(key)-1):
				e=0
			else:
				e+=1
	width,height = image.size
	print 'Width: ',width,' Height: ',height
	#encryptedList = []*(width*height)#global list for encryption/decryption
	k=0
	for y in range(height):
		for x in range(width):
			cc = image.getpixel((x,y))
			#PUTPIXEL( (X,Y) , color(R,G,B) )
			image.putpixel((x,y),(int(privateK[k]),int(privateK[k+1]),int(privateK[k+2])))
			k+=3
	image.show()	
	image.save('decrypted.jpg')


def main():
	name = raw_input('Give the name of image : ')
	choice = raw_input('e for encryption , d for decryption: ')
	if(choice=='d'):
		namep = raw_input('Give the private key: ')
		decrypt(name+'.jpg',namep+'.txt')
	elif(choice=='e'):
		encrypt(name+'.jpg')
	else:
		print 'Input Error'
	

main()
