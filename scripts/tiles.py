import pygame


def backgroundRender(surface):
    c = 0
    tiles = [
        pygame.transform.scale(
            pygame.image.load("assets/Tiles/grass.png").convert_alpha(), (40, 40)
        )
    ] * (15**2)
    for i in range(15):
        x = i * 40
        for j in range(15):
            y = j * 40
            surface.blit(tiles[c], (x, y))
            c += 1


def trackRender(surface):
    c = 0
    offsetX = 150
    tiles = [
        pygame.transform.scale(
            pygame.image.load("assets/Tiles/asphalt.png").convert_alpha(), (40, 40)
        )
    ] * (7 * 15)

    for i in range(7):
        x = offsetX + (i * 40)
        for j in range(15):
            y = j * 40
            surface.blit(tiles[c], (x, y))
            c += 1
