#!/usr/bin/env python3
import pygame

pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initializing Color
color = (180, 180, 180)
color2 = (0, 0, 0)

# create a text surface object,
# on which text is drawn on it.

# create a rectangular object for the
# text surface object


def draw_rect(x, y, screen):
    pygame.draw.rect(surface, color, pygame.Rect(x, y, 800, 700))


def draw_text(x, y, input, size, screen):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(input, True, color2)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)
