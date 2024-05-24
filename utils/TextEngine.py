import pygame


def textRender(textString, textColor):
    font = pygame.font.Font("Assets/fonts/kaph-regular.ttf", 13)
    text = font.render(textString, True, textColor)
    return text
