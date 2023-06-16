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
        #when selected a piece tells the row, col of selected -- for selecting/deselection 
        
    def move(self, row, col):
        #bbb
