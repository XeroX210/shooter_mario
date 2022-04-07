import pygame
import random


# crée les monstres

class Monster(pygame.sprite.Sprite):

    def __init__(self, game, health, attack, file, max_health, type, velocity):
        super().__init__()
        self.game = game
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.image = pygame.image.load(file).convert_alpha()
        self.type = type
        self.rect = self.image.get_rect()
        if self.type == "Goomba":
            self.image = pygame.transform.scale(self.image, (35, 35))
            self.rect.x = 1050 + random.randint(0, 300)
            self.rect.y = 650
        elif self.type == "Boss":
            self.image = pygame.transform.scale(self.image, (140, 140))
            self.rect.x = 1150 + random.randint(0, 300)
            self.rect.y = 550
        self.velocity = velocity

    def damage(self, amount):
        # infliger des degats
        self.health -= amount

        # verifier si son nombre de pts de vie est <= a 0
        if self.health <= 0:
            self.rect.x = 1150 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health
            # Ajout du score
            self.game.score += 10
            if self.type == "Boss":
                self.velocity = 0
                self.game.score += 40

    def update_health_bar(self, surface):
        # dessiner la barre
        if self.type == "Goomba":
            pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 25, self.rect.y - 20, self.max_health, 5])
            pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 25, self.rect.y - 20, self.health, 5])
        elif self.type == "Boss":
            pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 40, self.rect.y - 20, self.max_health / 2, 5])
            pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 40, self.rect.y - 20, self.health / 2, 5])

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            self.game.player.damage(self.attack)
