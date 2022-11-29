import pygame,sys
from library.Setting import *

pygame.init()

# set screen
screen = pygame.display.set_mode((lebar, tinggi))

# set title
pygame.display.set_caption('Mario clone')

# set surfaces
sky_surface = pygame.image.load("asset/Sky.png")

ground_surface = pygame.image.load("asset/Ground.png")

test_font = pygame.font.Font(None, 50)
text_surface = test_font.render("tes", False, 'White')

# clock obj for framerate
clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  screen.blit(sky_surface, (0, 0))
  screen.blit(ground_surface, (0, 450))

  pygame.display.update()
  clock.tick(40)