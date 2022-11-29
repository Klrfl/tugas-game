import pygame,sys
from library.Setting import *

pygame.init()

# set screen
screen = pygame.display.set_mode((1280, 700))

# set title
pygame.display.set_caption('Mario clone')

# set surfaces
test_surface = pygame.Surface((100, 200))
test_surface.fill("Red")

test_font = pygame.font.Font(None, 50)
text_surface = test_font.render("tes", False, 'White')

# clock obj for framerate
clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  screen.blit(test_surface, (200, 100))
  screen.blit(text_surface, (300, 500))
  pygame.display.update()
  clock.tick(40)