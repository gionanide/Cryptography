#!usr/bin/python 

import sys
import fractions
import math

#CRT prcedure
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
 
    for n_i, a_i in zip(n, a):
	p = prod / n_i
	sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 

#checking for common factors
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1

    while a > 1:
	try:
		q = a / b
		a, b = b, a%b
		x0, x1 = x1 - q * x0, x0
	except:
		print "Bad N values (check no common factors in N vals)"
		return 0
    if x1 < 0: x1 += b0
    return x1


def GCD(a,b):
	#The Euclidean Algorithm 
	a = abs(a)
	b = abs(b)
	while a:
	        a, b = b%a, a
	return b
	
	
def GCD_List(list):
	#Finds the GCD of numbers in a list.
	#Input: List of numbers you want to find the GCD of
		#E.g. [8, 24, 12]
	#Returns: GCD of all numbers
	return reduce(GCD, list)




def ex13():
	nval=[]
	aval=[]

	#N1 = 493
	#N2 = 517
	#N3 = 943
	#e=3
	#C1 = (message)**e % (N1)
	#C2 = (message)**e % (N2)
	#C3 = (message)**e % (N3)

	print ('attack RSA with CRT')
	N1 = raw_input('Give the public key factor: ')
	C1 = raw_input('Give the encrypted message with the previous factor: ')
	N2 = raw_input('Give the public key factor: ')
	C2 = raw_input('Give the encrypted message with the previous factor: ')
	N3 = raw_input('Give the public key factor: ')
	C3 = raw_input('Give the encrypted message with the previous factor: ')
	e = raw_input('Give the exponent: ')

	#initialize chinese remainder theorem input
	nval.append(int(N1))
	nval.append(int(N2))
	nval.append(int(N3))
	aval.append(int(C1))
	aval.append(int(C2))
	aval.append(int(C3))

	n = nval
	a = aval
	g = GCD_List(n)
	
	print "N1: ",N1,'\n'
	print "N2: ",N2,'\n'
	print "N3: ",N3,'\n'
	print "Cipher1: ",C1,'\n'
	print "Cipher2: ",C2,'\n'
	print "Cipher3: ",C3,'\n'
	print "e: ",e,'\n'


	if (g>1):
		print 'Computing error'
	else:
		result = chinese_remainder(n, a)
		count=0
	

	for str1 in nval:
		print "x mod "+str(str1)+"="+str(aval[count])
		count=count+1

	print "Result (x) is: ",result,"\n"
	m = 10**(math.log10(result)/int(e))
	print 'Calculated value of m is ',int(round(m))


ex13()
