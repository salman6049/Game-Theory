# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:29:02 2020

@author: Salman
"""

from bisect import bisect_left

def part(high):
    a=[0]*(1+high)
    a[0]=1
    for n in range(1,1+high):
        k=1
        while k*k<=n:
            a[n]+=a[n-k*k]
            k+=1
    return a

a=part(121)
for _ in range(int(input())):
    print(bisect_left(a,int(input())))