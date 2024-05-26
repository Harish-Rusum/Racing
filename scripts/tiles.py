import pygame


def backgroundRender(surface):
    tiles = pygame.transform.scale(
        pygame.image.load("assets/Tiles/grass.png").convert_alpha(), (40, 40)
    )
    for i in range(15):
        x = i * 40
        for j in range(15):
            y = j * 40
            surface.blit(tiles, (x, y))


def trackRender(surface):
    offsetX = 90
    tiles1 = pygame.transform.scale(
        pygame.image.load("assets/Tiles/asphalt1.png").convert_alpha(), (60, 60)
    )

    tiles2 = pygame.transform.scale(
        pygame.image.load("assets/Tiles/asphalt2.png").convert_alpha(), (60, 60)
    )

    for i in range(7):
        x = offsetX + (i * 60)
        for j in range(10):
            y = j * 60
            if i % 2 == 0:
                surface.blit(tiles1, (x, y))
            else:
                surface.blit(tiles2, (x, y))
