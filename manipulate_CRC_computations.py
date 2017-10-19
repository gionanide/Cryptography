#!/usr/bin/env python3
import itertools
import zlib

def comb_calc_bit(num):
tuples = list(itertools.product([0, 1], repeat=num))
res=[]
for elem in tuples:
elem = str(elem)[1:-1]
elem = "".join(elem.split(", "))
res.append(elem)
return res

def crc(message, div):
pad='0'*(len(div)-1)
message = message + pad
message = list(message)
div = list(div)
for i in range(len(message)-len(pad)):
if message[i] == '1':
    for j in range(len(div)):
        message[i+j] = str((int(message[i+j])^int(div[j])))
return ''.join(message[-len(pad):])

def calculate_all_collision(message,div,prefixList=None):
final_crc=crc(message,div)
comb5=comb_calc_bit(len(div))
curr_msg=""
res=[]
if prefixList==None:
prefixList=comb_calc_bit(len(message)-len(div))
for prefix in prefixList:
for calc_bit in comb5:
    curr_msg=prefix+calc_bit
    if crc(curr_msg,div) == final_crc:
        res.append(curr_msg)
return res

  print calculate_all_collision("11010110","10011",["111"])

