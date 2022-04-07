import pygame
from projectile import Projectile


# Creer une premiere classe ( Joueur)

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 3
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load('Mario/MarioJeux.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (45, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 470
        self.rect.y = 625

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # Si Mario a 0 hp
            self.game.game_over()

    def update_health_bar(self, surface):
        # dessiner la barre
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 25, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 25, self.rect.y - 20, self.health, 5])

    def launch_projectile(self):

        self.all_projectile.add(Projectile(self))

    # Deplacement de mario
    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
