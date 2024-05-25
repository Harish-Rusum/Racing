import pygame


def textRender(textString, textColor):
    font = pygame.font.Font("assets/fonts/kaph-regular.ttf", 13)
    text = font.render(textString, True, textColor)
    return text
