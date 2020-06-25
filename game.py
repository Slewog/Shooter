import pygame  # Import of python modules.
from player import Survivor  # Import of annex python files.
from monster import Mummy


class Game:
    def __init__(self, window):
        self.window = window  # Game window.
        self.is_playing = False
        self.all_players = pygame.sprite.Group()  # Create a group of players.
        self.player = Survivor(self, self.window)  # Creates an instance of the survivor class.
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()  # Create a group of monsters.
        self.pressed = {}  # Dictionary for activated keys.

    def start_game(self):
        self.is_playing = True
        self.player.rect.x = self.window.get_width() / 2 - self.player.rect.width / 2  # Player's starting position.
        self.player.rect.y = 580
        self.spawn_monster()  # Creates an instance of the mummy class.
        self.spawn_monster()

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    # Update window.
    def update_game(self):
        self.window.blit(self.player.image, self.player.rect)  # Apply player image.
        self.player.update_health_bar(self.window)  # Displays the life bar of the player.
        self.player.update_armor_bar(self.window)  # Displays the armor bar of the player.

        # Collect the projectiles.
        for projectile in self.player.all_projectiles:
            projectile.move_bullets()  # Moves projectiles on the window.

        # Collect the monsters.
        for monster in self.all_monsters:
            monster.forward()  # Move group of monsters.
            monster.update_health_bar(self.window)  # Displays the life bar of the monsters.

        self.player.all_projectiles.draw(self.window)  # Apply player's projectile.
        self.all_monsters.draw(self.window)  # Apply monsters group.

        # If the key pressed is equal to the right and the position smaller than the window size.
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < self.window.get_width():
            self.player.move_right()  # Moves the player to the right.
        # If the key pressed is equal to the left and the position greater than 0 pixels.
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()  # Moves the player to the left.

    # Check the collision between 2 sprites.
    def check_collision(self, sprite, sprite_group):
        return pygame.sprite.spritecollide(sprite, sprite_group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        self.all_monsters.add(Mummy(self, self.window))  # Save the monster created in the monsters group.
