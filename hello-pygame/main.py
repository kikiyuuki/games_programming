import pygame
import testing as test
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
player1posX, player1posY = 400, 300
player2posX, player2posY = 50, 50

player1Color = (255, 107, 53)
player2Color = (40, 80, 30)
running = True
gotCaught = False


my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Du wurdest gefangen', False, (255, 255, 255))

def displayText():
    screen.blit(text_surface, (200,0))


def spawn_player(x, y, width, height):
    player = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, (255, 0, 255), player)
    return player

    


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player1posX -= 5
    if keys[pygame.K_RIGHT]: player1posX += 5
    if keys[pygame.K_UP]:    player1posY -= 5
    if keys[pygame.K_DOWN]:  player1posY += 5
    if keys[pygame.K_SPACE]: player3 = spawn_player(player1posX, player1posY, 40, 40)

    if keys[pygame.K_w]: player2posY -= 5
    if keys[pygame.K_s]: player2posY += 5
    if keys[pygame.K_a]: player2posX -= 5
    if keys[pygame.K_d]: player2posX += 5

    # Kollisionserkennung
    player1_rect = pygame.Rect(player1posX, player1posY, 40, 40)
    player2_rect = pygame.Rect(player2posX, player2posY, 20, 20)
    if player1_rect.colliderect(player2_rect):
        gotCaught = True

    screen.fill((11, 13, 16))

    if gotCaught:
        displayText()

    borderNorth = pygame.draw.rect(screen, (255,0,0), (0,0,800,3))
    borderWest = pygame.draw.rect(screen, (255,0,0), (0,0,3,600))
    borderSouth = pygame.draw.rect(screen, (255,0,0), (0,597,800,3))
    borderEast = pygame.draw.rect(screen, (255,0,0), (797,0,3,600))

    player1 = pygame.draw.rect(screen, player1Color, (player1posX, player1posY, 40, 40))
    player2 = pygame.draw.rect(screen, player2Color, (player2posX, player2posY, 20, 20))

    pygame.display.flip()
    clock.tick(60)
        

    if player1.colliderect(borderNorth) or player1.colliderect(borderWest) or player1.colliderect(borderSouth) or player1.colliderect(borderEast)   :
        player1posX, player1posY = 400, 300

    if (gotCaught):
        displayText()



    pygame.display.flip()
    clock.tick(60)

pygame.quit()