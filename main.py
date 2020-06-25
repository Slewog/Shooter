#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os  # Import of python modules.
import sys
from math import ceil
import pygame
from game import Game

os.environ['SDL_VIDEO_WINDOW_POS'] = "250,150"
pygame.init()  # Generate the game window.
pygame.display.set_caption("Shooter")  # Window title.
game_window = pygame.display.set_mode((1400, 800))  # Window size.
background = pygame.image.load('assets/background.jpg')  # Import window logo.
banner = pygame.image.load('assets/banner.png')  # Import banner.
banner = pygame.transform.scale(banner, (600, 600))
banner_rect = banner.get_rect()
banner_rect.x = ceil(game_window.get_width() / 3.5)
button_play = pygame.image.load('assets/button.png')  # Import button play.
button_play = pygame.transform.scale(button_play, (575, 250))
button_play_rect = button_play.get_rect()
button_play_rect.x = ceil(game_window.get_width() / 3.3)
button_play_rect.y = ceil(game_window.get_height() / 1.9)
if sys.platform == 'win32':
    pygame.display.set_icon(pygame.image.load("assets/logo.png"))  # Logo application if windows operating system.

game = Game(game_window)  # Creates an instance of the game class.
games_running = True  # Enables you to enter the game loop.

# Game loop.
while games_running:
    game_window.blit(background, (0, -130))  # Apply the background image on the game window.

    # Check if the game to start.
    if game.is_playing:
        game.update_game()
    else:  # Otherwise display the home screen
        game_window.blit(button_play, button_play_rect)  # Displays the play button_play.
        game_window.blit(banner, banner_rect)  # Displays the banner.

    pygame.display.flip()  # Update the game window.

    # Check the different events.
    for event in pygame.event.get():
        # Check if the player closes the game.
        if event.type == pygame.QUIT:
            games_running = False  # Exits the game loop.
            pygame.quit()  # Close the game.
        # Check if a key is pressed.
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True  # Stores the key pressed in a dictionary to the value TRUE.
            # If the SPACE key is activated, create a projectile.
            if event.key == pygame.K_SPACE:
                game.player.launch_bullets()
        # Check if a key is released.
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False  # Stores the released key in a dictionary to the value FALSE.
        # Check if a mouse button_play is pressed.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_play_rect.collidepoint(event.pos):
                game.start_game()
