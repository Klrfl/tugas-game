import pygame

class Tile(pygame.sprite.Sprite):
  def __init__(self, pos, ukuran):
    super().__init__()
    self.image = pygame.Surface((ukuran, ukuran))
    self.image.fill("Brown")
    self.rect = self.image.get_rect(topleft = pos)