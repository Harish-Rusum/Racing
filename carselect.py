import pygame
import sys

pygame.init()

screenHeight = 600
screenWidth = 600
clock = pygame.time.Clock()
fps = 60
running = True
pressed = False

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Car Select")

# Imports
from utils.TextEngine import textRender
from utils.CenteringEngine import centerImageX


# Load assets
def loadImages():
    cars = {
        "black": {
            "big": [
                pygame.image.load(f"assets/Cars/car_black_{i}.png") for i in range(1, 6)
            ],
            "small": [
                pygame.image.load(f"assets/Cars/car_black_small_{i}.png")
                for i in range(1, 6)
            ],
        },
        "blue": {
            "big": [
                pygame.image.load(f"assets/Cars/car_blue_{i}.png") for i in range(1, 6)
            ],
            "small": [
                pygame.image.load(f"assets/Cars/car_blue_small_{i}.png")
                for i in range(1, 6)
            ],
        },
        "green": {
            "big": [
                pygame.image.load(f"assets/Cars/car_green_{i}.png") for i in range(1, 6)
            ],
            "small": [
                pygame.image.load(f"assets/Cars/car_green_small_{i}.png")
                for i in range(1, 6)
            ],
        },
        "red": {
            "big": [
                pygame.image.load(f"assets/Cars/car_red_{i}.png") for i in range(1, 6)
            ],
            "small": [
                pygame.image.load(f"assets/Cars/car_red_small_{i}.png")
                for i in range(1, 6)
            ],
        },
        "yellow": {
            "big": [
                pygame.image.load(f"assets/Cars/car_yellow_{i}.png")
                for i in range(1, 6)
            ],
            "small": [
                pygame.image.load(f"assets/Cars/car_yellow_small_{i}.png")
                for i in range(1, 6)
            ],
        },
    }

    colors = {
        "black": pygame.image.load("assets/colors/Black.png"),
        "blue": pygame.image.load("assets/colors/Blue.png"),
        "green": pygame.image.load("assets/colors/Green.png"),
        "red": pygame.image.load("assets/colors/Orange.png"),
        "yellow": pygame.image.load("assets/colors/Yellow.png"),
    }

    return cars, colors


playerSelections, colors = loadImages()

from scripts.player import Player
from scripts.tiles import backgroundRender


def renderCenterdText(text, yOffset=0):
    textSurf = textRender(text, (0, 0, 0))
    textX, textY = centerImageX(textSurf, screen, yOffset)
    screen.blit(textSurf, (textX, textY))


def numToColor(num):
    return {1: "black", 2: "blue", 3: "green", 4: "red", 5: "yellow"}[num]


def numToSize(num):
    return {1: "big", 2: "small"}[num]


def handleEvents():
    global running, pressed, screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYUP:
            if pygame.K_1 <= event.key <= pygame.K_5:
                pressed = False


def colorSelect():
    global running, pressed, screen
    while running:
        handleEvents()
        keys = pygame.key.get_pressed()
        for i in range(1, 6):
            if keys[pygame.K_0 + i] and not pressed:
                pressed = True
                return i

        screen.fill((255, 255, 255))
        backgroundRender(screen)
        renderCenterdText("Pick a color for your car", 200)

        positions = [(60, 300), (160, 300), (260, 300), (360, 300), (460, 300)]
        for curNumber, colorKey in enumerate(colors.keys(), start=1):
            screen.blit(colors[colorKey], positions[curNumber - 1])
            numberText = textRender(str(curNumber), (0, 0, 0))
            screen.blit(numberText, (positions[curNumber - 1][0] + 33, 390))

        pygame.display.flip()
        clock.tick(fps)


def modelSelect(color):
    global running, pressed, screen
    while running:
        handleEvents()
        screen.fill((255, 255, 255))
        keys = pygame.key.get_pressed()
        for i in range(1, 6):
            if keys[pygame.K_0 + i] and not pressed:
                pressed = True
                return i
        backgroundRender(screen)
        renderCenterdText("Pick a car model", 200)

        carImages = playerSelections[list(playerSelections.keys())[color - 1]]["big"]
        for curNumber, carImg in enumerate(carImages, start=1):
            screen.blit(carImg, (50 + 100 * (curNumber - 1), 250))

        positions = [(50, 300), (150, 300), (250, 300), (350, 300), (450, 300)]
        for curNumber in range(5):
            numberText = textRender(str(curNumber + 1), (0, 0, 0))
            screen.blit(numberText, (positions[curNumber][0] + 33, 390))

        pygame.display.flip()
        clock.tick(fps)


def sizeSelect(color, model):
    global running, pressed, screen
    while running:
        handleEvents()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and not pressed:
            pressed = True
            return 1
        if keys[pygame.K_2] and not pressed:
            pressed = True
            return 2

        backgroundRender(screen)
        renderCenterdText("Pick a size (big or small)", 200)

        positions = [(200, 300), (300, 300)]
        carOpts = [
            playerSelections[numToColor(color)]["big"][model - 1],
            playerSelections[numToColor(color)]["small"][model - 1],
        ]
        screen.blit(carOpts[0], (positions[0][0], positions[0][1]))
        screen.blit(carOpts[1], (positions[1][0], positions[1][1]))
        screen.blit(textRender("1", (0, 0, 0)), (230, 450))
        screen.blit(textRender("2", (0, 0, 0)), (320, 450))

        pygame.display.flip()
        clock.tick(fps)


def select():
    color = colorSelect()
    model = modelSelect(color)
    size = sizeSelect(color, model)
    player = Player(numToColor(color), numToSize(size), model, playerSelections)
    pygame.quit()
    return player
