import pygame,sys
from library.Setting import *

pygame.init()

screen = pygame.display.set(lebar, tinggi)

running = True
while running:
  for event in pygame.events.get():
    if event.type == pygame.QUIT:
      running = False 
