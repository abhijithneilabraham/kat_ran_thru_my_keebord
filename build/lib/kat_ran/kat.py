
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:12:15 2019

@author: abhijithneilabraham
"""
import random
import time
from playsound import playsound
def katran():
    
    kat_sounds = ["cat1.mp3", "cat2.mp3", "cat3.mp3", "cat4.mp3", "cat5.mp3", "cat6.mp3"]
    
    print('cat is running through ya keyboard.Press ctrl+c two times to exit')
      
    
    
    
    r = 0.05
    i=1
    while i%2!=0:
        try:
            if i % 5 == 0:
                r = random.uniform(0.01,0.2)
                playsound("cataudios/" + random.choice(kat_sounds))
            a = random.randint(97, 136)
            print(chr(a), end="")        
            time.sleep(r)
    
            i+=2        
        except KeyboardInterrupt:
            print("\n Oops, cat ran through ya keyboard!")
            break

consent=input("Do you wanna let your cat run on your keyboard?")
if consent=="yes":
    katran()
    
elif consent=="no":
    exit()
else:
    print("Well then, let's begin")
    katran()
