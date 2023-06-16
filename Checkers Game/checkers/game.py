#for handling the game -- can we move here, selecting a piece etc
#game doesn't only work by mouse pressing, it works for the AI as well
import pygame
from .constants import RED, WHITE
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win#destroys the win so that dont have to pass everytime
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()
    
    def _init(self):
        #'_' makes this func private-for calling it have to call reset
        #initializes the game
        self.selected = None #what piece is selected
        self.board = Board()#from main board=Board()wont happen now, from main we will create a game and this game will control the board for us
        self.turn = RED 
        self.valid_moves = {}#current valid moves

    def reset(self):
        self._init()

    def select(self, row, col):
        #when selected a piece tells the row, col of selected -- for selecting/deselection --giving input to a method
        #if valid move the selected piece to row, col if not again recall this function and the same thing will happen for reselected piece
        if self.selected:
            result = self._move(row, col)#we will try to move the selected to a row,col we have chosen
            if not result:
                self.selected = None#resets selection
                self.select(row, col)#reselects row-col-recursion
                #if not valid move select a new one type
        else: 
            piece = self.board.get_piece(row, col)
            if piece!=0 and piece.color == self.turn:
                #piece!=0--some piece is selected
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True #if selection valid return true
        return False
        
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            #selected something and there's no other piece on the new position and the new pos is valid
            self.board.move(self.selected, row, col)#currently selected piece will be moved to row, col
            self.change_turn()
        else:
            return False
        return True
    def draw_valid_moves(self, move):
        #42:59
    def change_turn(self):
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
