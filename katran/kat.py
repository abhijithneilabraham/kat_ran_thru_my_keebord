
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:12:15 2019

@author: abhijithneilabraham
"""
import random
import time
from playsound import playsound
import os
def katran(path_to_audio):
    
    kat_sounds =os.listdir(path_to_audio)
    
    print('cat is running through ya keyboard.Press ctrl+c two times to exit')
      
    
    
    
    r = 0.05
    i=1
    while i%2!=0:
        try:
            if i % 5 == 0:
                r = random.uniform(0.01,0.2)
                playsound(path_to_audio + random.choice(kat_sounds))
            a = random.randint(97, 136)
            print(chr(a), end="")        
            time.sleep(r)
    
            i+=2        
        except KeyboardInterrupt:
            print("\n Oops, cat ran through ya keyboard!")
            break
        


def main(path):
    consent=input("Do you wanna let your cat run on your keyboard? say yes or no \n")
    if consent=="yes":
        print("Well then, let's begin")
        katran(path)
    else:
        exit()

