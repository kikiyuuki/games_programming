import PlayerController as PlayerController
import Enemy as Enemy

class Game:
    def __init__(self):
        self.entities = []

    def spawn_player(self, x, y):
        player = PlayerController.PlayerController(x, y, 40, 40)
        self.entities.append(player)
    
    def spawn_enemy(self, x, y):
        enemy = Enemy.Enemy(x, y, 80, 40)
        self.entities.append(enemy)

    def update(self):
        for entity in self.entities:
            entity.update()

    def draw(self, screen):
        for entity in self.entities:
            entity.draw(screen)