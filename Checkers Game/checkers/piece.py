import pygame
from .constants import RED, GREY,SQUARE_SIZE, WHITE, CROWN

class Piece:
    PADDING = 15 #how much padding we want from each side
    OUTLINE = 2 #outline/border to be
    def __init__(self, row, col, color):
        #we need to pass which row, col and color
        self.row = row
        self.col = col 
        self.color = color 
        self.king = False #tells if it's a king piece, if king piece we can jump backwards
        #a piece becomes king when it reaches last row

        #direction for each piece, neg or pos, where are we going basically, meaning for white piece(on top) they must move downward, direction pos, for red piece, it goes upward
        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        #calculates our x,y position based or row and col
        self.x = SQUARE_SIZE*self.col +SQUARE_SIZE //2  #horizontal axis=x and it's col (SQUARE_SIZE*self.col) and for being on the middle of the square (SQUARE_SIZE //2)->as circular piece is drawn from center with radius, gives 50
        self.y = SQUARE_SIZE*self.row + SQUARE_SIZE//2
    def make_king(self):
        self.king = True
    def draw(self, win):
        #draws the circular piece
        radius = SQUARE_SIZE//2 - self.PADDING 
        #draw outline
        pygame.draw.circle(win, GREY, (self.x, self.y), radius+self.OUTLINE)#actual radius's 2px outside -- basically we draw a big circle(radius+outline) and on top a smaller circle
        #sq_size = 100, middle = 50 and minus the padding around 
        pygame.draw.circle(win, self.color, (self.x, self.y), radius) 
        if self.king:
            #blit means to put some image/surface on the screen, image, x, y position
            win.blit(CROWN, (self.x-CROWN.get_width()//2, self.y-CROWN.get_height()//2))#wrote in khata
    
    def move(self, row, col):
        #sets the previous row and col to new row and col
        self.row = row
        self.col = col
        self.calc_pos()
    
    def __repr__(self):
        #will help debug-shows the actual representation 
        #repr has to be string 
        return str(self.color)



        
