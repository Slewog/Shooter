import pygame  # Import of python modules.
from projectile import Bullets  # Import of annex python files.


# Player class.
class Survivor(pygame.sprite.Sprite):
    def __init__(self, game, window):
        super().__init__()
        self.game = game  # Game class instance.
        self.window = window  # Game window.
        self.health = 100  # Player's life point.
        self.max_health = 100
        self.armor = 50  # Player's armor point.
        self.max_armor = 50
        self.attack = 10  # Player's attack point.
        self.speed = 2  # Player's movement speed.
        self.all_projectiles = pygame.sprite.Group()  # Create a group of projectiles.
        self.image = pygame.image.load('assets/player.png')  # Player's picture.
        self.rect = self.image.get_rect()  # Player's position.
        self.rect.x = self.window.get_width() / 2 - self.rect.width / 2  # Player's starting position.
        self.rect.y = 580

    # Creates an instance of the Projectile class.
    def launch_bullets(self):
        self.all_projectiles.add(Bullets(self, self.window))  # Save the projectile created in the projectile group.

    def damage(self, amount):
        if self.armor > 0:
            self.armor -= amount
        else:
            if self.health - amount > amount:
                self.health -= amount
            else:
                self.game.game_over()

    # Update the life bar.
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (57, 57, 57), [self.rect.x + 52, self.rect.y + 20, self.max_health, 6])  # Applies the maximum life bar.
        pygame.draw.rect(surface, (0, 255, 0), [self.rect.x + 52, self.rect.y + 20, self.health, 6])  # Applies the life bar.

    def update_armor_bar(self, surface):
        pygame.draw.rect(surface, (57, 57, 57), [self.rect.x + 52, self.rect.y + 11, self.max_armor, 6])  # Applies the maximum armor bar.
        pygame.draw.rect(surface, (0, 0, 255), [self.rect.x + 52, self.rect.y + 11, self.armor, 6])  # Applies the armor bar.

    # Moves the player to the right.
    def move_right(self):
        # If the player is not in contact with a monster.
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.speed

    # Moves the player to the left.
    def move_left(self):
        self.rect.x -= self.speed
