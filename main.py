import random
import time
from tkinter import *
from pixie import Pixie
from food import Food
from utils import *

seed = int(time.time())
random.seed(seed)
print("Seed for world =", seed)

## global vars
canvasWidth = 1270
canvasHeight = 790


## Tkinter Stuff
root = Tk()
c = Canvas(root, width=canvasWidth, height=canvasHeight)
pixies = []
foods = []
## call class
c.create_rectangle(0, 0, canvasWidth, canvasHeight, fill="#19722f")
for i in range(10):
    x = random.random() * canvasWidth
    y = random.random() * canvasHeight
    pixies.append(Pixie(c, x, y))
c.pack()

# the simulation
while True:
    if len(foods) < 1000:
        foods.append(Food(c))

    for pixie in pixies:
        pixie.goTo(c, foods)
    c.update()

root.mainloop()
