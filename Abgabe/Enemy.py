import pygame 
import Colors as colors 

class Enemy:
    def __init__(self, x, y, width, height, speed=2, color=colors.red):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.color = color


    def update(self):
        pass

    
    
    # --- DRAW ---
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
