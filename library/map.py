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

  # def map_scroll_x(self):
  #   player = self.player.sprite
  #   player_x = player.rect.centerx
  #   arah_x = player.direction.x

  #   if player_x < 200 and arah_x < 0:
  #     self.world_shift = 8
  #     player.speed = 0
  #   elif player_x > 200 and arah_x > 0:
  #     self.world_shift = -8
  #     player.speed = 0
  #   else:
  #     self.world_shift = 0
  #     player.speed = 8
  
  def run(self):
    self.Tile.update(0)
    self.tiles.draw(self.display_surface)