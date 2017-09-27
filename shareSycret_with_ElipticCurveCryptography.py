#!usr/bin/python
from __future__ import division
import operator
def ex14():
	#eliptic curve equation
	alice = initializePuK()
	alicePK = initializePrK()
	#bob = initializePuK()
	#bobPK = initializePrK()
	print 'Send message procedure begins'
	flag=True
	results = calculateSendMessage(int(alice[3]),int(alice[4]),int(alice[3]),int(alice[4]),int(alicePK),int(alice[0]),int(alice[2]),flag)
	#print results

	
	

def initializePuK():
	a = raw_input('Give me the a factor: ')
	b = raw_input('Give me the b factor: ')
	p = raw_input('Give me the p prime: ')
	x,y = raw_input('Give me the initial point with this format xy: ')
	print '\n'
	print 'The curves equation as a PUBLIC KEY: (y** 2 = x** 3 + x*',a,'+',b,') mod ',p
	print 'And the initial point: (',x,',',y,') \n'
	return a,b,p,x,y

def initializePrK():
	m = raw_input('Give the multiplier: ')
	print'The multiplier as a PRIVATE KEY: ',m,'\n'
	return m


def multiplicativeInverse(n):
	x=1
	while(not(n*x % 17 == 1)):
		x+=1
	return x
	
def calculateP(x1,y1,x2,y2,a,p,flag,i):
	if(x1==x2):
		if(y1==y2):
			if(flag):
				divide = multiplicativeInverse(2*y1)
				s=(((3*x1**2 + a)%p)*(divide))%p
				flag=False
		else:#divide with zero
			s=0
	else:
		divide1 = multiplicativeInverse(x1-x2)
		s=((y1-y2)%p*(divide1))%p
	x3 = ((s**2)%p - (x1 + x2)%p)%p
	y3 = (((s*(x1-x3))%p)%p - y1)%p
	print 'Round : ',i,' (',x3,',',y3,')'
	return x2,y2,x3,y3

def calculateSendMessage(x1,y1,x2,y2,m,a,p,flag):
	variables = calculateP(x1,y1,x2,y2,a,p,flag,1)
	if(m-1<=1):
		return variables[2],variables[3]
	else:
		for x in range(1,m):
			variables = calculateP(variables[2],variables[3],variables[0],variables[1],a,p,flag,x+1)
		return variables[2],variables[3]
		
		
	

ex14()
