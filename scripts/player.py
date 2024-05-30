import pygame


class Player:
    def __init__(self, color, size, model, selections,x,y):
        self.color = color
        self.model = model
        self.size = size
        self.img = selections[self.color][self.size][self.model - 1]
        self.rect = self.img.get_rect()
        self.x = x
        self.y = y

    def render(self, surface):
        self.rect.x = self.x
        self.rect.y = self.y
        surface.blit(self.img, self.rect)
    
    def right(self):
        self.x = min(self.x + 60, 460)

    def left(self):
        self.x = max(self.x - 60, 100)

    def up(self):
        self.y = min(self.y + 60, 530)

    def down(self):
        self.y = max(self.y - 60, 60)

    def scale(self):
        self.img = pygame.transform.smoothscale(self.img, (40, 62))
