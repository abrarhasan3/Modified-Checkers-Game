# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:03:37 2023

@author: Jafar
"""

import pygame

#__INIT__.PY TELLS THAT, CHECKERS FOLDER IS A PYTHON PACKAGE AND THAT'S WHY WE CAN IMPORT THINGS FROM IT AND IF WE WRITE FROM CONSTANCE IMPORT *, WE DONT HAVE TO WRITE .CONSTANCE HERE
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.board import Board
from checkers.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#CAPTION
pygame.display.set_caption('Checkers')

#making the mouse handle moves
def get_row_col_from_mouse(pos):
    #takes the position of mouse/piece and give us which row,col we are clicking on, pos is a tuple
    #on mouse down we will get position and move piece to there or selects that piece
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col 

#main func that runs when we play the game
def main():
    #creating an event loop to check every sec if we pressed on something
    run = True
    Clock = pygame.time.Clock()#pygame has a clock that checks our event loop doesnt run too fast or too slow
    #creating board object
    #board = Board()#changed to game.py
    game = Game(WIN)

    
    #while loops does the event controlling and drawing
    while run:
        Clock.tick(FPS)
        #this for loop will check if an events happend in the current time, if have they will be in the list of pygame.event.get
        for event in pygame.event.get():
            #now we check if the event is of a specific type, like quit - we quit the game
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #where are we moving etc things will be checked if we click any button on our mouse
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                #piece = board.get_piece(row, col) 
                #board.move(piece, 4, 3)
        #for each end loop, draws on window
        #board.draw(WIN)#changed into game.py
        #pygame.display.update()#when update the display, draw is called, on top of each other
        game.update()
    #this will get rid of the window that will pop up
    pygame.quit()
main()