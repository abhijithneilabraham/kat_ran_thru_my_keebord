#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:12:15 2019

@author: abhijithneilabraham
"""
import random
import time
from playsound import playsound

kat_sounds = ["cat1.mp3", "cat2.mp3", "cat3.mp3", "cat4.mp3", "cat5.mp3", "cat6.mp3"]
c = int(input('Write in number how much you love a cat \n'))    
def catran():
    playsound("catsounds/" + random.choice(kat_sounds))
    a = random.randint(97, 136)
    print(chr(a), end="")

r = 0.05
for i in range(c):
    if i % 5 == 0:
        r = random.uniform(0.01,0.2)
    time.sleep(r)
    catran()

print("\n Oops, cat ran", str(c), "times through ya keyboard!")
