from planet import Planet
from strar import Star
from asteroid import Asteroid
from satelite import Satelite
import pygame
import os
print("Directorio actual:", os.getcwd())


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

#screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("Sistema Solar")

sun = Star(image_path="../images/sun.png",mass=1200,nucleo_status="Activate")


mercury = Planet(image_path="../images/mercury.png", distance = 140, orbit_speed = 4.15,
                 mass = 200, nucleo_status="Inactive")

venus = Planet(image_path="../images/venus.png", distance = 180, orbit_speed = 3.13,
               mass = 200, nucleo_status="Inactive")

earth = Planet(image_path="../images/earth.gif", distance = 230, orbit_speed = 2.57, 
               mass=3500, nucleo_status="Activate")

moon = Satelite(image_path="../images/luna.gif", mass=100, distance=30, orbit_speed=6, planet=earth, 
                nucleo_status="Activate")

mars = Planet(image_path="../images/marte.png", distance = 280, orbit_speed = 2.06,
              mass=3000, nucleo_status="Activate")

jupiter = Planet(image_path="../images/jupiter.gif", distance = 330, orbit_speed = 1.43, 
                mass=3500, nucleo_status="Activate")

saturno = Planet(image_path="../images/saturno.png", distance = 380, orbit_speed = 1.19,
                mass=3500, nucleo_status="Activate")

uranus = Planet(image_path="../images/uranus.gif", distance = 430, orbit_speed = 0.84,
                mass=3000, nucleo_status="Activate")

neptune = Planet(image_path="../images/neptuno.png", distance = 480, orbit_speed = 0.66,
                 mass=3500, nucleo_status="Activate")

pluto = Planet(image_path="../images/pluton.gif", distance = 530, orbit_speed=0.53,
               mass = 200, nucleo_status="Inactive")

asteroid = Asteroid(image_path="../images/asteroide_llamas.png", distance = 570, orbit_speed=0.45, mass = 200)

sun.image = pygame.transform.scale(sun.image,(50,50))
sun.rect = sun.image.get_rect()

mercury.image = pygame.transform.scale(mercury.image,(7,7))
mercury.rect = mercury.image.get_rect()

venus.image = pygame.transform.scale(venus.image,(15,15))
venus.rect = venus.image.get_rect()

earth.image = pygame.transform.scale(earth.image,(18,18))
earth.rect = earth.image.get_rect()
moon.image = pygame.transform.scale(moon.image,(7,7))
moon.rect = moon.image.get_rect()

mars.image = pygame.transform.scale(mars.image,(10,10))
mars.rect = mars.image.get_rect()

jupiter.image = pygame.transform.scale(jupiter.image,(30,30))
jupiter.rect = jupiter.image.get_rect()

saturno.image = pygame.transform.scale(saturno.image,(25,25))
saturno.rect = saturno.image.get_rect()

uranus.image = pygame.transform.scale(uranus.image,(22,22))
uranus.rect = uranus.image.get_rect()

neptune.image = pygame.transform.scale(neptune.image,(18,18))
neptune.rect = neptune.image.get_rect()

pluto.image = pygame.transform.scale(pluto.image,(8,8))
pluto.rect = pluto.image.get_rect()

asteroid.image = pygame.transform.scale(asteroid.image,(50,50))
asteroid.rect = asteroid.image.get_rect()

backcroud_image = pygame.image.load("../images/fondo.png").convert()
backcroud_image = pygame.transform.scale(backcroud_image, (800, 600))

backgroud_rect = backcroud_image.get_rect()


clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(backcroud_image, backgroud_rect)

    sun.update()
    sun.draw(screen)
    sun.generate_magnetic_field(screen)

    mercury.update()
    mercury.draw(screen)
    mercury.generate_magnetic_field(screen)

    venus.update()
    venus.draw(screen)

    earth.update()
    earth.draw(screen)
    earth.generate_magnetic_field(screen)

    moon.update()
    moon.draw(screen)

    mars.update()
    mars.draw(screen)
    mars.generate_magnetic_field(screen)

    jupiter.update()
    jupiter.draw(screen)
    jupiter.generate_magnetic_field(screen)

    saturno.update()
    saturno.draw(screen)
    saturno.generate_magnetic_field(screen)

    uranus.update()
    uranus.draw(screen)
    uranus.generate_magnetic_field(screen)

    neptune.update()
    neptune.draw(screen)
    neptune.generate_magnetic_field(screen)

    pluto.update()
    pluto.draw(screen)

    asteroid.update()
    asteroid.draw(screen)
    

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
