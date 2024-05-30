import random

class Lane:
    def __init__(self, clear, x):
        self.clear = clear
        self.speed = random.randint(3,8)
        self.x = x

    def randomizeSpeed(self):
        self.speed = random.randint(1,5)
