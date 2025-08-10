import pygame
import math
from abc import ABC,abstractmethod

class CelestialObject(ABC):

    def __init__(self,image_path, mass ,distance=0, orbit_speed =0):
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.angle = 0
        self.distance = distance
        self._orbit_speed = 0
        self._mass = 0

        self.orbit_speed = orbit_speed
        self.mass = mass


    @property
    def orbit_speed(self):
        return self._orbit_speed  
    
    @orbit_speed.setter
    def orbit_speed(self, orbit_speed):

        if orbit_speed >= 0 and orbit_speed <= 10:
            self._orbit_speed = orbit_speed

        else:
            raise ValueError("Error en la orvita")
    

    @property
    def mass(self):
        return self._mass
    
    @mass.setter
    def mass(self,mass):
        if mass >= 1 and mass <= 10000:
            self._mass = mass
        else:
            raise ValueError("Error en la masa")

    
    
    def update(self):
        self.angle += self.orbit_speed


    def draw(self, screen):
        x = (screen.get_width() // 2) + (self.distance * math.cos(math.radians(self.angle)))
        y = (screen.get_height() // 2) + (self.distance * math.sin(math.radians(self.angle)))
        #print(f"Object {self.image_patn}, coor x: {x}, coor y: {y}")
        self.rect.centerx = x
        self.rect.centery = y
        screen.blit(self.image, self.rect)


    @abstractmethod
    def generate_magnetic_field(self,scree):
        pass