import os

xLim = 20
yLim = 20
class Screen:
    def __init__(self):
        self._map = [ [ 0 for y in range( xLim ) ] for x in range( yLim ) ]
        self.draw()
    
    def draw(self, obj=None):
        os.system('clear')
        p = False
        for x in self._map: #Line
            for y in x: #Column
                if y:
                    print(y, end = '')
                print(" ", end = '')
            print()
        
    def register(self, obj):
        if not self._map[obj.line][obj.column]:
            self._map[obj.line][obj.column] = obj.rep
            self.draw()
    
    def unregister(self, obj):
        if self._map[obj.line][obj.column]:
            self._map[obj.line][obj.column] = 0
