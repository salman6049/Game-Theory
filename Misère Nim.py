# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 08:35:22 2020

@author: Salman
"""

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the misereNim function below.
def misereNim(a):
    s , c = a[0] , 1
    for i in range(1,len(a)): s ^= a[i]
    for i in a:  
        if i > 1: c = 0
    if s == c: return "Second"
    else: return "First"

for _ in range(input()):
    n = input()
    my_list = map(int, raw_input().split())
    print misereNim(my_list)