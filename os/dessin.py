from ion import *
from math import *
from kandinsky import *
from turtle import *
x=0
y=0

while True:
    if keydown(KEY_LEFT) and x>-219:
        x-=1
        goto(x,y)
    if keydown(KEY_RIGHT) and x<219:
        x+=1
        goto(x,y)
    if keydown(KEY_UP) and x>-219:
        y+=1
        goto(x,y)
    if keydown(KEY_DOWN) and x<219:
        y-=1
        goto(x,y)
