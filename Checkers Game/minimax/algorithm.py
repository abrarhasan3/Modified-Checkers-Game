from copy import deepcopy
#shallowcopy imports only the ref, deepcopy copies the ref and object--gonna need it to copy the board multiple times
#in shallow, x=[] y=x x[0]=1 then y[0]=1
#in deep, values in x and y wont change each other

import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game):
    #position->the current pos->board object
    #minimax will have board from board.get_all_pieces and it will give the best position/board we can have after that
    #depth->how far want to extend the decision tree->decrement and recursive call-for each call will decrease
    #max_player->boolean->tells if we are maximizing or minimizing the value of score
    #game->game object we get from main.py file
    #we evaluate a position only when we reach the end of the tree->so first get depth->then go bottom-up to root
    if depth == 0 or position.winner()!=None:
        #when at the last node of a tree, get the actual position and evaluate and return them as what evaluation goes with which position
        #if won the game no need to do further evaluation
        return position.evaluate(), position
    if max_player:
        #maximize the score
        #each time we check for best position and initially -inf is best and for max value anything higher than -inf we change
        maxEval = float('-inf')
        best_move = None #best move we can make

        #get_all_moves get all possible moves for out current position and ai is white and game is for drawing--visualize
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game) [0]
            #for every move we evaluate so we decrease the depth and go to next level and when depth =0 it'll give the pos's evaluation->meaning we going downward from root and at the end getting the eval score

            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move #if its best move seen so far save it
        return maxEval, best_move
    else:
        #minimize
        minEval = float('inf')
        best_move = None 
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game) [0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move 
        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    #move[0] = row, move[1] = col
    board.move(piece, move[0], move[1])
    if skip:
        #skipped a piece
        board.remove(skip)
    return board

def get_all_moves(board, color, game):
    #we can get all the pieces from board.py and check all moves
    moves = [] 
    #moves will store like this [[board, piece], [...]]->if we move that piece the state of new board will be that
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        #in valid_moves dictionary, (row, col) = [pieces if we skipped this row-col]-- .item will give key, value pair like this and the pieces will say which ones to remove after that move
        #move is row, col and skip is the piece we skip
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            #we save the copy of modified board everytime and not replace the same board else we will be trying everything on the changed board and lose the main state

            #for coping pos of pieces
            temp_piece = temp_board.get_piece(piece.row, piece.col)

            new_board = simulate_move(temp_piece, move, temp_board, game, skip) #will take the piece and what move want to do->do the move on temp board and return the new board
            #moves.append([new_board, piece])#store the new board and for which piece and then score it in minimax
            moves.append(new_board) #for now dont need piece-if need to draw the piece and draw circle around it, we'll use upper code 
    return moves