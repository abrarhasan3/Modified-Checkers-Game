
import pygame
from .piece import Piece
from .constant import BLACK, ROWS, RED,WHITE, SQUARE_SIZE, COLS,BLUE
#পুরা চেকারসস বোর্ড মেইনটেইন হবে এইখান থেকে
class Board:
    def __init__(self):
        self.board = []
        #এখানে বোর্ডটা একটা 2d Array এর মত। 
    # [[0,Piece,0,.....,piece,0],
    #  [piece,0,piece,.....,0,piece],
    #  [0,Piece,0,.....,piece,0]]
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()
    def draw_cubes(self, win):
        win.fill(BLACK) #পুরা উইন্ডো কালো করবে
        for row in range(ROWS):
            for col in range(row%2, COLS, 2):
                pygame.draw.rect(win, BLUE, (row* SQUARE_SIZE,col*SQUARE_SIZE, SQUARE_SIZE,SQUARE_SIZE))
        #BLUE  BLACK BLUE  BLACK....
        #Black blue  black blue....
    
    def evaluate(self):
        return self.white_left - self.red_left + (self.white_kings*0.5 - self.red_kings*0.5)
    #white king কে প্রায়োরাটাইজ করার জন্য লাস্টে কিং এর কাউন্ডের একটা রেশিও এড করা হয়েছে, এতে AI king বানানো কে প্রয়োরাটাইজ করবে
    
    #ঐ কালারের সব পিস রিটার্ন করে
    def get_all_pieces(self,color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece !=0 and piece.color == color:
                    pieces.append(piece)
        return pieces
    
    
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col]= self.board[row][col], self.board[piece.row][piece.col]
        #যে পজিশনে মুভ করতেসি সেই পজিশনের ভ্যালু swap হবে। মানে বর্তমান পজিশনটা ০ হবে, নতুন পজিশনে Piece() বসবে
        piece.move(row, col)
        
        if row==ROWS-1 or row ==0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings +=1
            else:
                self.red_kings +=1
            
    def get_piece(self, row, col):
        return self.board[row][col]
    
    
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            #প্রতিটা row এর জন্য একটা লিস্ট 
            for col in range(COLS):
                #যখন row 0 তখন আমার Peice গুলো শুধু অড কলামে হবে। Row 1 এ ইভেন কলামে হবে
                if col%2 == ((row + 1)%2):
                    if row<3:
                        self.board[row].append(Piece(row,col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row,col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
        self.board[5][0].make_corner()
        
        '''
        t = Piece(0,6, RED)
        t.make_king()
        self.red_kings+=1
        self.board[0][6] =  t
        '''
    def draw(self,win):
        #WIN মানে হল window
        self.draw_cubes(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece !=0:
                    piece.draw(win)
    
    #বোর্ড থেকে রিমুভ করসে
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col]=0
            if piece !=0:
                if piece.color == RED:
                    self.red_left-=1
                else:
                    self.white_left-=1
    def winner(self):
        if self.red_left <=0:
            return WHITE
        elif self.white_left <=0:
            return RED
        return None
                    
    
        
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col -1
        right = piece.col + 1
        row = piece.row
        if piece.color == RED or piece.king:
            moves.update(self.traverse_front(row-1,max(row-3,-1),-1,piece.color,left+1))
            #moves.update(self.traverse_left(row-1,max(row-3,-1),-1,piece.color,left))
            #moves.update(self.traverse_right(row-1,max(row-3,-1),-1,piece.color,right))
        if piece.color == WHITE or piece.king:
            moves.update(self.traverse_front(row+1,min(row+3,ROWS),1,piece.color,left+1))
            #moves.update(self.traverse_right(row+1,min(row+3,ROWS),1,piece.color,right))
        if piece.corner:
            t1 = self.traverse_left(row-1,max(row-3,-1),-1,piece.color,left)
            t2 = (self.traverse_right(row-1,max(row-3,-1),-1,piece.color,right))
            moves = {**moves, **t1}
            moves = {**moves, **t2}
            
        return moves
    
    
    def traverse_left(self, start, stop, step, color, left, skipped =[]):
        moves = {}
        last = []
        for r in range (start, stop, step):
            if left<0:
                break
            current = self.board[r][left]
            
            if current==0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,left)]=last+skipped
                else:
                    moves[(r,left)] = last
                if last:
                    if step== -1:
                        row=max(r-3,0)
                    else:
                        row= min(r+3, ROWS)
                    moves.update(self.traverse_left(r+step, row, step, color, left-1, skipped=last))
                    moves.update(self.traverse_right(r+step, row, step, color, left+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
                    
            left-=1
        return moves
            
    def traverse_right(self, start, stop, step, color, right, skipped =[]):
        moves = {}
        last = []
        for r in range (start, stop, step):
            if right>=COLS:
                break
            current = self.board[r][right]
            if current==0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)]=last+skipped
                else:
                    moves[(r,right)] = last
                if last:
                    if step== -1:
                        row=max(r-3,0)
                    else:
                        row= min(r+3, ROWS)
                    moves.update(self.traverse_left(r+step, row, step, color, right-1, skipped=last))
                    moves.update(self.traverse_right(r+step, row, step, color, right+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
                    
            right +=1
        return moves
    
    def traverse_front(self, start, stop, step, color, col, skipped =[]):
        moves = {}
        last = []
        for r in range (start, stop, step):
            if r<0 or r>7:
                break
            current = self.board[r][col]
            
            if current==0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,col)]=last+skipped
                else:
                    moves[(r,col)] = last
                if last:
                    if step== -1:
                        row=max(r-3,0)
                    else:
                        row= min(r+3, ROWS)
                    moves.update(self.traverse_front(r+step, row, step, color, col, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
        return moves
    
    
    
                
        