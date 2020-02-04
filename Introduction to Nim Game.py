# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 08:31:50 2020

@author: Salman
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nimGame function below.
def nimGame(a):
    s = a[0]
    for i in range(1,len(a)):
        s ^= a[i]
    if s == 0: return "Second"
    else: 
        return "First"

for _ in range(input()):
    n = input()
    my_list = map(int, raw_input().split())
    print (nimGame(my_list))