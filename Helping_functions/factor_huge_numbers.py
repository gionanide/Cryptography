#!usr/bin/python
import random
from fractions import gcd

def factorNumber():
	#find the prime factors of a big number
	#for example N = p * q RSA
	#Using Euler's logic, modular arithmetic
	#we have to find the period of the repeating patternt
	number = int(raw_input('The number for factorization: '))
	a = randomRelativePrime(number)
	period = computeThePeriod(number,a)
	while(not((period%2==0) and (not((a**(period/2)+1)==(0%number))))):
		print 'This relative prime number does not satisfy the conditions \n'
		a = randomRelativePrime(number)
		period = computeThePeriod(number,a)
	# (a**period)%number == 1 in order to check if everything is right, so it is means that ((a**period)-1)%number == 0, and from this we can conclude that a**period - 1 is a multiple of N(number). So a k exists that (a**period - 1 == k*N). Now because period is an even number we can write is as follow : (a**period/2 - 1)(a**period/2 + 1) = k*N and since N = p * q we can replace it. (a**period/2 - 1)(a**period/2 + 1) = k*p*q

	#Assumptions
	p = gcd(a**(period/2) - 1,number)
	q = gcd(a**(period/2) + 1,number)
	#I assume this because of the last equation a**period/2 - 1)(a**period/2 + 1) = k*p*q which means that p 
	#must divide one the factors on on the left and q must divide one of the factors on the left. But they cannot 
	#divide tha same factor since the factor would be divisible by N. Why is neither factor divisible by N? ---- we 
	#assume that (a**period/2+1)!=0modN and for the other we know that period is the minimum value of x such that 
	#a**x == 1modN. So since p and q divide seperate factos ont he left side of the equation we can assume that p 
	#divides (a**period/2 -1) and q divides (a**period/2 +1).
	print 'Factors are: ',p,q
		
	

def computeThePeriod(number,a):
	for x in range(2,20):
		if(a==(a**x)%number):
			print 'period: ',x-1
			return x-1
			break
		

def randomRelativePrime(number):
	a = int(random.randrange(1,number-1))
	while(not(gcd(number,a)==1)):
		a = int(random.randrange(1,number-1))
	print 'relative prime: ',a
	return a


factorNumber()
	
