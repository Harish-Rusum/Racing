import pygame
import sys
from carselect import select

player = select()

pygame.init()

screenWidth = 600
screenHeight = 600
clock = pygame.time.Clock()
fps = 60
running = True
pressed = False

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Racing")

from scripts.player import Player
from scripts.tiles import backgroundRender
from scripts.tiles import trackRender


def handleEvents():
    global running, pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                pressed = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                pressed = False


playerX = 0
playerY = 0

while running:
    handleEvents()

    screen.fill((0, 0, 0))  # Clear the screen
    backgroundRender(screen)
    trackRender(screen)

    player.render(playerX, playerY, screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
