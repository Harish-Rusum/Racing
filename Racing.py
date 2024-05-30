import pygame
import random
import sys
from carselect import select

player, playerSelections = select()

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
from scripts.enemy import Car
from scripts.lane import Lane
from scripts.tiles import backgroundRender
from scripts.tiles import trackRender


from utils.TextEngine import textRender
from utils.CenteringEngine import centerImageX


def renderCenterdText(text, size, yOffset=0):
    textSurf = textRender(text, (0, 0, 0), size)
    textX, textY = centerImageX(textSurf, screen, yOffset)
    screen.blit(textSurf, (textX, textY))


def handleEvents():
    global running, pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l or event.key == pygame.K_d:
                if not pressed:
                    player.right()
                    pressed = True
            if event.key == pygame.K_h or event.key == pygame.K_a:
                if not pressed:
                    player.left()
                    pressed = True
            if event.key == pygame.K_k or event.key == pygame.K_w:
                if not pressed:
                    player.down()
                    pressed = True
            if event.key == pygame.K_j or event.key == pygame.K_s:
                if not pressed:
                    player.up()
                    pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_l or event.key == pygame.K_d:
                pressed = False
            if event.key == pygame.K_h or event.key == pygame.K_a:
                pressed = False
            if event.key == pygame.K_j or event.key == pygame.K_w:
                pressed = False
            if event.key == pygame.K_k or event.key == pygame.K_s:
                pressed = False


player.scale()

lanes = [
    Lane(100),
    Lane(160),
    Lane(220),
    Lane(280),
    Lane(340),
    Lane(400),
    Lane(460),
]

cars = []
spawnRate = 40
time = 0
score = 0

plaque = pygame.image.load("assets/tiles/plaque.png")

while running:
    handleEvents()

    screen.fill((0, 0, 0))
    backgroundRender(screen)
    trackRender(screen)

    cars = [car for car in cars if car.notOffScreen]
    for i in range(len(cars)):
        car = cars[i]
        if car.notOffScreen:
            car.update()
            car.render(screen)

    player.render(screen)

    if time % spawnRate == 0:
        for i in range(len(lanes)):
            if random.choice(["yes", "no"]) == "yes":
                cars.append(Car(playerSelections, lanes[i], player))

    if time % fps == 0:
        score += 1
    
    screen.blit(plaque,(0,0))
    renderCenterdText(str(score), 40,25)


    time = time + 1 % 1000000
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
