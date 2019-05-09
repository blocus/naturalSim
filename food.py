import random
class Food:
    def __init__(self, canvas, color = "red"):
        x = random.random() * int(canvas["width"])
        y = random.random() * int(canvas["height"])
        if x < 10:
            x = 10
        if y < 10:
            y = 10

        if x > int(canvas["width"]) - 10:
            x = int(canvas["width"]) - 10
        if y > int(canvas["height"]) - 10:
            y = int(canvas["height"]) - 10

        self.x = x
        self.y = y

        self.r = 2
        self.color = color
        xS = self.x - self.r
        xE = self.x + self.r
        yS = self.y - self.r
        yE = self.y + self.r
        self.body = canvas.create_oval(xS, yS, xE, yE, fill=color, outline="")
