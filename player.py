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
        self.shield = 50  # Player's shield point.
        self.max_shield = 50
        self.attack = 10  # Player's attack point.
        self.speed = 2  # Player's movement speed.
        self.boost_speed = 3  # Player's movement speed bonus.
        self.all_projectiles = pygame.sprite.Group()  # Create a group of projectiles.
        self.image = pygame.image.load('assets/player.png')  # Player's picture.
        self.rect = self.image.get_rect()  # Player's position.
        self.rect.x = self.window.get_width() / 2 - self.rect.width / 2  # Player's starting position.
        self.rect.y = 580

    # Creates an instance of the Projectile class.
    def launch_bullets(self):
        self.all_projectiles.add(Bullets(self, self.window))  # Save the projectile created in the projectile group.

    def damage(self, amount):
        # If the player has a shield they inflict damage.
        if self.shield > 0:
            self.shield -= amount  # We subtract the damage to shield points.
        else:  # Damage is inflicted on hit points.
            # Check that the player has enough life to take the damage.
            if self.health - amount > amount:
                self.health -= amount  # We subtract the damage to hit points.
            else:  # Game over.
                self.game.game_over()

    # Update the life bar.
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (57, 57, 57), [self.rect.x + 52, self.rect.y + 20, self.max_health, 6])  # Applies the maximum life bar.
        pygame.draw.rect(surface, (0, 255, 0), [self.rect.x + 52, self.rect.y + 20, self.health, 6])  # Applies the life bar.

    def update_shield_bar(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), [self.rect.x + 52, self.rect.y + 20, self.shield, 6])  # Applies the shield bar.

    # Moves the player to the right.
    def move_right(self):
        # If the player is not in contact with a monster or a boss.
        if not self.game.check_collision(self, (self.game.all_monsters or self.game.all_boss)):
            self.rect.x += self.speed   # Increment the position of the player by its speed of movement.

    # Moves the player to the left.
    def move_left(self, speed):
        self.rect.x -= speed   # Decreases the position of the player by its speed of movement.
