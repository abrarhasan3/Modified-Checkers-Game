from copy import deepcopy
import pygame


RED = (255,0,0)
WHITE = (255,255,255)

#position হল কারেন্ট পজিশন, depth হল ট্রি কত ডেপথ পর্যন্ত ট্রাই করবো
#minmax একটা বোর্ড রিটার্ন করবে, moves.append[new_board] এইলাইনে বোর্ড এর সিচুয়েশন এসাইন হচ্ছে
def minimax(position,depth,max_player, game):
    if depth == 0 or position.winner()!= None:
        return position.evaluate(), position
    #যখন ট্রির ডেপথ ০ হয়ে গেসে তখন আমরা ইভাল্যুয়েট করবো, এখানে position.evaluate মানে হল 
# board.evaluate, তাহলে এই বোর্ডের কারেন্ট সিচুয়েশনে আমার red piece কত, white piece কত এটা
#কাউন্ড করে ইভ্যালুয়েশন করছে।
    
    
    #এখানে ট্রি এর প্রথম এ White চাললো, এরপরে রেড চালবে, তাহলে সবগুলা মুভ সিমুলেট করে হিসাব করবে AI 
  # তাই maxEval এবং minEval সিমুলেট
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_move(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            #প্রতিটা মুভ এর জন্য ইভালুয়েশন করতেসে, রিকার্সিভ কল
            maxEval = max(maxEval,evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_move(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval,evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move
        
        
        

def simulate_move(piece,move,board,game,skip):
   board.move(piece,move[0],move[1])
   #move হল ডিকশনারির index (row,col) এমন। এখন কারেন্ট যে মুভ আছে তার row, col এখান থেকেই পাওয়া যায়
   if skip:
       board.remove(skip)
      #যদি কারো উপরে জাম্প করি তাহলে ঐ পিসটা রিমুভ করব
   return board        

       
def get_all_move(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            #draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
#এই পিসটা মুভ করলে বোর্ডের সিচ্যুয়েশন কি হবে এটা রিটার্ন করে simulate move 
            moves.append(new_board)
    return moves

def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win,(0,255,0),(piece.x,piece.y),50,5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #pygame.time.delay(100)


            