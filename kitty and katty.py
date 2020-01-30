# -*- coding: utf-8 -*-
"""
Created on January 2019

@author: Salman
"""

for n in (int(input()) for _ in range(int(input()))):
    print('Kitty' if n==1 or not (n&1) else 'Katty')