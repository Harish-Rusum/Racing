import pygame
import random
import sys
from carselect import select

player, playerSelections = select()

pygame.init()
pygame.mixer.init()

screenWidth = 600
screenHeight = 600
clock = pygame.time.Clock()
fps = 60
running = True
pressed = False

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Racing")

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
            if event.key in (pygame.K_l, pygame.K_d):
                if not pressed:
                    player.right()
                    pressed = True
            elif event.key in (pygame.K_h, pygame.K_a):
                if not pressed:
                    player.left()
                    pressed = True
            elif event.key in (pygame.K_k, pygame.K_w):
                if not pressed:
                    player.up()
                    pressed = True
            elif event.key in (pygame.K_j, pygame.K_s):
                if not pressed:
                    player.down()
                    pressed = True
        if event.type == pygame.KEYUP:
            if event.key in (
                pygame.K_l,
                pygame.K_d,
                pygame.K_h,
                pygame.K_a,
                pygame.K_j,
                pygame.K_w,
                pygame.K_k,
                pygame.K_s,
            ):
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
highScore = 0
crash = pygame.mixer.Sound("assets/audio/hit.wav")
track = pygame.mixer.Sound("assets/audio/track.mp3")
track.play(-1)

plaque = pygame.image.load("assets/tiles/plaque.png")


def menu():
    global time, running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                else:
                    return
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        backgroundRender(screen)
        trackRender(screen)
        screen.blit(plaque, (0, 0))

        renderCenterdText("press any key", 30, 25)
        player.render(screen)

        pygame.display.flip()
        clock.tick(fps)


def main():
    global time, score, cars, running, highScore
    while running:
        handleEvents()

        screen.fill((0, 0, 0))
        backgroundRender(screen)
        trackRender(screen)

        cars = [car for car in cars if car.notOffScreen]
        for car in cars:
            if car.notOffScreen:
                car.update()
                car.render(screen)

        player.render(screen)

        if time % spawnRate == 0:
            for lane in lanes:
                if random.choice(["yes", "no"]) == "yes":
                    cars.append(Car(playerSelections, lane, player))

        if time % fps == 0:
            score += 1
            highScore = max(score, highScore)
        for car in cars:
            if car.rect.colliderect(player.rect):
                if not car.collidedWith:
                    crash.play()
                    score -= 2
                    car.collidedWith = True
            else:
                car.collidedWith = False

        if score < 0:
            return
        screen.blit(plaque, (0, 0))
        if score >= 0:
            renderCenterdText(str(score), 40, 25)

        time = (time + 1) % 1000000
        pygame.display.flip()
        clock.tick(fps)


def endScreen():
    global time, running, highScore
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        backgroundRender(screen)
        screen.blit(plaque, (0, 250))
        renderCenterdText(f"highScore : {highScore}", 30, 280)
        pygame.display.flip()
        clock.tick(fps)


menu()
main()
endScreen()
pygame.quit()
sys.exit()
