import random
import sys

import pygame

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
display = pygame.surface.Surface((screenWidth, screenHeight))
pygame.display.set_caption("Racing")

from scripts.enemy import Car
from scripts.lane import Lane
from scripts.tiles import backgroundRender, trackRender
from utils.CenteringEngine import centerImageX
from utils.TextEngine import textRender


def renderCenterdText(text, size, yOffset=0):
    textSurf = textRender(text, (0, 0, 0), size)
    textX, textY = centerImageX(textSurf, display, yOffset)
    display.blit(textSurf, (textX, textY))


def handleEvents():
    global running, pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key in (pygame.K_l, pygame.K_d, pygame.K_RIGHT):
                if not pressed:
                    player.right()
                    pressed = True
            elif event.key in (pygame.K_h, pygame.K_a, pygame.K_LEFT):
                if not pressed:
                    player.left()
                    pressed = True
            elif event.key in (pygame.K_k, pygame.K_w, pygame.K_UP):
                if not pressed:
                    player.up()
                    pressed = True
            elif event.key in (pygame.K_j, pygame.K_s, pygame.K_DOWN):
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
                pygame.K_DOWN,
                pygame.K_UP,
                pygame.K_RIGHT,
                pygame.K_LEFT,
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
xOffset, yOffset = 0, 0
screenShake = False
plaque = pygame.image.load("assets/tiles/plaque.png")
cooldownTimer = 30


def menu():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                else:
                    return
            if event.type == pygame.QUIT:
                sys.exit()
        display.fill((0, 0, 0))
        backgroundRender(display)
        trackRender(display)
        display.blit(plaque, (0, 0))

        renderCenterdText("press any key", 30, 25)
        player.render(display)

        screen.blit(display, (0 + xOffset, 0 + yOffset))

        pygame.display.flip()
        clock.tick(fps)


def main():
    global time, score, cars, running, highScore, xOffset, yOffset, screenShake, cooldownTimer
    while running:
        handleEvents()

        display.fill((0, 0, 0))
        backgroundRender(display)
        trackRender(display)

        cars = [car for car in cars if car.notOffScreen]
        for car in cars:
            if car.notOffScreen:
                car.update()
                car.render(display)

        player.render(display)

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
                    car.notOffScreen = False
                    score -= 2
                    car.collidedWith = True
                    screenShake = True
            else:
                car.collidedWith = False
        if screenShake:
            cooldownTimer -= 1
        if cooldownTimer <= 0:
            screenShake = False
            cooldownTimer = 30
        if score < 0:
            return
        display.blit(plaque, (0, 0))
        if score >= 0:
            renderCenterdText(str(score), 40, 25)

        if screenShake:
            xOffset = random.randint(0, 8) - 4
            yOffset = random.randint(0, 8) - 4
        screen.blit(display, (0 + xOffset, 0 + yOffset))

        time = (time + 1) % 1000000
        pygame.display.flip()
        clock.tick(fps)


def endScreen():
    global time, running, highScore, xOffset, yOffset
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
        display.fill((0, 0, 0))
        backgroundRender(display)
        display.blit(plaque, (0, 250))
        renderCenterdText(f"highScore : {highScore}", 30, 280)
        screen.blit(display, (0 + xOffset, 0 + yOffset))
        pygame.display.flip()
        clock.tick(fps)


menu()
main()
endScreen()
pygame.quit()
sys.exit()
