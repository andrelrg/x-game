from pointer import up, down, left, right

class Player():
    def __init__(self, pointer):
        self.pointer = pointer

    def Walk(self):
        self.pointer.WaitToWalk()