import random
import pygame
from os import path

# Directory for images
IMG_DIR = path.join(path.dirname(__file__), "class_images")


class Vampire(pygame.sprite.Sprite):
    """This class represents the vampires."""

    def __init__(self, vampire_direction: str) -> None:
        super().__init__()
        self.vampire_direction = vampire_direction
        self.points = 50
        self.image = pygame.image.load(path.join(IMG_DIR, "vampire.png")).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def get_points(self) -> int:
        return self.points


class VampireGun(pygame.sprite.Sprite):
    """This class represents vampires with guns."""

    def __init__(self, vampire_direction: str) -> None:
        super().__init__()
        self.vampire_direction = vampire_direction
        self.points = 150
        self.shooting_number = random.randint(1, 100)
        self.image = pygame.image.load(path.join(IMG_DIR, "vampire_gun.png")).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def get_points(self) -> int:
        return self.points

    def get_shooting_number(self) -> int:
        return self.shooting_number


class VampireBoss(pygame.sprite.Sprite):
    """This class represents the final boss."""

    def __init__(self, vampire_direction: str) -> None:
        super().__init__()
        self.vampire_direction = vampire_direction
        self.image = pygame.image.load(path.join(IMG_DIR, "tentacula.png")).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.shooting_number = random.randint(1, 60)
        self.life = 10

    def get_shooting_number(self) -> int:
        return self.shooting_number

    def shooted(self) -> None:
        self.life -= 1

    def get_life(self) -> int:
        return self.life


class Soul(pygame.sprite.Sprite):
    """This class represents a soul."""

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(path.join(IMG_DIR, "soul.png")).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self) -> None:
        self.rect.y -= 1.5


class SoulGun(pygame.sprite.Sprite):
    """This class represents a soul with a gun."""

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(path.join(IMG_DIR, "soul_gun.png")).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self) -> None:
        self.rect.y -= 1.5


class Bullet(pygame.sprite.Sprite):
    """This class represents a bullet."""

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(path.join(IMG_DIR, "bullet.png")).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self) -> None:
        self.rect.y -= 3


class BulletBoss(pygame.sprite.Sprite):
    """This class represents a boss's bullet."""

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(path.join(IMG_DIR, "energy_ball.png")).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self) -> None:
        self.rect.y -= 3


class Pidgeon(pygame.sprite.Sprite):
    """This is the protagonist class."""

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(path.join(IMG_DIR, "pidgeon.png")).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def electrocute(self) -> None:
        self.image = pygame.image.load(path.join(IMG_DIR, "electrocuted_pidgeon.png")).convert()
        self.image.set_colorkey((255, 255, 255))

    def bump_left(self) -> None:
        self.image = pygame.image.load(path.join(IMG_DIR, "pidgeon_bump_left.png")).convert()
        self.image.set_colorkey((255, 255, 255))

    def bump_right(self) -> None:
        self.image = pygame.image.load(path.join(IMG_DIR, "pidgeon_bump_right.png")).convert()
        self.image.set_colorkey((255, 255, 255))

    def bump_head(self) -> None:
        self.image = pygame.image.load(path.join(IMG_DIR, "pidgeon_bump_head.png")).convert()
        self.image.set_colorkey((255, 255, 255))


class Shit(pygame.sprite.Sprite):
    """Shits are the ammo coming from the Pidgeon class."""

    def __init__(self, wind_effect: int) -> None:
        super().__init__()
        img_dir = path.join(path.dirname(__file__), "class_images")
        self.image = pygame.image.load(path.join(img_dir, "shit.png")).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.wind_effect = wind_effect

    def update(self) -> None:
        """Update the position of the shit."""
        self.rect.y += 3
        self.rect.x += self.wind_effect


class Wind(pygame.sprite.Sprite):
    """This class represents the wind."""

    def __init__(self, wind_direction: int) -> None:
        super().__init__()
        img_dir = path.join(path.dirname(__file__), "class_images")
        self.image = pygame.image.load(path.join(img_dir, "wind_left.png")).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.wind_direction = wind_direction

    def update(self) -> None:
        """Update the wind's position."""
        self.rect.x += self.wind_direction

    def change_direction(self) -> None:
        """Change the wind's direction."""
        img_dir = path.join(path.dirname(__file__), "class_images")
        self.image = pygame.image.load(path.join(img_dir, "wind_right.png")).convert()
        self.image.set_colorkey((255, 255, 255))


class UFO(pygame.sprite.Sprite):
    """This class represents a UFO."""

    def __init__(self, ufo_speed: int) -> None:
        super().__init__()
        img_dir = path.join(path.dirname(__file__), "class_images")
        self.image = pygame.image.load(path.join(img_dir, "UFO_left.png")).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.ufo_speed = ufo_speed

    def update(self) -> None:
        """Update the UFO's position."""
        self.rect.x += self.ufo_speed

    def change_direction(self) -> None:
        """Change the UFO's direction."""
        img_dir = path.join(path.dirname(__file__), "class_images")
        self.image = pygame.image.load(path.join(img_dir, "UFO_right.png")).convert()
        self.image.set_colorkey((255, 255, 255))


class Drone(pygame.sprite.Sprite):
    """This class represents a Drone."""

    def __init__(self, drone_speed: int) -> None:
        super().__init__()
        img_dir = path.join(path.dirname(__file__), "class_images")
        self.image = pygame.image.load(path.join(img_dir, "drone_left.png")).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.drone_speed = drone_speed

    def update(self) -> None:
        """Update the Drone's position."""
        self.rect.x += self.drone_speed

    def change_direction(self) -> None:
        """Change the Drone's direction."""
        img_dir = path.join(path.dirname(__file__), "class_images")
        self.image = pygame.image.load(path.join(img_dir, "drone_right.png")).convert()
        self.image.set_colorkey((255, 255, 255))
