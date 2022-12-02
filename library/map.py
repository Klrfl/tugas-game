import pygame
from library.Setting import ukuran
from library.tile import Tile

class Map:
  def __init__(self,level_map,surface):
    self.display_surface = surface
    # self.level_map = level_map
    self.setup_level(level_map)

  def setup_level(self,layout):
    self.tiles = pygame.sprite.Group()
    for row_index,row in enumerate(layout):
      for col_index,cell in enumerate(row):
        if cell == "X":
          x = col_index * ukuran
          y = row_index * ukuran
          tile = Tile((x, y), ukuran)
          self.tiles.add(tile)

    for row in layout:
      print(row)
  
  def run(self):
    self.Tile.update(0)
    self.tiles.draw(self.display_surface)