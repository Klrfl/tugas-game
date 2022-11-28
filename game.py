import pygame

pygame.init()

screen = pygame.display.set(800, 600)

running = True
while running:
  for event in pygame.events.get():
    if event.type == pygame.QUIT:
      running = False 