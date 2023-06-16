import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8

#INTEGER DIVIDE
SQUARE_SIZE = WIDTH//COLS
 #PYGAE HAS RGB COLORS ONLY
RED = (255, 51, 51)
TEMP = (0, 102, 204)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#BLUE FOR WHAT SQUARE THE PERSON CAN MOVE TO 
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

#loading crown and resizing
CROWN = pygame.transform.scale( pygame.image.load('assets/crown.png'), (44, 25))
#44,25 makes the image small enough to put it on direct center

