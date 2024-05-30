import random


class Lane:
    def __init__(self, x):
        self.speed = random.randrange(4,8)
        self.x = x
