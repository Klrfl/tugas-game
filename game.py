import pygame
from library.Setting import *
from library.tile import Tile
from library.map import Map

pygame.init()

# set screen
screen = pygame.display.set_mode((lebar, tinggi))

# set title
pygame.display.set_caption('Mario clone')

# set surfaces
sky_surface = pygame.image.load("asset/Sky.png").convert()
ground_surface = pygame.image.load("asset/Ground.png").convert()

player_surface = pygame.image.load("asset/Sprite.png").convert()
player_x_pos = 0
# text
test_font = pygame.font.Font(None, 50)
text_surface = test_font.render("Mario clone", False, 'White')

map = Map(map,screen)

# clock obj for framerate
clock = pygame.time.Clock()


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  # render sky, ground, text
  screen.blit(sky_surface, (0, 0))
  screen.blit(ground_surface, (0, 445))

  player_x_pos += 0
  screen.blit(player_surface, (player_x_pos, 375))

  screen.blit(text_surface, (420, 50))
  
  map.run()
  
  pygame.display.update()
  clock.tick(40)