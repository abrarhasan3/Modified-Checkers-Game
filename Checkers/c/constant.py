
import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

#rgb
RED = (0,0,0)
MOVE_COLOR = (0,102,204)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREY = (128,128,128)
CROWN = pygame.transform.scale(pygame.image.load('c/king.png'), (44,25))
ARROW = pygame.transform.scale(pygame.image.load('c/arrow.png'), (44,25))

