import pygame,sys
from library.Setting import *

pygame.init()

# set screen
screen = pygame.display.set_mode((1280, 700))

# set title
pygame.display.set_caption('Mario clone')
test_surface = pygame.Surface((100, 200))
test_surface.fill("Red")

# clock obj for framerate
clock = pygame.time.Clock()


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  screen.blit(test_surface, (200, 100))

  pygame.display.update()
  clock.tick(40)