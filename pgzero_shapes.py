import pgzrun
from random import randint 


WIDTH = 300
HEIGHT = 300

#Screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw():
  width = WIDTH 
  height = WIDTH - 200

  r = 255
  g = 0
  b = randint(120, 255)

  for i in range(15):
    rect = Rect((0, 0), (width, height))
    rect.center = 150, 150
    screen.draw.rect(rect, (r, g, b))

    r -= 10
    g += 10
    height += 10
    width -= 10

pgzrun.go()
# Screen.mainloop()


# pip install pgzero