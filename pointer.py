import getch
from screen import xLim, yLim

up = "w"
down = "s"
left = "a"
right = "d"

class Pointer:
    def __init__(self, screen, x=10, y=1, rep='X'):
        self.line = x
        self.column = y
        self.screen = screen
        self.rep = rep
        self.screen.register(self)
    
    def WaitToWalk(self):
        while(1):
            c = getch.getch()
            if c == up:
                self.screen.unregister(self)
                self.line -= 1
                if self.line == 0:
                    self.line = xLim - 1 
                self.screen.register(self)
            elif c == down:
                self.screen.unregister(self)
                self.line += 1
                if self.line == xLim:
                    self.line = 1
                self.screen.register(self)
            elif c == left:
                self.screen.unregister(self)
                self.column -= 1
                if self.column == 0:
                    self.column = yLim - 1
                self.screen.register(self)
            elif c == right:
                self.screen.unregister(self)
                self.column += 1
                if self.column == yLim:
                    self.column = 1
                self.screen.register(self)
