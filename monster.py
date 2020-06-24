import pygame  # Import of python modules.
from random import randint


# Class of "Mommies" type enemies.
class Mummy(pygame.sprite.Sprite):
    def __init__(self, game, window):
        super().__init__()
        self.game = game  # Game class instance.
        self.window = window  # Game window.
        self.health = 100   # Mummy's life point.
        self.max_health = 100
        self.attack = 5   # Mummy's attack point.
        self.speed = 1  # Mummy's movement speed.
        self.image = pygame.image.load('assets/mummy.png')  # Mummy's picture.
        self.rect = self.image.get_rect()  # Mummy's position.
        self.rect.x = self.window.get_width() - self.rect.width / 3.5  # Mummy's starting position.
        self.rect.y = 530

    # Applies the damage.
    def damage(self, amount):
        self.health -= amount
        # If the life of the monster is equal to or less than 0, we make it reappear.
        if self.health <= 0:
            self.rect.x = self.window.get_width() - self.rect.width / 3.5
            self.health = self.max_health

    # Update the life bar.
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (57, 57, 57), [self.rect.x + 13, self.rect.y - 10, self.max_health, 5])  # Applies the maximum life bar.
        pygame.draw.rect(surface, (255, 0, 0), [self.rect.x + 13, self.rect.y - 10, self.health, 5])  # Applies the life bar.

    # Moves the mummy to the left.
    def forward(self):
        # If the mummy is not in contact with a player.
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.speed
