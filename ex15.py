from random import randint

def compute_b(a,x,y,N):
    return (y**2-x**3-a*x)%N

def single_sum((x,y),a,b,N):
    if y==0 :
        return x,y
    m=(3*(x**2)+a)*modinv(2*y,N)
    x3=(m**2-2*x)%N
    y3=(m*(x-x3)-y)%N
    return x3,y3

def add((x1,y1),(x2,y2),a,b,N):
    if x1-x2 == 0 and y1-y2 == 0:
        return single_sum((x1,y1),a,b,N)
    m=(y2-y1)*modinv((x2-x1),N)
    x3=(m**2-x1-x2)%N
    y3=(m*(x1-x3)-y1)%N
    return x3, y3

def multiply((x,y),n,a,b,N):
    i=0
    xr,yr=x,y
    while i < n-1:
        xr,yr = add((x,y),(xr,yr),a,b,N)
        i+=1
    return xr,yr

def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def coefficient_conditions(a,b):
    return 4*a**3  + 27*b**2 != 0




#main
a , b , N , x1 , y1 , Xm , Ym = 27 , 152 , 229 , 32 , 11 , 79 , 40
m = 58

p17=(97339010987059066523156133908935, 149670372846169285760682371978898)
a17=321094768129147601892514872825668
b17=430782315140218274262276694323197
N17=564538252084441556247016902735257
n17=486035459702866949106113048381182

#print multiply(p17,n17,a17,b17,N17)
