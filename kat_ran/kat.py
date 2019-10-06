#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:12:15 2019

@author: abhijithneilabraham
"""
import random
import time
c=int(input('write in number how much you love a cat \n'))    
def catran():
    a=random.randint(97,122)
    print(chr(a),end="")
r=0.05
for i in range(c):
    
    if i%5==0:
        r=random.uniform(0.01,0.2)
    time.sleep(r)
    catran()
print("\n Oops,cat ran"+str(c)+"times through ya keyboard!")
    

    
