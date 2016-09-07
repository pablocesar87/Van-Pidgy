import random, pygame, sys, time
from pygame import image
from pygame.sprite import Sprite
from os import path

img_dir = path.join(path.dirname(__file__), 'class_images')

class Vampire(pygame.sprite.Sprite):
    #this class represents the vampires
    def __init__(self,vampire_direction):
        pygame.sprite.Sprite.__init__(self)
        self.vampire_direction=vampire_direction
        self.points=50
        self.image=pygame.image.load(path.join(img_dir, "vampire.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
    def get_points(self):
        return self.points
        
class Vampire_gun(pygame.sprite.Sprite):
    #this class represents the vampires
    def __init__(self,vampire_direction):
        pygame.sprite.Sprite.__init__(self)
        self.vampire_direction=vampire_direction
        self.points=150
        self.shoting_number=random.randint(1,100)
        self.image=pygame.image.load(path.join(img_dir, "vampire_gun.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
    def get_points(self):
        return self.points
    def get_shoting_number(self):
        return self.shoting_number

class Vampire_boss(pygame.sprite.Sprite):
    #this class is the final boss
    def __init__(self, vampire_direction):
        pygame.sprite.Sprite.__init__(self)
        self.vampire_direction = vampire_direction
        self.image = pygame.image.load(path.join(img_dir, "tentacula.png")).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.shoting_number = random.randint(1, 60)
        self.life=10
    def get_shoting_number(self):
        return self.shoting_number
    def shooted(self):
        self.life -=1
    def get_life(self):
        return self.life
        
class Soul(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path.join(img_dir, "soul.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 1.5
        
class Soul_gun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path.join(img_dir, "soul_gun.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 1.5
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path.join(img_dir, "bullet.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 3

class Bullet_boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(img_dir, "energy_ball.png")).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 3
        
class Pidgeon(pygame.sprite.Sprite): 
    #this is the protagonist class
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path.join(img_dir, "pidgeon.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
    def electrocute(self):
        self.image=pygame.image.load(path.join(img_dir, "electrocuted_pidgeon.png")).convert() 
        self.image.set_colorkey((255,255,255)) 
    def bumpLeft(self):
        self.image=pygame.image.load(path.join(img_dir, "pidgeon_bump_left.png")).convert() 
        self.image.set_colorkey((255,255,255))
    def bumpRight(self): 
        self.image=pygame.image.load(path.join(img_dir, "pidgeon_bump_right.png")).convert() 
        self.image.set_colorkey((255,255,255))
    def bumpHead(self):
        self.image=pygame.image.load(path.join(img_dir, "pidgeon_bump_head.png")).convert() 
        self.image.set_colorkey((255,255,255))
class Shit(pygame.sprite.Sprite):
    #Shits are the ammo coming from the pidgeon class
    def __init__(self, wind_effect):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path.join(img_dir, "shit.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.wind_effect=wind_effect
    def update(self):
        #this makes the shit to goes down
        #and left if the case requires it
        self.rect.y += 3
        self.rect.x = self.rect.x + self.wind_effect
        
class Wind(pygame.sprite.Sprite):
     def __init__(self, wind_direction):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path.join(img_dir, "wind_left.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.wind_direction=wind_direction
     def update(self):
        #this makes the wind goes left, also it is the wind velocity
        self.rect.x = self.rect.x + self.wind_direction
     def change_direction(self):
        self.image=pygame.image.load(path.join(img_dir, "wind_right.png")).convert()
        self.image.set_colorkey((255,255,255))

class UFO(pygame.sprite.Sprite):
    def __init__(self, ufo_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path.join(img_dir, "UFO_left.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.ufo_speed=ufo_speed
    def update(self):
        #this makes the ufo goes left
        self.rect.x = self.rect.x + self.ufo_speed
    def change_direction(self):
        self.image=pygame.image.load(path.join(img_dir, "UFO_right.png")).convert()
        self.image.set_colorkey((255,255,255))
        
class Drone(pygame.sprite.Sprite):
    def __init__(self, drone_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path.join(img_dir, "drone_left.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.drone_speed=drone_speed
    def update(self):
        #this makes the ufo goes left
        self.rect.x = self.rect.x + self.drone_speed
    def change_direction(self):
        self.image=pygame.image.load(path.join(img_dir, "drone_right.png")).convert()
        self.image.set_colorkey((255,255,255))
    
    
    
    
    
    
    