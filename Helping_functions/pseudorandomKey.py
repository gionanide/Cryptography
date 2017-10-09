#!usr/bin/python

#entropy with python , using mouse moves


import pyautogui
import hashlib
import random

#sceern size
width, height = pyautogui.size()
print width,height
#move the mouse
def makeKey(position):
	position = set(position)
	readyInput = ''.join(position)
	firstPass = hashlib.sha256(readyInput.encode()).hexdigest()
	secondPass = hashlib.sha256(firstPass.encode()).hexdigest()
	print secondPass


def randomKey():
	#mouse move by its own generating random numbers
	position1=[]
	inputA = int(raw_input('Give a number the bigger the number the bigger the entropy and so as the security: '))
	for i in range(inputA):
		x = random.randint(1,inputA**2)
		y = random.randint(1,inputA**2)
		#mouse moves based on random numbers
		pyautogui.moveRel(x, y, duration=0)
		x,y = pyautogui.position()
		position1.append(str(x))
		position1.append(str(y))
	makeKey(position1)

def makeYourKey():
	#move the mouse by your own
	#make antropy and generate random key
	position=[]
	print 'Move your mouse...'
	try:
		while(True):
			#take all the mouse's moves
			x,y = pyautogui.position()
			position.append(str(x))
			position.append(str(y))
	except KeyboardInterrupt:
		print('\nDone')
	#make the list unique
	makeKey(position)


