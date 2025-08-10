import pygame
import math
from celestial_object import CelestialObject

class Satelite(CelestialObject):
    def __init__(self, image_path, mass, distance, orbit_speed, planet,nucleo_status):
        super().__init__(image_path=image_path, mass=mass, distance=distance, orbit_speed=orbit_speed)
        self.nucleo_status = nucleo_status
        self.planet = planet  #para tener la rerencia del planeta a que va orbitar
        self.angle = 0

    def update(self):
        self.angle += self.orbit_speed
        if self.angle >= 360:
            self.angle -= 360  #se reinicia para matener el angulo

        x = self.planet.rect.centerx + self.distance * math.cos(math.radians(self.angle))
        y = self.planet.rect.centery + self.distance * math.sin(math.radians(self.angle))
        
        self.rect.centerx = x
        self.rect.centery = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def generate_magnetic_field(self,screen):
        pass
