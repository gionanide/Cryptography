#!usr/bin/python

def ex11():
	#compute number = (43210^23456)%99987
	#computation take place by squaring and multiplying
	base = 43210
	power = 23456
	modulo = 99987
	#make power binary with 20bits
	binaryPower = "{0:b}".format(power)
	#I skip the first bit because is number^x(and x=1) so number^x=number
	baseBase = base
	for x in binaryPower[1:]:
		base = anadromic(base,int(x),modulo,baseBase)
	print 'Result from hidden slides procedure: ',base
	print 'Result using normal operators: ',(43210**23456)%99987

def anadromic(number,x,modulo,baseBase):
	#baseBase because i want every time that the bit is 1 to multiple with the initial base
	#the following procedure is from the hidden slides, (squaring and multiplying)
	if(x==0):
		result = (number**2)%modulo
		return result
	elif(x==1):
		result = ((number**2)%modulo*baseBase)%modulo
		return result

	
ex11()
