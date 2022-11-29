import pygame
from library.Setting import *
from library.tile import Tile
# from library.map import Map

pygame.init()

# set screen
screen = pygame.display.set_mode((lebar, tinggi))

# set title
pygame.display.set_caption('Mario clone')

# set surfaces
sky_surface = pygame.image.load("asset/Sky.png")
ground_surface = pygame.image.load("asset/Ground.png")

# text
test_font = pygame.font.Font(None, 50)
text_surface = test_font.render("tes", False, 'White')

test_tile = pygame.sprite.Group(Tile((200,100),200))
# map = Map(map,screen)

# clock obj for framerate
clock = pygame.time.Clock()


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  screen.blit(sky_surface, (0, 0))
  screen.blit(ground_surface, (0, 450))
  
  test_tile.draw(screen)
  
  # map.exec()
  pygame.display.update()
  clock.tick(40)