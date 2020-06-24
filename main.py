#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os  # Import of python modules.
import sys
import pygame
from game import Game

os.environ['SDL_VIDEO_WINDOW_POS'] = "150,150"
pygame.init()  # Generate the game window.
pygame.display.set_caption("Shooter")  # Window title.
game_window = pygame.display.set_mode((1400, 800))  # Window size.
background = pygame.image.load('assets/background.jpg')  # Window logo.
if sys.platform == 'win32':
    pygame.display.set_icon(pygame.image.load("assets/logo.png"))  # Logo application if windows operating system.

game = Game(game_window)  # Creates an instance of the game class.
games_running = True  # Enables you to enter the game loop.

# Game loop.
while games_running:
    game_window.blit(background, (0, -130))  # Apply the background image on the game window.
    game_window.blit(game.player.image, game.player.rect)  # Apply player image.
    game.player.update_health_bar(game_window)  # Displays the life bar of the player.
    game.player.update_armor_bar(game_window)  # Displays the armor bar of the player.

    # Collect the projectiles.
    for projectile in game.player.all_projectiles:
        projectile.move_bullets()  # Moves projectiles on the window.

    # Collect the monsters.
    for monster in game.all_monsters:
        monster.forward()  # Move group of monsters.
        monster.update_health_bar(game_window)  # Displays the life bar of the monsters.

    game.player.all_projectiles.draw(game_window)  # Apply player's projectile.

    game.all_monsters.draw(game_window)  # Apply monsters group.

    # If the key pressed is equal to the right and the position smaller than the window size.
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < game_window.get_width():
        game.player.move_right()  # Moves the player to the right.
    # If the key pressed is equal to the left and the position greater than 0 pixels.
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()  # Moves the player to the left.

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
