
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
#    playsound("cataudios/" + random.choice(kat_sounds))
    a = random.randint(97, 136)
    print(chr(a), end="")

r = 0.05
for i in range(c):
    if i % 5 == 0:
        r = random.uniform(0.01,0.2)
    time.sleep(r)
    catran()

print("\n Oops, cat ran", str(c), "times through ya keyboard!")


from tkinter import *

root = Tk()
imagelist = ["kat.jpeg"]
# extract width and height info
photo = PhotoImage(file=imagelist[0])
width = photo.width()
height = photo.height()
canvas = Canvas(width=width, height=height)
canvas.pack()
# create a list of image objects
giflist = []
for imagefile in imagelist:
    photo = PhotoImage(file=imagefile)
    giflist.append(photo)
# loop through the gif image objects for a while
canvas.create_image(width/2.0, height/2.0, image=giflist[0])
canvas.update()
time.sleep(0.1)
root.mainloop()
