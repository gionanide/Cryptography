#!usr/bin/python
from PIL import Image
import hashlib

def secretMessage():
	bitsList=[]
	secret = raw_input('Give the message you want to hide: ')
	for x in secret:
		#format 8 bits per charachter
		bitsList.append("{0:08b}".format(ord(x)))
	print ''.join(bitsList)
	return ''.join(bitsList)
	
	
def keySchedule(height,width):
	key = raw_input('Give the key: ')
	firstPass = hashlib.sha256(key.encode()).hexdigest()
	secondPass = hashlib.sha256(firstPass.encode()).hexdigest()
	thirdPass = hashlib.sha256(secondPass.encode()).hexdigest()
	secretKey = firstPass+secondPass+thirdPass
	signal = createSignal(secretKey,height,width)
	print 'Private key: ',secretKey,', Signal: ',signal
	return signal
	

#initiate the stego
def createSignal(key,height,width):
	result=0
	for x in range(len(key)-4):
		result+=xor(key[x:x+2],key[x+2:x+4])
	return result%(height-len(key))




#XOR logical gate
def xor(a,b):
	#print 'XORed charachters' ,  a,b , '\n'
	c = int(a,16) #convert to integer
	d = int(b,16)
	e = c^d #XOR the integers
	#result = hex(e) #convert to hexadecimal again
	#print 'Result: ',e
	return e

def transformImage():
	image = Image.open('walknut.jpg')
	#image.show()
	#if the image is too big you can resize it using ANTIALIAS
	#image = image.resize((100,100), Image.ANTIALIAS)
	#visualize the result
	#image.show()
	width, height = image.size
	rgb_im = image.convert('RGB')
	return width,height,image

def replaceBit(r,n):
	r = "{0:08b}".format(r)
	r = r[::-1].replace(r[len(r)-1],n,1)
	return r[::-1]


#hide the message procedures
def LSB(height,width,image,messageList,signal):
	y=signal
	k=0
	for x in range(signal,signal+len(messageList)-1,3):
			r,g,b = image.getpixel((y,y))
			#binary representation
			#print r,messageList[k]
			r = replaceBit(r,messageList[k])
			#print r
			#print g,messageList[k+1]
			g = replaceBit(g,messageList[k+1])
			#print g
			#print b,messageList[k+2]
			b = replaceBit(b,messageList[k+2])
			#print b
			#print image.getpixel((x,y))
			image.putpixel((y,y),(int(r,2),int(g,2),int(b,2)))
			#print image.getpixel((x,y))
			k+=3
			y+=1
	r,g,b = image.getpixel((y+1,y))
	#print r,messageList[k]
	r = replaceBit(r,messageList[k])
	image.putpixel((y,y),(int(r,2),g,b))
	#print r
	#print messageList
	print 'Stego image in stego.jpg'
	image.save('encrypted.jpg')
	return signal
	#hidding the message in the less significant bit (last bit)
		

def mainProcedure():
	width,height,image = transformImage()	
	messageBitList = secretMessage()
	signal = keySchedule(height,width)
	signal = LSB(height,width,image,messageBitList,signal)
	print 'Signal: ',signal


mainProcedure()
