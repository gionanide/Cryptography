#!usr/bin/python 

import sys
import fractions
import math


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
 
    for n_i, a_i in zip(n, a):
	p = prod / n_i
	sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
