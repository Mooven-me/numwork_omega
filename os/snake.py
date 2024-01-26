from time import *
from ion import *
from random import *
from kandinsky import *
def Snake(v = 1):
  score = 0
  home = True
  dx,dy = 0,1
  vert,rouge = (0,252,0),(248,0,0)
  s = [[160,110]]
  food = True
  pt = monotonic()
  while True:
    if keydown(KEY_HOME):
      if home==False:
        home=True
        sleep(0.5)
    if keydown(KEY_HOME):
      if home==True:
        home=False
        sleep(0.5)
    ct = monotonic()
    dt = ct-pt
    if food:
      fx = 10 * randint(0,31)
      fy = 10 * randint(0,21)
      food = False
    fill_rect(fx,fy,10,10,rouge)
    if keydown(KEY_UP): dx,dy = 0,-1
    if keydown(KEY_DOWN) : dx,dy = 0,1
    if keydown(KEY_LEFT): dx,dy = -1,0
    if keydown(KEY_RIGHT): dx,dy = 1,0
    if dt>.2-.02*v and home:
      pt = monotonic()
      x = s[0][0] + 10*dx
      y = s[0][1] + 10*dy
      if x<0 or x>310 or y<0 or y>210 or get_pixel(x,y)==vert:
        fill_rect(3,8,244,22,(251,0,0))
        draw_string("t'a perdu t'es une merde",5,10)
        fill_rect(x,y,10,10,rouge)
        return score
      s.insert(0,[x,y])
      if get_pixel(x,y)!=rouge:
        q = s.pop()
        fill_rect(q[0],q[1],10,10,(248,255,248))
      else:
        score += 1
        draw_string(str(score),5,10)
        food=True
      fill_rect(s[0][0],s[0][1],10,10,vert)
Snake()
