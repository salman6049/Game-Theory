# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 08:23:18 2020

@author: sigar
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the towerBreakers function below.
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the towerBreakers function below.
def towerBreakers(n,m):
    if m == 1 or n % 2 == 0:
        print(2)
    else:
        print(1)
if __name__ == "__main__":
    case = int(input())
    for _ in range(case):
        n,m = map(int,input().split())
        towerBreakers(n,m)