import pygame
import math
from celestial_object import CelestialObject

class Planet(CelestialObject):
    def __init__(self,image_path, distance, orbit_speed, mass, nucleo_status):
        super().__init__(image_path=image_path, distance=distance, orbit_speed=orbit_speed, mass=mass)
        self.nucleo_status = nucleo_status
        self.satellite_angle = 0
        self.satellite_speed = 0.08

    
    def generate_magnetic_field(self,screen):
        if self.nucleo_status == "Activate" and self.mass >= 2000:

            whidth = self.rect.width + 15 
            height = self.rect.height + 15 

            blue_field = pygame.image.load("../images/campo_azul.png")
            blue_field_resized = pygame.transform.scale(blue_field,(whidth,height))
            blue_field_resized_rect = blue_field_resized.get_rect()

            blue_field_resized_rect.centerx = self.rect.centerx
            blue_field_resized_rect.centery = self.rect.centery
            
            screen.blit(blue_field_resized, blue_field_resized_rect)

    
    def generate_satelite(self,screen):
        whidth = self.rect.width / 4
        height = self.rect.height / 4

        blue_field = pygame.image.load("../images/luna.gif")
        blue_field_resized = pygame.transform.scale(blue_field,(whidth,height))
        blue_field_resized_rect = blue_field_resized.get_rect()

        blue_field_resized_rect.centerx = self.rect.centerx - 30 * math.cos(self.satellite_angle)
        blue_field_resized_rect.centery = self.rect.centery - 30 * math.sin(self.satellite_angle)

        self.satellite_angle += self.satellite_speed

        screen.blit(blue_field_resized, blue_field_resized_rect)
