from screen import Screen
from pointer import Pointer
from player import Player
# import threading

if __name__ == "__main__":
    t = Screen()
    p = Pointer(t)
    player = Player(p)
    player.Walk()
