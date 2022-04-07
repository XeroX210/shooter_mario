import pygame
from comet import Comet

# Créer une classe pour l'event
class CometFallEvent:

    # Lors du Chargement crée un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game

        # definir un groupe de spritz pour stocker nos comètes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # Apparaitre un champi
        for loop in range(30):
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # la jauge d'event est full
        if self.is_full_loaded():
            print("Pluie de comètes ! ")
            self.meteor_fall()
            self.reset_percent()
        if self.game.is_playing == False:
            self.all_comets.remove(Comet(self))
            self.percent.remove()



    def update_bar(self, surface):
        # add percent
        self.add_percent()

        # Appel de la methode pour essayer de mettre la pluie de cometes
        self.attempt_fall()

        # barre noire
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # X
            surface.get_height() - 20,  # Y
            surface.get_width() ,  # Longueur de la fenetre
            10  # Epaisseur de la barre
        ])

        # Barre rouge
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # X
            surface.get_height() - 20,  # Y
            (surface.get_width() / 100) * self.percent,  # Longueur de la fenetre
            10  # Epaisseur de la barre

        ])
