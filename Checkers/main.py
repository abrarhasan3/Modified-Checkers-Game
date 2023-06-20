import pygame,sys
pygame.font.init()
from c.constant import WIDTH,HEIGHT, SQUARE_SIZE, RED, WHITE, BG, Play_Again
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
        WIN.blit(BG, (0, 0))
        
        pygame.draw.rect(WIN,(116, 116, 116), (0, 400, WIDTH+200, 100))
        
        if(winner == RED):
            livees_label = main_font.render(f"YOU WIN", 1, WHITE)
            WIN.blit(livees_label, (livees_label.get_width()+150, 400+20))
        else:
            livees_label = main_font.render(f"YOU LOSE", 1, WHITE)
            WIN.blit(livees_label, (livees_label.get_width()+130, 400+20))
            
        WIN.blit(Play_Again, (Play_Again.get_width()+200, 600))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                a, b = pygame.mouse.get_pos()
                if Play_Again.get_width()+200 <= a <= (Play_Again.get_width())*2+200 and 600<=b<=600+Play_Again.get_height():
                    main()
                else:
                    pass
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            

           
           
        
            
            

def main():
   run = True
   clock = pygame.time.Clock() 
   main_font = pygame.font.SysFont("comicsans", 30)
   # কোনো কম্পিউটার ফাস্ট হলে ফাস্ট গেম রান হবে, স্লো হলে স্লো, এটা প্রিভেন্ট করে একটা
   #কন্সট্যান্ট ফ্রেম রেটের জন্য এই লাইন
   
   game = Game(WIN)
   while run:
       clock.tick(FPS)
       
       if game.turn == WHITE:
           pygame.display.set_caption('AI')
           value, new_board = minimax(game.get_board(), 3, WHITE, game)
           game.ai_move(new_board)
           #print(value)
       else:
           pygame.display.set_caption('Your turn')
       
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
        
        #WIN.fill(RED)
        screen = pygame.transform.scale(pygame.image.load('c/open.png'), (1000,612))
        play = pygame.transform.scale(pygame.image.load('c/play_btn.png'), (200,100))
        WIN.blit(screen,(0,94))
        WIN.blit(play,(130,350))
        pygame.display.update()
    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                a, b = pygame.mouse.get_pos()
                if 130 <= a <= 130+play.get_width() and 350<=b<=350+play.get_height():
                    main()                    
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
       
                    

splash_screen()
#main()
#game_over(WHITE)