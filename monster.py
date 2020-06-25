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
        self.attack = 0.5   # Mummy's attack point.
        self.max_monsters_killed = 50  # Set the maximum number of monsters defeated to unlocking the boss.
        self.speed = randint(1, 2)  # Mummy's movement speed.
        self.image = pygame.image.load('assets/mummy.png')  # Mummy's picture.
        self.rect = self.image.get_rect()  # Mummy's position.
        self.rect.x = self.window.get_width() - self.rect.width + randint(0, 135)  # Mummy's starting position.
        self.rect.y = randint(610, 635)

    # Applies the damage.
    def damage(self, amount):
        self.health -= amount
        # If the life of the monster is equal to or less than 0, we make it reappear.
        if self.health <= 0:
            self.game.all_monsters.remove(self)  # The defeated monster is removed from the group of monsters.
            self.game.spawn_monster()  # Creation of a new monster.
            self.game.dead_monsters += 1  # The defeated monster counter is incremented by 1.
            # If there are enough defeated monsters.
            if self.game.dead_monsters == self.max_monsters_killed:
                self.game.spawn_boss()  # Creates an instance of the Boss class.

    # Update the life bar.
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (57, 57, 57), [self.rect.x + 13, self.rect.y - 10, self.max_health, 5])  # Applies the maximum life bar.
        pygame.draw.rect(surface, (255, 0, 0), [self.rect.x + 13, self.rect.y - 10, self.health, 5])  # Applies the life bar.

    # Moves the mummy to the left.
    def forward(self):
        # If the mummy is not in contact with a player.
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.speed
        else:  # Applies damage to the player.
            self.game.player.damage(self.attack)


# Class of "Boss" type enemies.
class Boss(pygame.sprite.Sprite):
    def __init__(self, game, window):
        super().__init__()
        self.game = game  # Game class instance.
        self.window = window  # Game window.
        self.health = 100   # Boss life point.
        self.max_health = 100
        self.shield = 100  # Boss shield point.
        self.max_shield = 100
        self.attack = 1.0   # Boss attack point.
        self.speed = 2  # Boss movement speed.
        self.image = pygame.image.load('assets/alien.png')  # Boss picture.
        self.image = pygame.transform.scale(self.image, (200, 200))  # Set the size of the projectile.
        self.rect = self.image.get_rect()  # Boss position.
        self.rect.x = self.window.get_width() - self.rect.width + randint(0, 135)  # Boss starting position.
        self.rect.y = 560

    # Applies the damage.
    def damage(self, amount):
        if self.shield > 0:
            self.shield -= amount  # We subtract the damage to shield points.
        else:
            # If the life of the boss is equal to or less than 0, we make it reappear.
            if self.health - amount > amount:
                self.health -= amount  # We subtract the damage to hit points.
            else:  # Game over.
                self.game.game_win()

    # Update the life bar.
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (57, 57, 57), [self.rect.x + 52, self.rect.y, self.max_health, 5])  # Applies the maximum life bar.
        pygame.draw.rect(surface, (255, 0, 0), [self.rect.x + 52, self.rect.y, self.health, 5])  # Applies the life bar.

    # Update the shield bar.
    def update_shield_bar(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), [self.rect.x + 52, self.rect.y, self.shield, 5])  # Applies the shield bar.

    # Moves the boss to the left.
    def forward(self):
        # If the boss is not in contact with a player.
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.speed
        else:  # Applies damage to the player.
            self.game.player.damage(self.attack)
