import os
os.environ['SDL_VIDEODRIVER'] = 'x11'

import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("WSL Pygame Test")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

