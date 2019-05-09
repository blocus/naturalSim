from utils import *
import random
import numpy as np

class Pixie:
    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y
        self.r = 3
        self.speed = int(random.random() * 5) + 1
        xS = self.x - self.r
        xE = self.x + self.r
        yS = self.y - self.r
        yE = self.y + self.r
        self.body = canvas.create_oval(xS, yS, xE, yE, fill="#FFFFFF", outline="")
        self.target = canvas.create_line(0, 0, 0, 0)

    def move(self, canvas, x, y):
        canvasWidth = float(canvas["width"])
        canvasHeight = float(canvas["height"])
        if x < 0:
            x = 0
        elif x > canvasWidth:
            x = canvasWidth
        if y < 0:
            y = 0
        elif y > canvasHeight:
            y = canvasHeight

        self.x = x
        self.y = y
        xS = self.x - self.r
        xE = self.x + self.r
        yS = self.y - self.r
        yE = self.y + self.r
        canvas.coords(self.body, xS, yS, xE, yE)

    def goTo(self, canvas, foods):
        record = np.inf
        index = 0
        i = 0
        if(len(foods) == 0):
            return False

        for food in foods:
            d = dist(self.x, self.y, food.x, food.y)
            if d < record:
                record = d
                index = i
            i += 1

        food = foods[index]
        d = dist(self.x, self.y, food.x, food.y)

        if d <= self.speed:
            self.move(canvas, food.x, food.y)
            foods.pop(index)
            canvas.delete(food.body)
            return True

        den = self.x - food.x
        if den != 0:
            slope = (self.y - food.y) / den
            angle = np.arctan(slope)
            if self.x > food.x:
                angle += np.pi
            dx = np.cos(angle) * self.speed
            dy = np.sin(angle) * self.speed
        else:
            dx = 0
            dy = self.speed
            if self.y > food.y:
                dy = - self.speed

        self.move(canvas, self.x + dx, self.y + dy)
        canvas.coords(self.target, self.x, self.y, self.x + (dx * 10), self.y + (dy * 10))
