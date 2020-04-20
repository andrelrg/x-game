from screen import Screen
from pointer import Pointer
from player import Player
from ambient import ambientGen
import threading

if __name__ == "__main__":
    t = Screen()
    p = Pointer(t)
    player = Player(p)
    ambient = threading.Thread(target=ambientGen, args=(t,))
    ambient.start()
    # ambientGen(t)
    player.Walk()

