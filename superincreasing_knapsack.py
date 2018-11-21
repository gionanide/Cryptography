from random import randint
from collections import deque

char_per_block=2
N=8*char_per_block

def build_superincreasing_knapsack():
    SIK=[0]*N
    for it_i in range(0,N):
        sum_ij=0
        for it_j in range(0,it_i):
            sum_ij+=SIK[it_j]
        SIK[it_i]=sum_ij+randint(1,5)
    superi=0
    for i in range(len(SIK)-1): #check if it is a SUPERINCREASING KNAPSACK
        superi+=SIK[i]
        if superi > SIK[i+1] :
            print "NON SIK"
    return SIK

#here there is my private key
SIK=[1, 4, 6, 12, 25, 50, 103, 205, 409, 820, 1639, 3276, 6554, 13106, 26212, 52425]#build_superincreasing_knapsack()
m,n=89, 104848
mmi=87177
#here is my public key
GK=[89, 356, 534, 1068, 2225, 4450, 9167, 18245, 36401, 72980, 41023, 81868, 59066, 13106, 26212, 52513]
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1

def choose_m_n():
    sum_i=0
    for i in SIK:
        sum_i+=i
    m=randint(41,100)
    n=0
    while n < sum_i:
        if coprime(m,sum_i+1):
            n=sum_i+1
    return m,n

def build_general_knapsack(m,n,SIK):
    GK=[]
    for ai in SIK:
        GK.append((ai*m)%n)
    return GK

def modulo_multiplicative_inverse(A, M):
    # A and M are coprime
    gcd, x, y = extended_euclid_gcd(A, M)
    if x < 0:
        x += M
    return x

def extended_euclid_gcd(a, b):
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a
    while r != 0:
        quotient = old_r/r
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
    return [old_r, old_s, old_t]

def str2ascii(x):
    x=ord(x)
    binary="{0:b}".format(x)
    if len(binary) <= 7:
        binary='0'*(8-len(binary))+binary
    return binary

def encrypt_N_char(chars):
    bin_chars=""
    for i in range(len(chars)):
        bin_chars=str2ascii(chars[i])[::-1]+bin_chars
    return sum([int(x)*y for x,y in zip(list(bin_chars), GK)])


def decrypt_N_char(number):
    res=""
    d=(number*mmi)%n
    for sik_i in SIK[::-1]:
        if d >= sik_i:
             res="1"+res
             d-=sik_i
        else :
            res="0"+res
    res=res[::-1]
    char1 , char2 =  chr(bit2Str(res[:8])), chr(bit2Str(res[8:]))
    return char1+char2


def bit2Str(bitstring):
    out=0
    for bit in list(bitstring):
        out = (out << 1) | int(bit)
    return out


def encrypt_mh(message):
    msg=[]
    encrypted=[]
    if len(message) % char_per_block != 0:
        message+=" "*(char_per_block-len(message)%char_per_block)
    for i in range(0,len(message),char_per_block):
        msg.append(message[i:i+char_per_block])
    for chars in msg:
        encrypted.append(encrypt_N_char(chars))
    return encrypted

def decrypt_mh(crypto_list):
    plaintext=""
    for num in crypto_list:
        plaintext+=decrypt_N_char(num)
    return plaintext

#print "charbit2int , ord c, d",charbit2int(str2ascii("C")+str2ascii("d")),ord("C"),ord("d")

#print "GK", GK
#
#en=encrypt_N_char("ci")
#print "en ",en
#print decrypt_N_char(en)
print decrypt_mh(encrypt_mh("ciao, io mi chiamo francesco "))
#print "ord c ord i",ord("c"), ord("i")

fin=open("encrypted","r").readlines() #lista con riga\n ad ogni elem
text=""
for i in fin:
    text+= decrypt_mh([int(i,16)])
print text




#
