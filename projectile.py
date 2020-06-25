import pygame  # Import of python modules.


# Player's projectile class.
class Bullets(pygame.sprite.Sprite):
    def __init__(self, player, window):
        super().__init__()
        self.player = player  # Survivor class instance.
        self.window = window  # Game window.
        self.speed = 3  # Projectile's movement speed.
        self.angle = 0  # Projectile's angle.
        self.image = pygame.image.load('assets/projectile.png')  # Projectile's picture.
        self.image = pygame.transform.scale(self.image, (35, 35))  # Set the size of the projectile.
        self.origin_image = self.image
        self.rect = self.image.get_rect()  # Projectile's position.
        self.rect.x = player.rect.x + player.rect.width / 1.5  # Projectile's starting position.
        self.rect.y = player.rect.y + player.rect.height / 2

    # Rotate the projectile while it is moving.
    def rotate_bullets(self):
        self.angle -= 5  # Add 5 degrees to the rotation angle.
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)  # Apply rotation.
        self.rect = self.image.get_rect(center=self.rect.center)  # Moves the rotation point to the center of the image.

    # Deletes the projectile if it leaves the screen.
    def remove_bullets(self):
        self.player.all_projectiles.remove(self)  # Removes the projectile from the projectile group.

    # Moves the projectile to the right.
    def move_bullets(self):
        self.rect.x += self.speed  # Increment the position of the projectile by its speed of movement.
        self.rotate_bullets()  # Apply projectile rotation.
        # Check if the projectile comes into contact with a monster or a boss.
        for monster in self.player.game.check_collision(self, (self.player.game.all_monsters or self.player.game.all_boss)):
            self.remove_bullets()  # Delete the projectile.
            monster.damage(self.player.attack)  # Applies projectile damage.
        # If the position smaller than the window size.
        if self.rect.x + self.rect.width > self.window.get_width():
            self.remove_bullets()  # Delete the projectile.
