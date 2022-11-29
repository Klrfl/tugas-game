import pygame
from tile import Tile

class Map:
  def __init__(self,level_map,surface):
    self.displaySurface = surface
    self.set(level_map)

    def set(self,layout):
      self.tile = pygame.sprite.Group()
      for row in layout:
        print(row)

    def exec(self):self.tile_draw(self.displaySurface)