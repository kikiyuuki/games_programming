
import pygame
import Colors as colors
from Game import Game

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

game = Game()
game.spawn_player(400, 300)
game.spawn_enemy(100, 100)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---- Update ----
    game.update()

    # ---- Draw ----
    screen.fill(colors.black)
    game.draw(screen)

    pygame.display.flip()
    clock.tick(60)

