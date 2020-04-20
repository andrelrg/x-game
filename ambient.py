import random
import time
from screen import yLim

def ambientGen(t):
    l1 = 4
    l2 = yLim-4
    while (1):
        l = random.randint(-1,1)
        la = Ambient("left", 0, l1+l)
        ra = Ambient("right", 0, l2-l)
        t.register(la)
        t.register(ra)
        time.sleep(0.3)
        t.unregister(la)
        t.unregister(ra)


class Ambient:
    rep = "{"
    def __init__(self, orientation, x=0, y=0):
        if orientation == "left":
            self.rep = "}"
        self.line = x
        self.column = y


