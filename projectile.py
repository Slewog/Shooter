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
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.origin_image = self.image
        self.rect = self.image.get_rect()  # Projectile's position.
        self.rect.x = player.rect.x + player.rect.width / 1.5  # Projectile's starting position.
        self.rect.y = player.rect.y + player.rect.height / 2

    # Rotate the projectile while it is moving.
    def rotate_bullets(self):
        self.angle -= 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)  # Moves the rotation point to the center of the image.

    # Deletes the projectile if it leaves the screen.
    def remove_bullets(self):
        self.player.all_projectiles.remove(self)

    # Moves the projectile to the right.
    def move_bullets(self):
        self.rect.x += self.speed
        self.rotate_bullets()
        # Check if the projectile comes into contact with a monster.
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove_bullets()
            monster.damage(self.player.attack)

        # If the position smaller than the window size.
        if self.rect.x + self.rect.width > self.window.get_width():
            self.remove_bullets()
