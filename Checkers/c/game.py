
import pygame
from c.board import Board
from .constant import RED, WHITE, BLUE,SQUARE_SIZE,MOVE_COLOR
class Game:
    def __init__(self,win):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}
        self.win = win
#WIN= Window
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
    
    def winner(self):
        return self.board.winner()
 
        
    def reset(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
    
# যখন কোনো Piece Select হবে তখন এই মেথড কল হবে। কোন Piece সিলেক্ট করলে আমরা ২ টা কাজ করতে পারি
#হয় কোনো মুভ দেয়া অথবা নতুন একটা পিস সিলেক্ট করা
    def select(self, row, col):
        if self.selected:
            result = self._move(row,col)
            if not result:
                self.selected = None
                self.select(row, col)
            #যদি ভ্যালিড মুভ  না হয় তাইলে সিলেক্টন None করে দিবে , এরপরে আবার সেইম মেথড কল করে মুভ দিতে বলবে
            
#প্রথমবার যখন মাউস ক্লিক হবে তখন সিলেক্টড None থাকবে। তাহলে তখন এই যে ভ্যালিড মুভগুলা লিস্টে স্টোর হল। এরপরের বার যখন কোনো মুভ দিবে তখন if টা ট্রু হবে।      
        else:
            piece = self.board.get_piece(row,col)
            if piece !=0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        return False
    
    
    
#চেক করতেসে সে যায়গায় যাওয়ার জন্য মুভ দিসি সেটাতে কোনো পিস আছে কিনা, অথবা সেটা ভ্যালিড মুভ কিনা, যদি না হয় তাইলে False 
#return করবে।       
    def _move(self, row, col):
        piece = self.board.get_piece(row,col)
        if self.selected and piece == 0 and (row,col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row,col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True
    
    def draw_valid_moves(self,moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, MOVE_COLOR, (col*SQUARE_SIZE+SQUARE_SIZE//2, row*SQUARE_SIZE+SQUARE_SIZE//2), 15)
            
    def change_turn(self):
        self.valid_moves = {}
        if self.turn==RED:
            self.turn= WHITE
        else:
            self.turn=RED
            main_font = pygame.font.SysFont("comicsans", 30)
            livees_label = main_font.render(f"Your Turn", 1, WHITE)
            self.win.blit(livees_label, (800, 400))
            
    def get_board(self):
        return self.board
    
    def ai_move(self, board):
        self.board = board
        self.change_turn()
        