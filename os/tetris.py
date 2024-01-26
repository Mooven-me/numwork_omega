from time import *
from ion import *
from random import *
from kandinsky import *

def Tetros():
  Xdom, Ydom = range(12), range(22)
  info = ['Move     ARROWS', 'Descend  DOWN', 'Rotate   OK', 'Replay   EXE', 'Quit     BACK']
  TYPES = (
      ([[1, 0], [1, 1], [0, 1]],), # O
      ([[-1, 0], [1, 0], [2, 0]], [[0, -1], [0, 1], [0, 2]]), # I
      ([[-1, 0], [1, 0], [1, -1]], [[0, -1], [0, 1], [1, 1]], [[1, 0], [-1, 0], [-1, 1]], [[-1, -1], [0, -1], [0, 1]]), # L
      ([[-1, -1], [-1, 0], [1, 0]], [[1, -1], [0, -1], [0, 1]], [[-1, 0], [1, 0], [1, 1]], [[0, -1], [0, 1], [-1, 1]]), # J
      ([[1, 0], [-1, 0], [0, 1]], [[1, 0], [0, -1], [0, 1]], [[1, 0], [-1, 0], [0, -1]], [[0, -1], [-1, 0], [0, 1]]), # T
      ([[-1, 0], [0, 1], [1, 1]], [[1, -1], [1, 0], [0, 1]]), # S
      ([[1, 0], [0, 1], [-1, 1]], [[0, -1], [1, 0], [1, 1]])) # Z
  COLORS = ((255,)*3, True, (253, 225, 0), (43, 172, 226), (248, 150, 34), (0, 90, 157), (146, 43, 140), (238, 39, 51), (78, 183, 72))

  def sett(X, Y, value):
      M[Y] = M[Y][:X] + value + M[Y][X+1:]
      if value == '1': fill_rect(2+10*X, 1+10*(21-Y), 8, 8, COLORS[int(tetro[2])+2])
      else: fill_rect(2+10*X, 1+10*(21-Y), 8, 8, COLORS[int(value)])

  def unpack(op = False):
      X, Y, TYPE, ORIENTATION = tetro
      if op == 'down': Y -= 1
      elif op == 'left': X -= 1
      elif op == 'right': X += 1
      elif op == 'rotate': ORIENTATION = (ORIENTATION + 1)%len(TYPES[TYPE])
      cases = [[X, Y]]
      for case in TYPES[TYPE][ORIENTATION]: cases.append([X + case[0], Y + case[1]])
      return cases, [X, Y, TYPE, ORIENTATION]     

  def form(op = False):
      if op:
          old, _ = unpack()
          new, newtetro = unpack(op)
      else: new, _ = unpack()
      for case in new:
          if not(case[0] in Xdom) or case[1] < 0 or int(M[case[1]][case[0]]) > 1: return False
      if op:
          for case in old: sett(case[0], case[1], '0')
      for case in new: sett(case[0], case[1], '1')
      return newtetro

  while True:
      fill_rect(0, 0, 320, 222, (0,)*3) # Box
      fill_rect(1, 0, 122, 221, COLORS[0]) # Background - Game
      fill_rect(124, 0, 196, 222, COLORS[0]) # Background - Informations
      draw_string('TETRIS', 192, 20)
      draw_string('Lines    0', 147, 55)
      for string in info: draw_string(string, 147, 90 + 20*info.index(string))
      lines, M = 0, ['0'*len(Xdom),]*len(Ydom)
      while True:
          last = tetro = [6, 19, randint(0, 6), 0]
          if not(form(tetro)): break
          while True: 
              stamp = monotonic() + 0.2 + 0.5/(lines+2)
              while True:
                  if monotonic() > stamp or keydown(2): break
                  elif keydown(4): tetro = form('rotate')
                  elif keydown(0): tetro = form('left')
                  elif keydown(3): tetro = form('right')
                  if tetro != last:
                      sleep(0.1)
                      if tetro: last = tetro
                      else: tetro = last
              sleep(0.03)
              newtetro = form('down')
              if newtetro: last = tetro = newtetro
              else:
                  for Y in Ydom:
                      for X in Xdom:
                          if M[Y][X] == '1': sett(X, Y, str(int(tetro[2])+2))
                  completed = False
                  for line in M[:]:
                      if not('0' in line):
                          M.remove(line)
                          M.append('0'*len(Xdom))
                          lines += 1
                          completed = True
                  if completed:
                      sleep(0.2)
                      draw_string(str(lines), 237, 55)
                      for Y in Ydom:
                          for X in Xdom: sett(X, Y, M[Y][X])
                  break
      while not(keydown(52)): pass
Tetros()
