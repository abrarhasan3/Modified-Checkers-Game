#board class which will handle everything on the board, like moving, drawing specific pieces
import pygame
from .constants import BLACK, ROWS, COLS,RED, SQUARE_SIZE, WHITE, TEMP #relative import-from same directory
from .piece import Piece
class Board:
    def __init__(self):
        #defining attributes of this class
        self.board = []#internal representation of the board, 2D list(8 rows and 8 cols) will have objects like red and black pieces [[WHITE, 0, WHITE, 0, WHITE],[red, 0, red , 0]] something like this. 8 interrior list [[this one], []] will have 8 differet pieces that tell if they are white, red, king etc--meaning for each row we get if a cell has a piece or not and check the list's pos
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

    def evaluate(self):
        #would tell us given the state of the board what is the score--on the basis of how many kings and pieces we have--score +/- --white = ai--also the score we prioritise becoming king--when whiteking<redking it will be subtracted from score
        return self.white_left-self.red_left+(self.white_kings*0.5 - self.red_kings*0.5)

    def get_all_pieces(self, color):
        #here all same color pieces currently on board will be received and all their valid moves will be found together
        pieces = []
        for row in self.board:
            for piece in row:
                if piece!=0 and piece.color==color:
                    pieces.append(piece)
        return pieces
    
        #above we are checking the board 2D list, if a position is 0 meaning doesnt have a piece and of the color we requested we append it to list pieces

    def move(self, piece, row, col):
        #which piece, and to where(row, col), and then delete it from current
        #move piece within the list and then update the piece
        self.board[piece.row][piece.col], self.board[row][col]=self.board[row][col], self.board[piece.row][piece.col] #swaping position in a list -- the new pos wont have a piece so it will go to currently selected's place and the piece will go to blank place--the piece will move from piece.row,col to row,col type something
        piece.move(row, col)
        #for checking if becoming king--last row--pieces that are in last row wont be kkings without making any move--only kings can go backward so if king move back to it's starting position still stays a king
        if row == ROWS-1 or row == 0:
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
    def remove(self, pieces):
        for piece in pieces:
            #we will look through all pieces and remove needed ones
            self.board[piece.row][piece.col] = 0
            #print(piece.row, piece.col)
            if piece != 0:
                if piece.color == RED:
                    self.red_left-=1
                else:
                    self.white_left-=1
    def winner(self):
        if self.red_left<=0:
            return WHITE
        elif self.white_left<=0:
            return RED
        return None #if no one won
    def get_valid_moves(self, piece):
        #check color - red goes downward, so for each piece check left right diagonally at each row--1left and 1down, if it has a piece or blank, if has is the piece of same color as moving piece--cant move, if blank -- move, if has opposite color check if can jump over diagonally--check next row, if blank--valid--same for right diagonal--if jumped track for removed piece
        #double jumping--if jumped over 1piece check if we can jump over any other piece diagonally--valid only if can jump over another piece and add moves to the set
        moves = {} #dictionary for what place can move--as row,col-- (4,5) available space and it will be key and value will be any pieces we jump to that move and (4,5): [(3, 4)]--jumped over 3,4 to get to 4,5
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        #for checking move upward/downward/king_for both--king piece will satisfy both conditions
        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row-1, max(row-3, -1), -1, piece.color, left))
            #this will traverse and update--row-1(start) means move up to check for valid, how many rows looking(stop)max(2rows above now row or -1) highest can take row0--dont wanna check for more than 3rows, -1 means move up, left means col-where we subtract upwards

            moves.update(self._traverse_right(row-1, max(row-3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row+1, min(row+3, ROWS), +1, piece.color, left))
            moves.update(self._traverse_right(row+1, min(row+3, ROWS), +1, piece.color, right))
        return moves #merges the dictionary and returns
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        #checks left diagonal
        #start, stop, step is for FOR loop, step--do i go up/down, skipped--have we skipped any pieces--if we have we can skip to another piece
        moves = {}
        last = []
        for r in range (start, stop, step):
            if left<0:
                #outside of board
                break
            current = self.board[r][left]#keeps track of left
            if current == 0:#means found an empty square
                if skipped and not last:
                    #if we skipped and found blank -break-if we can't jump over another piece for being a valid move--skipped and didn't find another to skip over 
                    break
                elif skipped:
                    #in double jumping--combines last piece we jumped with the piece we skipped--to know whether we can jump 1/2
                    moves[(r, left)] = last+skipped
                    #print((r, left))

                else: #for didn't skip anything
                    moves[(r, left)] = last #if empty and last exists means we can jump over it and if no piece of other color--will add move cause last is empty list
                if last:
                    #we found something to jump over--but didn't jump for the chance of finding double or tripke jump--skipped over
                    if step == -1:
                        row = max(r-3, 0)
                    else: 
                        row = min (r+3, ROWS)
                    #at a new pos and have to calculated where to stop
                    #calling recursively to check if we can jump more
                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))
                    
                break #after this no more valid moves
            elif current.color==color:#if not empty and the piece is same color as our piece, can move
                break
            else:#means opponents color--assuming that there's a empty sq next we can jump on top of that
                last = [current]#if we can jump we loop again and check the next diagonal sq 
            left -=1
        return moves
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
            moves = {}
            last = []
            for r in range (start, stop, step):
                if right>=COLS:
                    #outside of board
                    break
                current = self.board[r][right]#keeps track of left
                if current == 0:#means found an empty square
                    if skipped and not last:
                        #if we skipped and found blank -break-if we can't jump over another piece for being a valid move--skipped and didn't find another to skip over 
                        break
                    elif skipped:
                        #in double jumping--combines last piece we jumped with the piece we skipped--to know whether we can jump 1/2
                        moves[(r, right)] = last+skipped
                        #print((r, right))

                    else: #for didn't skip anything
                        moves[(r, right)] = last #if empty and last exists means we can jump over it and if no piece of other color--will add move cause last is empty list
                    if last:
                        #we found something to jump over--but didn't jump for the chance of finding double or tripke jump--skipped over
                        if step == -1:
                            row = max(r-3, 0)
                        else: 
                            row = min (r+3, ROWS)
                        #at a new pos and have to calculated where to stop
                        #calling recursively to check if we can jump more
                        moves.update(self._traverse_left(r+step, row, step, color, right-1, skipped=last))
                        moves.update(self._traverse_right(r+step, row, step, color, right+1, skipped=last))
                    break #after this no more valid moves
                elif current.color==color:#if not empty and the piece is same color as our piece, can move
                    break
                else:#means opponents color--assuming that there's a empty sq next we can jump on top of that
                    last = [current]#if we can jump we loop again and check the next diagonal sq 
                right +=1
            return moves

