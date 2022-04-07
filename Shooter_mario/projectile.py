import pygame


# Definir la classe du projectile
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("Mario/Etoile.png")
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 30
        self.rect.y = player.rect.y + 20
        self.origin_image = self.image
        self.angle = 0
        # Animation de l'etoile
    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verifier si le projectile touche un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer les projectiles
            self.remove()
            #infliger des degats
            monster.damage(self.player.attack)

            if self.rect.x > 1080:
             self.remove


