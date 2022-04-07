import pygame
import random

# classe pour gérer cette comete

class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        # définir l'image de la comet
        self.image = pygame.image.load('Mario/Champignon.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3,5)
        self.rect.x = random.randint(20,950)
        self.rect.y = - random.randint(0,717)
        self.damage = 20
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

    def fall(self):
        self.rect.y += self.velocity

        # le champi ne tombe pas sur le sol
        if self.rect.y >= 700:
            # enlever le champi
            self.remove()

        #vérifier si le champi touche le joueur
        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_players
        ):
            # retirer la boule de feu
            self.remove()
            # dmg player
            self.comet_event.game.player.damage(20)



