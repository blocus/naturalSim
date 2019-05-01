import random
from utils import *
import time

seed = int(time.time())
random.seed(seed)
print("Seed for world =", seed)


class World:
    def __init__(self, canvas, width, height):
        self.pixWidth = 15
        self.width  = int(width / self.pixWidth)
        self.height = int(height / self.pixWidth)
        self.values = []
        self.pix = []
        for i in range(self.width):
            tmp = []
            tmpPix = []
            for j in range(self.height):
                r = random.random()
                tmp.append(r)
                xS = i * self.pixWidth
                xE = xS + (self.pixWidth)
                yS = j * self.pixWidth
                yE = yS + (self.pixWidth)
                col = rgb2hex((0, int(r * 255), 0))
                tmpPix.append(canvas.create_rectangle(xS, yS, xE , yE, fill=col, outline=""))
            self.values.append(tmp)
            self.pix.append(tmpPix)

    def show(self, canvas):
        for i in range(self.width):
            for j in range(self.height):
                self.values[i][j] -= random.random()  /1000
                if self.values[i][j] < 0:
                    self.values[i][j] = random.random()
                col = rgb2hex((0, int(self.values[i][j] * 255), 0))
                canvas.itemconfig(self.pix[i][j], fill=col)
