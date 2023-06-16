#board class which will handle everything on the board, like moving, drawing specific pieces
import pygame
from .constants import BLACK, ROWS, COLS,RED, SQUARE_SIZE, WHITE, TEMP #relative import-from same directory
from .piece import Piece
class Board:
    def __init__(self):
        #defining attributes of this class
        self.board = []#internal representation of the board, 2D list(8 rows and 8 cols) will have objects like red and black pieces [[WHITE, 0, WHITE, 0, WHITE],[red, 0, red , 0]] something like this. 8 interrior list [[this one], []] will have 8 differet pieces that tell if they are white, red, king etc
        #self.selected_piece = None #--now in game
        self.red_left = self.white_left = 12 #how many pieces we have, initially we have 12 each, when chosen a piece we will minus
        self.red_kings = self.white_kings = 0
        self.create_board()#creates the board where we get our pieces
    def draw_squares(self, win):
        #win means window or surface and we will draw the board like red-black-red pattern 
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row%2, COLS, 2):
                #row%2(initializtion of loop) means, if we start by row=0, 0x0 of board will be red, then increment by 2, 0x2 will be red like this, for row=1, 1%2=1, 1x1 will be red
                pygame.draw.rect(win, TEMP, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) #draws a red rect on window and draw happens from top left coordinate so (x,y)=(0,0) and as we go to right x increases and go bottom y inc. at bottom will be 800. at 0,0 draw a 100 width and 100 long square suppose. x = row*square_size, y = col*sq_size, width = sq_size, height = sq_size, x&y calculates where top left is. changed red to temp

    def move(self, piece, row, col):
        #which piece, and to where(row, col), and then delete it from current
        #move piece within the list and then update the piece
        self.board[piece.row][piece.col], self.board[row][col]=self.board[row][col], self.board[piece.row][piece.col] #swaping position in a list -- didn't understand did what--the piece will move from piece.row,col to row,col type something
        piece.move(row, col)
        #for checking if becoming king--last row--pieces that are in last row wont be kkings without making any move--only kings can go backward so if king move back to it's starting position still stays a king
        if row == ROWS or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings+=1
            else:
                self.red_kings+=1
    #for getting a piece to send to move() for making a move
    def get_piece(self, row, col):
        return self.board[row][col]
    def create_board(self):
        #create the actual internal representation of the board and add pieces to the list from piece.py
        #making the pieces and keeping track in a list of the location where piece is to be
        #4 in each row--white goes up
        for row in range(ROWS):
            self.board.append([])#interior list for each row--what each row will have
            for col in range (COLS):
                if col%2 == ((row+1)%2):
                    #if current col=0, 0%2=0, (0+1)%2=1 wont draw...col = 3%2=1 == 1-->draw piece_so for row is even we draw on odd cols and for row is odd we draw on even cols
                    if row<3:
                        #for white row(0, 1, 2)
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row>4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        #for row 3&4--blank piece--for keeping track--if not give a piece
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        #will draw all the pieces in the square
        self.draw_squares(win)#draws square for whole checker board
        #for loop draws the pieces
        for row in range(ROWS):
            for col in range(COLS):
                #loop through the board
                piece = self.board[row][col]
                if piece!=0:
                    #appended 0 above
                    piece.draw(win)#didnt understand this
                