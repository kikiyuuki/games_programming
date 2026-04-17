import pygame
pygame.init()

def create_player(x, y, width, height):
    return pygame.Rect(x, y, width, height)

def spawn_player(x, y, width, height):
    player = create_player(x, y, width, height)
    pygame.draw.rect(screen, (255, 255, 255), player)
    return player
