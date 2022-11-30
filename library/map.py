import pygame
from library.Setting import ukuran
from library.tile import *

class Map:
  def __init__(self,level_map,surface):
    self.displaySurface = surface
    self.set(level_map)

  def set(self,layout):
    self.tile = pygame.sprite.Group()
    for rowIndex,row in enumerate(layout):
      for colIndex,cols in enumerate(row):
        if cols == 'X':
          x = colIndex * ukuran
          y=rowIndex * ukuran
          tile = Tile((x,y),ukuran)
          self.tiles.add(tile)
  def exec(self):
    self.Tile.update(0)
    self.tile_draw(self.displaySurface)