

import pygame
pygame.font.init()
from c.constant import WIDTH,HEIGHT, SQUARE_SIZE, RED, WHITE
from c.board import Board
from c.game import Game
from minimax.algorithm import minimax

FPS = 60
WIN = pygame.display.set_mode((WIDTH+200,HEIGHT))
pygame.display.set_caption('Checkers')

def get_col_from_mouse(pos):
    x,y = pos
    row = y//SQUARE_SIZE 
    col = x//SQUARE_SIZE
    return row,col

def game_over(winner):
    run = True
    main_font = pygame.font.SysFont("comicsans", 50)
    while run:
        WIN.fill((102, 0, 51))
        pygame.draw.rect(WIN,(0, 102, 204), (100, 400, WIDTH, 100))
        
        if(winner == RED):
            livees_label = main_font.render(f"YOU WIN", 1, WHITE)
            WIN.blit(livees_label, (livees_label.get_width()+150, 400+20))
        else:
            livees_label = main_font.render(f"YOU LOSE", 1, WHITE)
            WIN.blit(livees_label, (livees_label.get_width()+130, 400+20))

        again = main_font.render(f"Play Again?", 1, (0,0,0))
        rect = pygame.draw.rect(WIN,WHITE, (100+again.get_width()+20, 600, again.get_width(), again.get_height()))
        WIN.blit(again, (100+again.get_width()+20, 600,))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                a, b = pygame.mouse.get_pos()
                if rect.x <= a <= rect.x+again.get_width() and rect.y<=b<=rect.y+again.get_height():
                    main()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    pygame.quit()

           
           
        
            
            

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
           #print(value)
       
       if game.winner()!= None:
            print(game.winner())
            
            game_over(game.winner())
            run = False
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
        

def splash_screen():
    run = True
    main_font = pygame.font.SysFont("comicsans", 50)
    while run:
        WIN.fill((102, 0, 51))
        pygame.draw.rect(WIN,(0, 102, 204), (100, 400, WIDTH, 100))
        pygame.draw.rect(WIN,(0, 0, 0), (80, 380, WIDTH-10, 90))

        again = main_font.render(f"Play Again?", 1, (0,0,0))
        rect = pygame.draw.rect(WIN,WHITE, (100+again.get_width()+20, 600, again.get_width(), again.get_height()))
        WIN.blit(again, (100+again.get_width()+20, 600,))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                a, b = pygame.mouse.get_pos()
                if rect.x <= a <= rect.x+again.get_width() and rect.y<=b<=rect.y+again.get_height():
                    main()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    pygame.quit()

splash_screen()
#main()
#game_over(WHITE)