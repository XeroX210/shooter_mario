import pygame
import random
from player import Player
from comet_event import CometFallEvent
from monster import Monster

# Seconde class

class Game:
    def __init__(self):
        # Definir si notre jeux a commencé
        self.is_playing = False
        # Generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Manager de la pluie de champi
        self.comet_event = CometFallEvent(self)
        # Groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        # Score a 0
        self.score = 0
        self.Boss = Monster(self, 500, 0.5, "Mario/Boo.png", 300, "Boss", 0)

    def start(self):
        self.is_playing = True
        self.spawn_monsters()
        self.spawn_monsters()
        self.spawn_monsters()
        self.spawn_monsters()
        self.spawn_boss()

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        self.comet_event.reset_percent()

    def update(self, screen):

        # Spawn du boss
        if self.score % 200 == 0 and self.score != 0:
            self.Boss.velocity = 1

        # Afficher le score
        font = pygame.font.SysFont("monospace", 16)
        score_text = font.render(f"Score : {self.score}", 1, (255, 255, 255))
        screen.blit(score_text, (20, 20))

        if self.score >= 1500:
            Game.game_over(self)

        # Image du personnage

        screen.blit(self.player.image, self.player.rect)

        # barre de vie joueur

        self.player.update_health_bar(screen)

        # Actualiser la barre d'event du jeu

        self.comet_event.update_bar(screen)

        # Recuperer les projectiles du joueur

        for projectile in self.player.all_projectile:
            projectile.move()

        # Recuperer les monsters

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # Recupere les cometes

        for comet in self.comet_event.all_comets:
            comet.fall()
            if self.is_playing == False:
                comet.remove()
                self.game_over()

        # Appliquer l'ensemble des images de projectile

        self.player.all_projectile.draw(screen)

        # Appliquer l'ensemble des images des monstres
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des images de mon groupe de cometes
        self.comet_event.all_comets.draw(screen)

        # verifier ou va le jouer
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monsters(self):
        monster = Monster(self, 100, 0.5, "Mario/Goomba.png", 100, "Goomba", 2 + random.randint(1, 2))
        self.all_monsters.add(monster)

    def spawn_boss(self):
        self.all_monsters.add(self.Boss)
