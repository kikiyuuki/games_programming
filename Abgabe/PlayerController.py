import pygame

class PlayerController:
    def __init__(self, x, y, width, height, speed=5):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    # --- INPUT ---
    def handle_input(self):
        keys = pygame.key.get_pressed()
        
        dx, dy = 0, 0

        if keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            dx += self.speed
        if keys[pygame.K_UP]:
            dy -= self.speed
        if keys[pygame.K_DOWN]:
            dy += self.speed

        return dx, dy

    # --- UPDATE ---
    def update(self):
        dx, dy = self.handle_input()
        self.move(dx, dy)

    # --- MOVEMENT ---
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    # --- DRAW ---
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)