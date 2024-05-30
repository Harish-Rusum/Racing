import pygame
import sys
from carselect import select

player,playerSelections = select()

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


def handleEvents():
    global running, pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                if not pressed:
                    player.right()
                    pressed = True
            if event.key == pygame.K_h:
                if not pressed:
                    player.left()
                    pressed = True
            if event.key == pygame.K_k:
                if not pressed:
                    player.down()
                    pressed = True
            if event.key == pygame.K_j:
                if not pressed:
                    player.up()
                    pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_l:
                pressed = False
            if event.key == pygame.K_h:
                pressed = False
            if event.key == pygame.K_j:
                pressed = False
            if event.key == pygame.K_k:
                pressed = False


player.scale()

lanes = [
    Lane(False,100),
    Lane(False,160),
    Lane(False,220),
    Lane(True,280),
    Lane(False,340),
    Lane(False,400),
    Lane(False,460),
]

cars = [
    Car(playerSelections,lanes[0]),
    Car(playerSelections,lanes[1]),
    Car(playerSelections,lanes[2]),
    Car(playerSelections,lanes[3]),
    Car(playerSelections,lanes[4]),
    Car(playerSelections,lanes[5]),
    Car(playerSelections,lanes[6]),
]
for car in cars:
    car.pick(player)
    car.scale()

while running:
    handleEvents()

    screen.fill((0, 0, 0))
    backgroundRender(screen)
    trackRender(screen)

    player.render(screen)
    
    for i in range(len(cars)):
        car = cars[i]
        if car.notOffScreen:
            car.update()
            car.render(screen)


    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
