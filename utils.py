import numpy as np

def rgb2hex(rgb):
    return "#%02x%02x%02x" % rgb

def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
