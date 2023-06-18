
import pygame
from .constant import RED, WHITE, SQUARE_SIZE, GREY, SPEAR_BLACK, SPEAR_WHITE,CROWN,CROWN_WHITE ,WIZ_BLACK,WIZ_WHITE
class Piece:
    PADDING = 15
    BORDER = 2
    def __init__(self,row,col,color):
        self.row=row
        self.col=col
        self.color=color
        self.corner = False
        self.king = False            
        self.x =0
        self.y =0
        self.calc_pos()
    def calc_pos(self):
        self.x = SQUARE_SIZE *  self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE *  self.row + SQUARE_SIZE // 2
#এখানে Square Size হল একটা row বা কলামের সাইজ। তাহলে destination কলামের মিড পয়েন্টের (x,y) কোঅর্ডিনেট রিটার্ন করসে


    def make_king(self):
        self.king = True
        
        
    def make_corner(self):
        self.corner = True
        
        
    def draw(self, win):
        radious = SQUARE_SIZE // 2 - self.PADDING
        
        if self.color == RED:
            pygame.draw.circle(win, WHITE,(self.x,self.y),radious+self.BORDER)
            pygame.draw.circle(win, (0,0,0),(self.x,self.y),radious)
            pygame.draw.circle(win, WHITE,(self.x,self.y),radious-10)
            pygame.draw.circle(win, (0,0,0),(self.x,self.y),radious-10-self.BORDER)
        else:
            pygame.draw.circle(win, (0,0,0),(self.x,self.y),radious+self.BORDER)
            pygame.draw.circle(win, self.color,(self.x,self.y),radious)
            pygame.draw.circle(win, (0,0,0),(self.x,self.y),radious-10)
            pygame.draw.circle(win, self.color,(self.x,self.y),radious-10-self.BORDER)
            
            
        if self.corner:
            if self.color==RED:
                
                win.blit(SPEAR_WHITE,(self.x- SPEAR_WHITE.get_width()//2, self.y - SPEAR_WHITE.get_height()//2))
                
            else:
                win.blit(SPEAR_BLACK,(self.x- SPEAR_BLACK.get_width()//2, self.y - SPEAR_BLACK.get_height()//2))
            
            
        
        if self.king and self.color==RED:
            if self.corner:
                pygame.draw.circle(win, (0,0,0),(self.x,self.y),radious-10-self.BORDER)
                win.blit(WIZ_WHITE ,(self.x- WIZ_WHITE.get_width()//2, self.y - WIZ_WHITE.get_height()//2))
            else:
                win.blit(CROWN_WHITE,(self.x- CROWN.get_width()//2, self.y - CROWN.get_height()//2))
        elif self.king and self.color==WHITE:
            if self.corner:                
                pygame.draw.circle(win, (255,255,255),(self.x,self.y),radious-10-self.BORDER)
                win.blit(WIZ_BLACK ,(self.x- WIZ_BLACK.get_width()//2, self.y - WIZ_BLACK.get_height()//2))
            else:
                win.blit(CROWN,(self.x- CROWN.get_width()//2, self.y - CROWN.get_height()//2))
            
            #এখানে (x,y) হল স্কয়ারের সেন্টার। কিন্তু এখন যদি আমরা ডিয়েক্ট (x,y) দিয়ে ড্র করি তাহলে হবে না, কারণ ইমেজ শুরু হবে তখন x,y তে
            #তাই ইমেজের width এর অর্ধেক বিয়োগ করতে হবে 
        
                            
    
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
        #এখানে row,col ভ্যালু আপডেট করছি এবং calc_pos() দিয়ে (x,y)এর ভ্যালু আপডেট করলাম
    
    
    def __repr__(self):
        return str(self.color)
    #অবজেক্ট প্রিন্ট করলে যেন কালার আসে