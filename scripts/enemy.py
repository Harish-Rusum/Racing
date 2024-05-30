import random
import pygame


class Car:
    def __init__(self, cars, lane):
        self.cars = cars
        self.lane = lane
        self.x = self.lane.x
        self.y = -50
        self.notOffScreen = True

    def pick(self, player):
        self.color = random.choice(["black", "green", "red", "blue", "yellow"])
        self.model = random.choice([0, 1, 2, 3, 4])
        self.size = random.choice(["big", "small"])

        while (
            self.color == player.color
            and self.model == player.model - 1
            and self.size == player.size
        ):
            self.color = random.choice(["black", "green", "red", "blue", "yellow"])
            self.model = random.choice([0, 1, 2, 3, 4])
            self.size = random.choice(["big", "small"])

        self.img = self.cars[self.color][self.size][self.model]
        self.rect = self.img.get_rect()

    def update(self):
        if not self.lane.clear:
            self.y += self.lane.speed
            self.rect.x = self.x
            self.rect.y = self.y
            if self.y > 600:
                self.notOffScreen = False

    def scale(self):
        self.img = pygame.transform.smoothscale(self.img, (40, 62))

    def render(self, surface):
        if not self.lane.clear:
            surface.blit(self.img, self.rect)
