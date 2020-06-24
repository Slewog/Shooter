import pygame  # Import of python modules.
from player import Survivor  # Import of annex python files.
from monster import Mummy


class Game:
    def __init__(self, window):
        self.window = window  # Game window.
        self.all_players = pygame.sprite.Group()  # Create a group of players.
        self.player = Survivor(self, self.window)  # Creates an instance of the survivor class.
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()  # Create a group of monsters.
        self.pressed = {}  # Dictionary for activated keys.
        self.spawn_monster()  # Creates an instance of the mummy class.

    # Check the collision between 2 sprites.
    def check_collision(self, sprite, sprite_group):
        return pygame.sprite.spritecollide(sprite, sprite_group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        self.all_monsters.add(Mummy(self, self.window))  # Save the monster created in the monsters group.
