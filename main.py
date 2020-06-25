#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os  # Import of python modules.
import sys
from math import ceil
import pygame
from game import Game

pygame.init()  # Generate the game window.
# os.environ['SDL_VIDEO_WINDOW_POS'] = str(ceil(pygame.display.Info().current_w / 7)) + "," + str(ceil(pygame.display.Info().current_h / 7))  # Place the window at a certain position on the screen.
os.environ['SDL_VIDEO_CENTERED'] = '1'  # Center window on screen.
pygame.display.set_caption("Tree Survival")  # Window title.
game_window = pygame.display.set_mode((1400, 800))  # Window size.
background = pygame.image.load('assets/background.jpg')  # Import window background.
logo = pygame.image.load("assets/logo.png")  # Import window logo.
banner = pygame.image.load('assets/banner.png')  # Import banner.
banner = pygame.transform.scale(banner, (600, 600))  # Set the size of the banner.
banner_rect = banner.get_rect()  # Get position.
banner_rect.x = ceil(game_window.get_width() / 3.5)  # Defines the X position of the banner.
banner_rect.y = -50  # Defines the Y position.
button_play = pygame.image.load('assets/button.png')  # Import button play.
button_play = pygame.transform.scale(button_play, (500, 200))  # Set the size of the button.
button_play_rect = button_play.get_rect()  # Get position.
button_play_rect.x = ceil(game_window.get_width() / 3.1)  # Defines the X position.
button_play_rect.y = ceil(game_window.get_height() / 1.9)  # Defines the Y position.
if sys.platform == 'win32':  # Logo application if windows operating system.
    pygame.display.set_icon(logo)

game = Game(game_window)  # Creates an instance of the game class.
games_running = True  # Enables you to enter the game loop.
font = pygame.font.Font('assets/fonts/Kid Games.ttf', 24)  # Copyright Label Font.
pos_copyright_x = ceil(game_window.get_width() / 2.5)  # Score Label copyright position.
pos_copyright_y = 750

# Game loop.
while games_running:
    game_window.blit(background, (0, -130))  # Apply the background image on the game window.

    # Check if the game to start.
    if game.is_playing:
        game.game_update()  # Load the game.
    else:  # Otherwise display the home screen
        game_window.blit(button_play, button_play_rect)  # Displays the play button_play.
        game_window.blit(banner, banner_rect)  # Displays the banner.
        game_window.blit(font.render("DEVELOP BY SLEWOG", True, (255, 255, 255)), (pos_copyright_x, pos_copyright_y))

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
            # If the RETURN key is activated, create a projectile.
            if event.key == pygame.K_RETURN:
                game.player.launch_bullets()
        # Check if a key is released.
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False  # Stores the released key in a dictionary to the value FALSE.
        # Check if a mouse button_play is pressed.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check the play button has been pressed.
            if button_play_rect.collidepoint(event.pos):
                game.game_start()  # Load the starting monsters and place the player.
