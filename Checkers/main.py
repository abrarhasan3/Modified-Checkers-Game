

import pygame
from c.constant import WIDTH,HEIGHT, SQUARE_SIZE, RED, WHITE
from c.board import Board
from c.game import Game
from minimax.algorithm import minimax

FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Checkers')

def get_col_from_mouse(pos):
    x,y = pos
    row = y//SQUARE_SIZE 
    col = x//SQUARE_SIZE
    return row,col

def main():
   run = True
   clock = pygame.time.Clock() 
   # কোনো কম্পিউটার ফাস্ট হলে ফাস্ট গেম রান হবে, স্লো হলে স্লো, এটা প্রিভেন্ট করে একটা
   #কন্সট্যান্ট ফ্রেম রেটের জন্য এই লাইন
   
   game = Game(WIN)
   while run:
       clock.tick(FPS)
       
       if game.turn == WHITE:
           value, new_board = minimax(game.get_board(), 3, WHITE, game)
           game.ai_move(new_board)
           print(value)
       
       if game.winner()!= None:
           print(game.winner())
           break
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False
               #সাইডের লাল QUIT বাটনের জন্য 
        
        #মাউসের কোনো ক্লিক হইসে কিনা চেক করার জন্য
           if event.type == pygame.MOUSEBUTTONDOWN:
               
               position= pygame.mouse.get_pos()
               row, col =  get_col_from_mouse(position)
               #print(row, col)
               if game.turn == RED:
                   game.select(row, col)                   
               else:
                   game.select(row, col)
       game.update()
       
       
        
   pygame.quit()
        
        
main()