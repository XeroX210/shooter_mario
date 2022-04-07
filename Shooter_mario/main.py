import pygame, sys, time
from game import Game
import math
from pygame.locals import *

pygame.init()



# Fenetre de notre jeux

pygame.display.set_caption("Shooter")
screen = pygame.display.set_mode((1080, 720))

# Image de fond

background = pygame.image.load('Mario/Fond.png')
background = pygame.transform.scale(background, (1080, 720))

# Bouton play

B = pygame.image.load("bouton play.png").convert_alpha()
B = pygame.transform.scale(B, (300, 300))
B_rect = B.get_rect()
B_rect.x = math.ceil(screen.get_width() / 2.7)
B_rect.y = math.ceil(screen.get_height() / 3.7)

# Bouton parametre

P = pygame.image.load("P.png").convert_alpha()
P = pygame.transform.scale(P, (50, 50))
P_rect = P.get_rect()
P_rect.x, P_rect.y = 1020, 650

P2 = pygame.image.load("Parametre.png").convert_alpha()
P2 = pygame.transform.scale(P2, (1080, 720))
P2_rect = P2.get_rect()

# charger notre jeux

game = Game()

running = True

# Menu du jeux
Menu = pygame.image.load('Mario/Fond.png')
Menu = pygame.transform.scale(Menu, (1080, 720))


def option_menu():
    in_option = 1
    while in_option:
        for event2 in pygame.event.get():
            if event2.type == pygame.QUIT:
                in_option = 0
            if event2.type == pygame.KEYDOWN:
                if event2.key == pygame.K_ESCAPE:
                    in_option = 0

        screen.blit(P2, P2_rect)
        pygame.display.update()

def menudefin():
    continuer=True

    while continuer:
        fenetre.fill((0,0,0))
        font = pygame.font.Font(None, 48)
        text = font.render("Press enter to restart or Press space to quit", 1, (0, 0, 255))
        textpos = text.get_rect()
        textpos.centerx, textpos.centery=largeur/2, hauteur/2+10

        fenetre.blit(text,textpos)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer=0
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    continuer=False
                    menu()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    continuer=False


# Boucle

while running:

    # Image de fond
    screen.blit(background, (0, 0))

    # Verifier si notre jeux a commencé
    if game.is_playing:
        # Déclancher les instructions de la partie
        game.update(screen)
    # Si il a pas commencé
    else:
        # ecran de bienvenue
        screen.blit(B, B_rect)

        # Regles
        screen.blit(P, P_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
                #Tire.play()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verif si la souris touche le bouton
            if B_rect.collidepoint(event.pos):
                # Le jeux en mode True
                game.start()
            if P_rect.collidepoint(event.pos):
                option_menu()

    pygame.display.update()
