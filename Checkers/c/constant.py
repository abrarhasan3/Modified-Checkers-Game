
import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

#rgb
RED = (255,0,0)
MOVE_COLOR = (0,102,204)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('c/king.png'), (44,25))
CROWN_WHITE = pygame.transform.scale(pygame.image.load('c/king_white.png'), (44,25))
SPEAR_BLACK = pygame.transform.scale(pygame.image.load('c/spear.png'), (32,32))
SPEAR_WHITE = pygame.transform.scale(pygame.image.load('c/spear_white.png'), (32,32))
WIZ_BLACK = pygame.transform.scale(pygame.image.load('c/wiz_black.png'), (40,40))
WIZ_WHITE = pygame.transform.scale(pygame.image.load('c/wiz_white.png'), (40,40))

