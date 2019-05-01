from tkinter import *
from world import World

## global vars
canvasWidth = 530
canvasHeight = 530


## Tkinter Stuff
root = Tk()
c = Canvas(root, width=canvasWidth, height=canvasHeight)


## call class
worldMap = World(c, canvasWidth, canvasHeight)


c.pack()

# the simulation
while True:
    worldMap.show(c)
    c.update()

root.mainloop()
