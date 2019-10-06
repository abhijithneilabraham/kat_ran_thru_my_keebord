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
     if a>=97 and a<=103:
        playsound('path\of\the\directory\cat1.mp3') #cat1.mp3, cat2.mp3, cat3.mp3 and cat4.mp3 is provided in the repo
    if a>103 and a<=110:
        playsound('path\of\the\directory\cat2.mp3')
    if a>110 and a<=117:
        playsound('path\of\the\directory\cat3.mp3')
    if a>117 and a<122:
        playsound('path\of\the\directory\cat4.mp3')
    print(chr(a),end="")
r=0.05
for i in range(c):
    
    if i%5==0:
        r=random.uniform(0.01,0.2)
    time.sleep(r)
    catran()
print("\n Oops,cat ran",str(c),"times through ya keyboard!")
    

    
