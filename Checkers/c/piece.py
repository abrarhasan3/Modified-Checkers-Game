
import pygame
from .constant import RED, WHITE, SQUARE_SIZE, GREY, CROWN, ARROW
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
        pygame.draw.circle(win, GREY,(self.x,self.y),radious+self.BORDER)
        pygame.draw.circle(win, self.color,(self.x,self.y),radious)
        if self.king:
            win.blit(CROWN,(self.x- CROWN.get_width()//2, self.y - CROWN.get_height()//2))
            #এখানে (x,y) হল স্কয়ারের সেন্টার। কিন্তু এখন যদি আমরা ডিয়েক্ট (x,y) দিয়ে ড্র করি তাহলে হবে না, কারণ ইমেজ শুরু হবে তখন x,y তে
            #তাই ইমেজের width এর অর্ধেক বিয়োগ করতে হবে 
        if self.corner:
            win.blit(ARROW,(self.x- ARROW.get_width()//2, self.y - ARROW.get_height()//2))            
    
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
        #এখানে row,col ভ্যালু আপডেট করছি এবং calc_pos() দিয়ে (x,y)এর ভ্যালু আপডেট করলাম
    
    
    def __repr__(self):
        return str(self.color)
    #অবজেক্ট প্রিন্ট করলে যেন কালার আসে