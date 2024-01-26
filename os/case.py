from random import *
from time import *
from kandinsky import *
from ion import *
from os import *

grille = [0,0,0,0,
          0,0,4,0,
          0,0,0,0,
          0,0,0,0]

def jeu_GRILLE(n,position,nombre,oui):
  if oui:
    grille[position]=nombre
  return grille[n]

def aff(n,x,y):
  chiffres = [31599,18724,29671,31207,18925,31183,31695,18727,31727,31215]
  if n>0:
    for k,c in enumerate(str(n)):
      for i in range(16):
        if chiffres[int(c)]>>i & 1 == 1:
          fill_rect(x+12*k+(i%3)*3,y+(i//3)*3,3,3,(110,110,90))

def jeu_DESSIN():
  fill_rect(60,10,200,200,[88,52,11])
  yg=12
  nombre=0
  for n in range(4):
    xg=62
    for i in range(4):
      fill_rect(xg,yg,42,42,[255,255-grille[nombre],255-grille[nombre]])
      aff(grille[nombre],xg+8,yg+12)
      xg+=50
      nombre+=1
    yg+=50
  sleep(0.5)


def deplacement():
  refresh=False
  dirct=0
  while True:

    if keydown(KEY_UP):
      refresh=True
      dirct = 1

    if keydown(KEY_DOWN):
      refresh=True
      dirct = -1

    if keydown(KEY_LEFT):
      refresh=True
      dirct = -2

    if keydown(KEY_RIGHT):
      refresh=True
      dirct = 2
    if refresh:
      refresh=False
      if dirct == -1:
        for i in range(16):
          a=15-i
          if grille[a]!=0 and a<=11:
            for k in range(3):
              if a+((k+1)*4)<=15:
                if grille[a+(k*4)] == grille[a+((k+1)*4)]:
                  grille[a+((k+1)*4)] = grille[a+(k*4)]*2
                  grille[a+(k*4)]=0

                elif grille[a+((k+1)*4)]==0:
                  grille[a+((k+1)*4)] = grille[a+(k*4)]
                  grille[a+(k*4)]=0

      if dirct == 1:
        for i in range(16):
          if grille[i]!=0 and i>=4:
            for k in range(3):
              if i-((k+1)*4)>=0:
                if grille[i-(k*4)] == grille[i-((k+1)*4)]:
                  grille[i-((k+1)*4)] = grille[i-(k*4)]*2
                  grille[i-(k*4)]=0

                elif grille[i-((k+1)*4)]==0:
                  grille[i-((k+1)*4)] = grille[i-(k*4)]
                  grille[i-(k*4)]=0

      if dirct == 2: ####DROITE####
        for i in range(16):
          b = int((((i%4)+1)*4)-1-((i%4-i)/4*-1))
          if grille[b]!=0 and b!=3 and b!=15 and b!=7 and b!=11:
            for k in range(3):
              if (b+k)!=3 and (b+k)!=15 and (b+k)!=7 and (b+k)!=11 and (b+k)<15:
                if grille[b+k+1]==grille[b+k]:
                  grille[b+k+1] = grille[b+k]*2
                  grille[b+k]=0
                elif grille[b+k+1]==0:
                  grille[b+k+1]=grille[b+k]
                  grille[b+k]=0
      if dirct == -2:
        for i in range(16):
          a = int(((i%4)*4)+((i%4-i)/4*-1))
          if grille[a]!=0 and a!=0 and a!=4 and a!=8 and a!=12:
            for i in range(3):
              if a-i!=0 and a-i!=4 and a-i!=8 and a-i!=12:
                if grille[a-i-1]==grille[a-i]:
                  grille[a-i-1]=grille[a-i]*2
                  grille[a-i]=0
                elif grille[a-i-1]==0:
                  grille[a-i-1]=grille[a-i]
                  grille[a-i]=0
      grilleale = []
      numberr = [4,4,4,4,4,4,4,4,4,4,4,4,8,8,8,8,8,8,16]
      for i in range(16):
        if grille[i]==0:
          grilleale.append(i)
      grille[choice(grilleale)]=choice(numberr)
      jeu_DESSIN()     


def jeu_START():
  jeu_DESSIN()
  deplacement()

jeu_START()
