from math import *
from kandinsky import *
from time import *
from ion import *

speed=0.05
quality=1
size=2

def line(x,y,xs,ys,color):
    if xs<0:
        return line(x+xs,y+ys,-xs,-ys,color)
    else:
        if ys<0:
            a=int((1/(xs+1))*(-ys)+1)
        else:
            a=int((1/(xs+1))*ys+1)
        for i in range((xs+1)/quality):
            for k in range(a/quality):
                fill_rect(x+(i*quality),y+int(((i*quality)/(xs+1))*ys)+(k*quality),size,size,color)


def carre(x=50,y=50,t=10):
    global quality
    global size
    global speed
    a=0

    while True:
        if keydown(KEY_ONE):
            m=[[int(t*cos(a)+1.5*t),int((t/3)*sin(a)+0.5*t)],[int(t*cos(a)+1.5*t),int((t/3)*sin(a)+1.5*t)]]
            n=[[int(t*cos(a-(pi/2))+1.5*t),int((t/3)*sin(a-(pi/2))+0.5*t)],[int(t*cos(a-(pi/2))+1.5*t),int((t/3)*sin(a-(pi/2))+1.5*t)]]
            v=[[int(t*cos(a-pi)+1.5*t),int((t/3)*sin(a-pi)+0.5*t)],[int(t*cos(a-pi)+1.5*t),int((t/3)*sin(a-pi)+1.5*t)]]
            u=[[int(t*cos(a-(1.5*pi))+1.5*t),int((t/3)*sin(a-(1.5*pi))+0.5*t)],[int(t*cos(a-(1.5*pi))+1.5*t),int((t/3)*sin(a-(1.5*pi))+1.5*t)]]

            line(m[0][0],m[0][1],m[0][0]-m[1][0],m[0][1]-m[1][1],(0,0,0))
            line(n[0][0],n[0][1],n[0][0]-n[1][0],n[0][1]-n[1][1],(0,0,0))
            line(v[0][0],v[0][1],v[0][0]-v[1][0],v[0][1]-v[1][1],(0,0,0))
            line(u[0][0],u[0][1],u[0][0]-u[1][0],u[0][1]-u[1][1],(0,0,0))

            line(m[0][0],m[0][1],u[0][0]-m[0][0],u[0][1]-m[0][1],(0,0,0))
            line(n[0][0],n[0][1],m[0][0]-n[0][0],m[0][1]-n[0][1],(0,0,0))
            line(v[0][0],v[0][1],n[0][0]-v[0][0],n[0][1]-v[0][1],(0,0,0))
            line(u[0][0],u[0][1],v[0][0]-u[0][0],v[0][1]-u[0][1],(0,0,0))

            line(m[1][0],m[1][1],u[1][0]-m[1][0],u[1][1]-m[1][1],(0,0,0))
            line(n[1][0],n[1][1],m[1][0]-n[1][0],m[1][1]-n[1][1],(0,0,0))
            line(v[1][0],v[1][1],n[1][0]-v[1][0],n[1][1]-v[1][1],(0,0,0))
            line(u[1][0],u[1][1],v[1][0]-u[1][0],v[1][1]-u[1][1],(0,0,0))



            a+=speed
        if keydown(KEY_TWO):
            u=[int(1.4*t),int(0.6*t)]
            m=[[int(t*cos(a)+1.5*t),int((t/3)*sin(a)+1.5*t)],[int(t*cos(a-pi)+1.5*t),int((t/3)*sin(a-pi)+1.5*t)]]
            n=[[int(t*cos(a-(pi/2))+1.5*t),int((t/3)*sin(a-(pi/2))+1.5*t)],[int(t*cos(a-(1.5*pi))+1.5*t),int((t/3)*sin(a-(1.5*pi))+1.5*t)]]
            
            line(m[0][0],m[0][1],n[0][0]-m[0][0],n[0][1]-m[0][1],(0,0,0))
            line(n[0][0],n[0][1],m[1][0]-n[0][0],m[1][1]-n[0][1],(0,0,0))
            line(m[1][0],m[1][1],n[1][0]-m[1][0],n[1][1]-m[1][1],(0,0,0))
            line(n[1][0],n[1][1],m[0][0]-n[1][0],m[0][1]-n[1][1],(0,0,0))
            line(m[0][0],m[0][1],u[0]-m[0][0],u[1]-m[0][1],(0,0,0))
            line(n[0][0],n[0][1],u[0]-n[0][0],u[1]-n[0][1],(0,0,0))
            line(m[1][0],m[1][1],u[0]-m[1][0],u[1]-m[1][1],(0,0,0))
            line(n[1][0],n[1][1],u[0]-n[1][0],u[1]-n[1][1],(0,0,0))
            a+=speed
            sleep(0.04)
        fill_rect(0,0,330,222,(255,255,255))
        if keydown(KEY_LEFTPARENTHESIS):
            speed+=0.01
        if keydown(KEY_RIGHTPARENTHESIS) and speed!=0.05:
            speed-=0.01
        if keydown(KEY_PLUS) and quality!=1:
            quality-=1
        if keydown(KEY_MINUS):
            quality+=1
        if keydown(KEY_MULTIPLICATION):
            size+=1
        if keydown(KEY_DIVISION) and size!=1:
            size-=1

carre(t=100)
