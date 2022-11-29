import pygame

class Tile(pygame.sprite.Sprite()):
  def __init__(self,pos,ukuran):
    super().__init__()
    self.Surface = pygame.Surface((size,size))
    self.Surface.fill("Brown")
    self.rect = self.Surface.get_rect(topl = pos)