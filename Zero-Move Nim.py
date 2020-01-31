# -*- coding: utf-8 -*-
"""
Created on January 2018

@author: Salman
"""

import sys
from functools import reduce

g = int(input().strip())
for a0 in range(g):
    n = int(input().strip()) # num of heaps
    p = [int(p_temp) for p_temp in input().strip().split(' ')] # pile counts
    p = [(pt+1 if pt%2 == 1 else pt-1) for pt in p]
    #print(p)
    nimsum = reduce((lambda x,y: x^y), p)
    won = False if nimsum == 0 else True
    print('W') if won else print('L')