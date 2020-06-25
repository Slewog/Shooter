import pygame  # Import of python modules.
from player import Survivor  # Import of annex python files.
from monster import Mummy
from monster import Boss


class Game:
    def __init__(self, window):
        self.window = window  # Game window.
        self.is_playing = False  # Allows you know the state of the game.
        self.dead_monsters = 0  # Numbers of monsters to kill.
        self.all_players = pygame.sprite.Group()  # Create a group of players.
        self.player = Survivor(self, self.window)  # Creates an instance of the survivor class.
        self.all_players.add(self.player)  # Add player to player group.
        self.all_monsters = pygame.sprite.Group()  # Create a group of monsters.
        self.all_boss = pygame.sprite.Group()  # Create a group of boss.
        self.pressed = {}  # Dictionary for activated keys.

    # Start the game.
    def start_game(self):
        self.is_playing = True  # Lets start the game.
        self.player.rect.x = self.window.get_width() / 2 - self.player.rect.width / 2  # Player's starting position.
        self.player.rect.y = 580
        self.player.all_projectiles = pygame.sprite.Group()  # Reset group of projectile.
        self.spawn_monster()  # Create a first instance of the mummy class.
        self.spawn_monster()  # Create a second instance of the mummy class.

    # Reset the game and display the welcome screen.
    def game_win(self):
        self.all_boss = pygame.sprite.Group()  # Reset group of boss
        self.player.health = self.player.max_health  # Reset player's life.
        self.player.shield = self.player.max_shield  # Reset player's shield.
        self.is_playing = False  # Returns to the home screen.
        print("GAME WIN !!!\n" + "You have killed " + str(self.dead_monsters) + " monsters in addition to the boss\n" + "Congrulatations !!!")
        self.dead_monsters = 0  # Resets the monster counter to 0.

    # Reset the game and display the welcome screen.
    def game_over(self):
        self.all_monsters = pygame.sprite.Group()  # Reset group of monsters.
        self.all_boss = pygame.sprite.Group()
        self.player.health = self.player.max_health  # Reset player's life.
        self.player.shield = self.player.max_shield  # Reset player's shield.
        self.is_playing = False  # Returns to the home screen.
        print("GAME OVER !!!\n" + "You have killed " + str(self.dead_monsters) + " monsters !!!")
        self.dead_monsters = 0  # Resets the monster counter to 0.

    # Displays the elements of the game.
    def update_game(self):
        self.window.blit(self.player.image, self.player.rect)  # Apply player image.
        self.player.update_health_bar(self.window)  # Displays the life bar of the player.
        self.player.update_shield_bar(self.window)  # Displays the shield bar of the player.

        # Collect the projectiles.
        for projectile in self.player.all_projectiles:
            projectile.move_bullets()  # Moves projectiles on the window.

        # Collect the monsters.
        for monster in self.all_monsters:
            monster.forward()  # Move group of monsters.
            monster.update_health_bar(self.window)  # Displays the life bar of the monsters.

        # Collect the monsters.
        for boss in self.all_boss:
            boss.forward()  # Move group of boss.
            boss.update_health_bar(self.window)  # Displays the life bar of the boss.
            boss.update_shield_bar(self.window)  # Displays the shield bar of the boss.

        self.player.all_projectiles.draw(self.window)  # Apply player's projectile.
        self.all_monsters.draw(self.window)  # Apply monsters group.
        self.all_boss.draw(self.window)  # Apply boss group.

        # If the key pressed is equal to the right and the position smaller than the window size.
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < self.window.get_width():
            self.player.move_right()  # Moves the player to the right.
        # If the keys pressed are LSHIFT and A.
        elif self.pressed.get(pygame.K_LSHIFT) and self.pressed.get(pygame.K_a):
            self.player.move_left(self.player.boost_speed)  # Moves the player to the left with the speed bonus.
        # If the key pressed is equal to the left and the position greater than 0 pixels.
        elif self.pressed.get(pygame.K_a) and self.player.rect.x > 0:
            self.player.move_left(self.player.speed)  # Moves the player to the left.

    # Check the collision between 2 sprites.
    def check_collision(self, sprite, sprite_group):
        return pygame.sprite.spritecollide(sprite, sprite_group, False, pygame.sprite.collide_mask)

    # Create a monster.
    def spawn_monster(self):
        self.all_monsters.add(Mummy(self, self.window))  # Save the monster created in the monsters group.

    # Create a boss.
    def spawn_boss(self):
        self.all_monsters = pygame.sprite.Group()  # Reset group of monsters.
        self.player.all_projectiles = pygame.sprite.Group()  # Reset group of projectile.
        self.player.rect.x = self.window.get_width() / 2 - self.player.rect.width / 2  # Player's starting position.
        self.player.rect.y = 580
        self.all_boss.add(Boss(self, self.window))  # Save the monster created in the monsters group.
